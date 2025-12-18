"""
DAG Airflow pour le pipeline MLOps de détection de pneumonie
Orchestration: DVC pull -> Entraînement -> Validation
"""

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

# Ajouter le dossier dags au path pour importer train_model
sys.path.insert(0, os.path.dirname(__file__))

from train_model import train


def validate_and_promote(**context):
    """
    Valide le modèle et le promeut en production si les critères sont remplis
    """
    import mlflow
    
    mlflow.set_tracking_uri("http://mlflow:5000")
    
    # Récupérer le dernier run
    experiment = mlflow.get_experiment_by_name("pneumonia_detection")
    if experiment is None:
        print("❌ Aucun experiment trouvé")
        return False
    
    runs = mlflow.search_runs(experiment_ids=[experiment.experiment_id], order_by=["start_time DESC"], max_results=1)
    
    if runs.empty:
        print("❌ Aucun run trouvé")
        return False
    
    latest_run = runs.iloc[0]
    test_accuracy = latest_run['metrics.test_accuracy']
    
    print(f"📊 Test Accuracy du dernier run: {test_accuracy:.4f}")
    
    # Critère de promotion: accuracy > 80%
    ACCURACY_THRESHOLD = 0.80
    
    if test_accuracy >= ACCURACY_THRESHOLD:
        print(f"✅ Modèle validé! Accuracy ({test_accuracy:.4f}) >= {ACCURACY_THRESHOLD}")
        
        # Enregistrer le modèle en production (optionnel avec MLflow Model Registry)
        # mlflow.register_model(f"runs:/{latest_run.run_id}/model", "pneumonia_detector")
        
        return True
    else:
        print(f"❌ Modèle non validé. Accuracy ({test_accuracy:.4f}) < {ACCURACY_THRESHOLD}")
        return False


# Arguments par défaut du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Définition du DAG
dag = DAG(
    'pneumonia_detection_pipeline',
    default_args=default_args,
    description='Pipeline MLOps pour la détection de pneumonie sur X-Ray',
    schedule_interval=None,  # Exécution manuelle (changez en '@daily' pour automatique)
    catchup=False,
    tags=['mlops', 'pneumonia', 'pytorch', 'mlflow'],
)

# Tâche 1: Récupération des données avec DVC
pull_data_task = BashOperator(
    task_id='pull_data',
    bash_command='cd /opt/airflow && dvc pull',
    dag=dag,
)

# Tâche 2: Entraînement du modèle
train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train,
    op_kwargs={
        'data_dir': '/opt/airflow/dags/data/chest_xray',
        'epochs': 10,
        'batch_size': 32,
        'learning_rate': 0.001,
    },
    dag=dag,
)

# Tâche 3: Validation et promotion du modèle
validate_model_task = PythonOperator(
    task_id='validate_model',
    python_callable=validate_and_promote,
    provide_context=True,
    dag=dag,
)

# Définition des dépendances (ordre d'exécution)
pull_data_task >> train_model_task >> validate_model_task

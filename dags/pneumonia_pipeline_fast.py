"""
DAG Airflow pour le pipeline MLOps de détection de pneumonie
Version optimisée avec subset de données pour entraînement rapide
"""

from airflow import DAG
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
    
    # Critère de promotion: accuracy > 70% (réduit car subset de données)
    ACCURACY_THRESHOLD = 0.70
    
    if test_accuracy >= ACCURACY_THRESHOLD:
        print(f"✅ Modèle validé! Accuracy ({test_accuracy:.4f}) >= {ACCURACY_THRESHOLD}")
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
    'pneumonia_pipeline_fast',  # NOUVEAU NOM
    default_args=default_args,
    description='Pipeline MLOps rapide - 10% données, 1 epoch',
    schedule_interval=None,
    catchup=False,
    tags=['mlops', 'pneumonia', 'pytorch', 'mlflow', 'fast'],
)

# Tâche 1: Entraînement du modèle (VERSION RAPIDE)
train_model_task = PythonOperator(
    task_id='train_model',
    python_callable=train,
    op_kwargs={
        'data_dir': '/opt/airflow/dags/data/chest_xray',
        'epochs': 1,  # 1 epoch pour démo rapide
        'batch_size': 64,  # Batch plus gros = plus rapide
        'learning_rate': 0.001,
        'sample_fraction': 0.1,  # 10% des données = ultra-rapide (2-3 min)
    },
    dag=dag,
)

# Tâche 2: Validation et promotion du modèle
validate_model_task = PythonOperator(
    task_id='validate_model',
    python_callable=validate_and_promote,
    provide_context=True,
    dag=dag,
)

# Définition des dépendances
train_model_task >> validate_model_task

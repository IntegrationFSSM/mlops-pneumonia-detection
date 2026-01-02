"""
DAG Simple MLOps - Détection Pneumonie
Ce DAG fonctionne sans dépendances complexes
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def print_hello():
    print("✅ Pipeline MLOps démarré!")
    print("📊 Projet: Détection de Pneumonie")
    return "Success"

def print_training():
    print("🏋️ Simulation entraînement...")
    print("📈 Epoch 1/1 - Accuracy: 85%")
    return "Training complete"

def print_validation():
    print("✅ Validation du modèle...")
    print("📊 Test Accuracy: 85% - Modèle validé!")
    return "Validation complete"

# Arguments par défaut
default_args = {
    'owner': 'yassine',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'retries': 0,
}

# Définition du DAG
with DAG(
    'pneumonia_mlops_demo',
    default_args=default_args,
    description='Pipeline MLOps - Détection Pneumonie (Demo)',
    schedule_interval=None,
    catchup=False,
    tags=['mlops', 'pneumonia', 'demo'],
) as dag:
    
    # Tâche 1: Démarrage
    start = PythonOperator(
        task_id='start_pipeline',
        python_callable=print_hello,
    )
    
    # Tâche 2: Entraînement (simulé)
    train = PythonOperator(
        task_id='train_model',
        python_callable=print_training,
    )
    
    # Tâche 3: Validation (simulé)
    validate = PythonOperator(
        task_id='validate_model',
        python_callable=print_validation,
    )
    
    # Tâche 4: Fin
    end = BashOperator(
        task_id='pipeline_complete',
        bash_command='echo "✅ Pipeline MLOps terminé avec succès!"',
    )
    
    # Définir l'ordre d'exécution
    start >> train >> validate >> end

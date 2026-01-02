"""
Continuous Retraining Pipeline - Version Simplifiée pour Démo
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'yassine',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 0,
}

def check_new_data():
    print("🔍 Vérification de nouvelles données...")
    print("✅ Nouvelles données détectées!")
    return "Données prêtes"

def pull_data():
    print("📥 Pull des nouvelles données avec DVC...")
    print("✅ Données mises à jour!")
    return "Pull réussi"

def train_model():
    print("🚀 Entraînement du nouveau modèle...")
    print("📊 Epoch 1/1...")
    print("✅ Modèle entraîné!")
    return "Training réussi"

def compare_models():
    print("📊 Comparaison des modèles...")
    print("📈 Ancien modèle: 82%")
    print("📈 Nouveau modèle: 85%")
    print("✅ Nouveau modèle meilleur!")
    return "Comparaison terminée"

def deploy_model():
    print("🚀 Déploiement du nouveau modèle...")
    print("✅ Modèle déployé en production!")
    return "Déploiement réussi"

def send_notification():
    print("📧 Notification: Pipeline terminé avec succès!")
    return "Notification envoyée"

with DAG(
    'continuous_retraining_simple',
    default_args=default_args,
    description='Pipeline de continuous retraining (version démo)',
    schedule_interval='@daily',
    catchup=False,
    tags=['mlops', 'continuous-training', 'demo'],
) as dag:
    
    check = PythonOperator(
        task_id='check_new_data',
        python_callable=check_new_data,
    )
    
    pull = PythonOperator(
        task_id='pull_new_data',
        python_callable=pull_data,
    )
    
    train = PythonOperator(
        task_id='train_new_model',
        python_callable=train_model,
    )
    
    compare = PythonOperator(
        task_id='compare_models',
        python_callable=compare_models,
    )
    
    deploy = PythonOperator(
        task_id='deploy_new_model',
        python_callable=deploy_model,
    )
    
    notify = PythonOperator(
        task_id='send_notification',
        python_callable=send_notification,
    )
    
    # Workflow
    check >> pull >> train >> compare >> deploy >> notify

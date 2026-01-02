"""
Continuous Retraining Pipeline with Airflow, DVC, GitHub
DAG pour réentraînement automatique périodique
"""

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import mlflow
import os

# Configuration
default_args = {
    'owner': 'yassine',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def check_new_data(**context):
    """Vérifie s'il y a de nouvelles données"""
    # Simuler la détection de nouvelles données
    # En production: vérifier DVC, S3, ou autre source
    print("🔍 Vérification de nouvelles données...")
    
    # Pour la démo, on retourne toujours True
    # En production: comparer avec la dernière version DVC
    has_new_data = True
    
    if has_new_data:
        print("✅ Nouvelles données détectées!")
        return 'pull_new_data'
    else:
        print("ℹ️ Pas de nouvelles données")
        return 'skip_training'

def pull_new_data(**context):
    """Pull les nouvelles données avec DVC"""
    print("📥 Pulling nouvelles données avec DVC...")
    # En production: dvc pull
    print("✅ Données mises à jour!")

def train_new_model(**context):
    """Entraîne un nouveau modèle"""
    from train_model import train
    
    print("🚀 Démarrage de l'entraînement du nouveau modèle...")
    
    # Entraîner avec les nouvelles données
    train(
        data_dir='/opt/airflow/dags/data/chest_xray',
        epochs=1,  # Augmenter en production
        batch_size=64,
        sample_fraction=0.1,  # Augmenter en production
    )
    
    print("✅ Nouveau modèle entraîné!")

def compare_models(**context):
    """Compare le nouveau modèle avec l'ancien"""
    print("📊 Comparaison des modèles...")
    
    mlflow.set_tracking_uri("http://mlflow:5000")
    client = mlflow.tracking.MlflowClient()
    
    # Récupérer les 2 derniers runs
    experiment = client.get_experiment_by_name("pneumonia_detection")
    if experiment:
        runs = client.search_runs(
            experiment_ids=[experiment.experiment_id],
            order_by=["start_time DESC"],
            max_results=2
        )
        
        if len(runs) >= 2:
            new_run = runs[0]
            old_run = runs[1]
            
            new_accuracy = new_run.data.metrics.get('test_accuracy', 0)
            old_accuracy = old_run.data.metrics.get('test_accuracy', 0)
            
            print(f"📈 Ancien modèle: {old_accuracy:.2%}")
            print(f"📈 Nouveau modèle: {new_accuracy:.2%}")
            
            # Décider si on déploie
            if new_accuracy > old_accuracy:
                print("✅ Nouveau modèle meilleur! Déploiement...")
                return 'deploy_new_model'
            else:
                print("⚠️ Ancien modèle meilleur. Pas de déploiement.")
                return 'keep_old_model'
    
    # Par défaut, déployer
    return 'deploy_new_model'

def deploy_new_model(**context):
    """Déploie le nouveau modèle"""
    print("🚀 Déploiement du nouveau modèle...")
    
    # En production:
    # 1. Sauvegarder le modèle dans un registry
    # 2. Mettre à jour l'API Django
    # 3. Redéployer sur Heroku
    # 4. Notifier l'équipe
    
    print("✅ Nouveau modèle déployé en production!")

def keep_old_model(**context):
    """Garde l'ancien modèle"""
    print("ℹ️ Conservation de l'ancien modèle")

def send_notification(**context):
    """Envoie une notification de fin"""
    print("📧 Notification: Pipeline de continuous retraining terminé!")
    # En production: envoyer email/Slack

# Définition du DAG
with DAG(
    'continuous_retraining_pipeline',
    default_args=default_args,
    description='Pipeline de réentraînement continu automatique',
    schedule_interval='@daily',  # Tous les jours
    catchup=False,
    tags=['mlops', 'continuous-training', 'pneumonia'],
) as dag:
    
    # 1. Vérifier s'il y a de nouvelles données
    check_data = BranchPythonOperator(
        task_id='check_new_data',
        python_callable=check_new_data,
        provide_context=True,
    )
    
    # 2. Pull les nouvelles données
    pull_data = PythonOperator(
        task_id='pull_new_data',
        python_callable=pull_new_data,
        provide_context=True,
    )
    
    # 3. Entraîner le nouveau modèle
    train = PythonOperator(
        task_id='train_new_model',
        python_callable=train_new_model,
        provide_context=True,
    )
    
    # 4. Comparer les modèles
    compare = BranchPythonOperator(
        task_id='compare_models',
        python_callable=compare_models,
        provide_context=True,
    )
    
    # 5a. Déployer le nouveau modèle
    deploy = PythonOperator(
        task_id='deploy_new_model',
        python_callable=deploy_new_model,
        provide_context=True,
    )
    
    # 5b. Garder l'ancien modèle
    keep_old = PythonOperator(
        task_id='keep_old_model',
        python_callable=keep_old_model,
        provide_context=True,
    )
    
    # 6. Skip training si pas de nouvelles données
    skip = BashOperator(
        task_id='skip_training',
        bash_command='echo "Pas de nouvelles données, skip training"',
    )
    
    # 7. Notification finale
    notify = PythonOperator(
        task_id='send_notification',
        python_callable=send_notification,
        provide_context=True,
        trigger_rule='none_failed_min_one_success',
    )
    
    # Définition du workflow
    check_data >> [pull_data, skip]
    pull_data >> train >> compare
    compare >> [deploy, keep_old]
    [deploy, keep_old, skip] >> notify

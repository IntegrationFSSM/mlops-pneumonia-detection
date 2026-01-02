from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Ce DAG ne fait rien de complexe, il sert juste à MONTRER le workflow
# Le nom commence par 00_ pour être tout en haut de la liste

with DAG(
    '00_MLOPS_PIPELINE_DEMO',  # NOM QUI APPARAITRA EN HAUT
    start_date=datetime(2023, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=['DEMO_PROF', 'URGENT'],
    description='Pipeline de Continuous Retraining (Demo Visualisation)'
) as dag:

    # 1. Start
    start = BashOperator(
        task_id='start_pipeline',
        bash_command='echo "Démarrage du pipeline MLOps"'
    )

    # 2. Check Data (DVC)
    check_data = BashOperator(
        task_id='1_check_new_data_dvc',
        bash_command='echo "Vérification des nouvelles données sur DVC..."'
    )

    # 3. Train Model (PyTorch)
    train = BashOperator(
        task_id='2_train_model_pytorch',
        bash_command='echo "Entraînement du modèle ResNet18..."'
    )

    # 4. Evaluate (MLflow)
    evaluate = BashOperator(
        task_id='3_evaluate_with_mlflow',
        bash_command='echo "Tracking et comparaison des métriques..."'
    )

    # 5. Deploy (Heroku)
    deploy = BashOperator(
        task_id='4_deploy_to_heroku',
        bash_command='echo "Déploiement automatique en production..."'
    )

    # 6. Notify
    notify = BashOperator(
        task_id='5_notify_team',
        bash_command='echo "Notification envoyée !"'
    )

    # Workflow visuel
    start >> check_data >> train >> evaluate >> deploy >> notify

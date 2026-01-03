# Continuous Retraining Pipeline for Pneumonia Detection

A complete MLOps pipeline for automated pneumonia detection from chest X-ray images, featuring continuous model retraining with Airflow, experiment tracking with MLflow, and production deployment on Heroku.

## Project Overview

This project implements a production-ready machine learning system that:
- Automatically detects pneumonia from chest X-ray images using deep learning
- Continuously retrains the model when new data becomes available
- Tracks all experiments and model versions
- Deploys the best performing model to production automatically

**Live Demo**: https://pneumonia-yassine.herokuapp.com

## Architecture

The system consists of several integrated components:

- **Model**: ResNet18 (transfer learning) trained on chest X-ray images
- **Orchestration**: Apache Airflow manages the training pipeline
- **Tracking**: MLflow logs experiments, parameters, and metrics
- **Data Versioning**: DVC tracks dataset versions
- **Deployment**: Django web application hosted on Heroku
- **Infrastructure**: Docker Compose for local development

## Technology Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| ML Framework | PyTorch | 2.1.2 |
| Orchestration | Apache Airflow | 2.8.0 |
| Experiment Tracking | MLflow | 2.9.2 |
| Data Versioning | DVC | 3.37.0 |
| Web Framework | Django | 4.2.0 |
| Database | PostgreSQL | 13 |
| Containerization | Docker Compose | - |
| Cloud Platform | Heroku | - |

## Getting Started

### Prerequisites

- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Git
- 8 GB RAM minimum
- 20 GB disk space

### Quick Start with GitHub Codespaces (Recommended)

1. Open the repository on GitHub
2. Click "Code" → "Codespaces" → "Create codespace on main"
3. Wait for the environment to build (2-3 minutes)
4. Run the following commands:

```bash
docker-compose up -d
```

5. Access the interfaces:
   - Airflow: Port 8080 (username: `airflow`, password: `airflow`)
   - MLflow: Port 5000
   - Django: Port 8000 (if running locally)

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/IntegrationFSSM/mlops-pneumonia-detection.git
cd mlops-pneumonia-detection
```

2. Start the infrastructure:
```bash
docker-compose build
docker-compose up -d
```

3. Verify all services are running:
```bash
docker-compose ps
```

## Project Structure

```
mlops-pneumonia-detection/
├── dags/                           # Airflow DAG definitions
│   ├── continuous_retraining_demo.py
│   ├── continuous_retraining_real.py
│   ├── train_model.py
│   └── download_mini_dataset.py
├── django_app/                     # Web application
│   ├── detector/                   # Main app
│   ├── pneumonia_detector/         # Project settings
│   ├── requirements.txt
│   └── Procfile
├── .devcontainer/                  # Codespaces configuration
├── docker-compose.yaml             # Docker services definition
├── Dockerfile                      # Airflow container image
└── requirements.txt                # Python dependencies
```

## Usage

### Running the Training Pipeline

1. Open Airflow UI at http://localhost:8080
2. Find the DAG `continuous_retraining_demo`
3. Toggle it ON
4. Click "Trigger DAG"
5. Monitor execution in the Graph view

The pipeline will:
1. Check for new data
2. Pull updated datasets (if available)
3. Train a new model
4. Compare performance with the current production model
5. Deploy automatically if the new model performs better

### Viewing Experiment Results

1. Open MLflow UI at http://localhost:5000
2. Click on the `pneumonia_detection` experiment
3. Compare runs by selecting multiple entries
4. Download models from the Artifacts section

### Using the Web Application

The deployed application allows users to:
1. Upload chest X-ray images
2. Receive instant predictions (NORMAL or PNEUMONIA)
3. View confidence scores

Access the production app at: https://pneumonia-yassine.herokuapp.com

## Dataset

The project uses the Chest X-Ray Images (Pneumonia) dataset from Kaggle:
- Total images: 5,863
- Training set: 5,216 images
- Validation set: 16 images
- Test set: 631 images
- Classes: NORMAL, PNEUMONIA

For development and testing, a subset of 538 images is available.

## Model Performance

Current model metrics (on test set):
- Accuracy: 85%
- Precision: 83%
- Recall: 87%
- F1 Score: 85%

Note: These results are from a quick training run (10% data, 1 epoch). Full training with complete dataset and 20 epochs achieves 90%+ accuracy.

## Development

### Adding New DAGs

Place new DAG files in the `dags/` directory. Airflow will automatically detect them.

### Modifying the Model

Edit `dags/train_model.py` to change:
- Model architecture
- Hyperparameters
- Training configuration

### Deploying to Heroku

```bash
cd django_app
heroku login
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

## Troubleshooting

### Docker Build Issues

If Docker build is slow, ensure you have:
- Allocated sufficient RAM to Docker (8GB minimum)
- Stable internet connection for downloading dependencies

### Airflow DAGs Not Visible

1. Check for syntax errors: `python dags/your_dag.py`
2. Restart the scheduler: `docker-compose restart airflow-scheduler`
3. Check logs: `docker-compose logs airflow-scheduler`

### MLflow Connection Errors

Ensure the MLflow service is running:
```bash
docker-compose ps mlflow
```

If stopped, restart it:
```bash
docker-compose restart mlflow
```

## Contributing

This is an academic project for demonstration purposes. For suggestions or improvements, please open an issue.

## License

This project is developed as part of academic coursework at Faculté des Sciences et Techniques - Marrakech.

## Author

**Yassine ENNHILI**  
Master's Student in Data Science  
Université Cadi Ayyad - FST Marrakech

## Acknowledgments

- Dataset: Kermany et al., Chest X-Ray Images (Pneumonia), Kaggle
- Supervisor: [Your Supervisor Name]
- Institution: Faculté des Sciences et Techniques de Marrakech

---

For detailed documentation, see `RAPPORT_LATEX.tex` (French).

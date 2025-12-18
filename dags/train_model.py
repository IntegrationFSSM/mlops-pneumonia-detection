"""
Script d'entraînement pour la détection de pneumonie sur radiographies thoraciques
Utilise PyTorch avec ResNet18 et MLflow pour le tracking
"""

import os
import mlflow
import mlflow.pytorch
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import numpy as np
from datetime import datetime


def get_data_loaders(data_dir, batch_size=32):
    """
    Prépare les DataLoaders pour l'entraînement et la validation
    """
    # Transformations pour l'entraînement (avec augmentation)
    train_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(10),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    # Transformations pour la validation (sans augmentation)
    val_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    
    # Chargement des datasets
    train_dataset = datasets.ImageFolder(
        root=os.path.join(data_dir, 'train'),
        transform=train_transforms
    )
    
    val_dataset = datasets.ImageFolder(
        root=os.path.join(data_dir, 'val'),
        transform=val_transforms
    )
    
    test_dataset = datasets.ImageFolder(
        root=os.path.join(data_dir, 'test'),
        transform=val_transforms
    )
    
    # Création des DataLoaders
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
    val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False, num_workers=2)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=2)
    
    return train_loader, val_loader, test_loader, train_dataset.classes


def create_model(num_classes=2):
    """
    Crée un modèle ResNet18 pré-entraîné et adapté pour la classification binaire
    """
    model = models.resnet18(pretrained=True)
    
    # Geler les couches pré-entraînées (optionnel)
    for param in model.parameters():
        param.requires_grad = False
    
    # Remplacer la dernière couche pour notre tâche
    num_features = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Linear(num_features, 512),
        nn.ReLU(),
        nn.Dropout(0.3),
        nn.Linear(512, num_classes)
    )
    
    return model


def train_epoch(model, train_loader, criterion, optimizer, device):
    """
    Entraîne le modèle pour une epoch
    """
    model.train()
    running_loss = 0.0
    all_preds = []
    all_labels = []
    
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item() * inputs.size(0)
        _, preds = torch.max(outputs, 1)
        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())
    
    epoch_loss = running_loss / len(train_loader.dataset)
    epoch_acc = accuracy_score(all_labels, all_preds)
    
    return epoch_loss, epoch_acc


def validate(model, val_loader, criterion, device):
    """
    Évalue le modèle sur l'ensemble de validation
    """
    model.eval()
    running_loss = 0.0
    all_preds = []
    all_labels = []
    
    with torch.no_grad():
        for inputs, labels in val_loader:
            inputs, labels = inputs.to(device), labels.to(device)
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            running_loss += loss.item() * inputs.size(0)
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())
    
    epoch_loss = running_loss / len(val_loader.dataset)
    epoch_acc = accuracy_score(all_labels, all_preds)
    epoch_precision = precision_score(all_labels, all_preds, average='binary')
    epoch_recall = recall_score(all_labels, all_preds, average='binary')
    epoch_f1 = f1_score(all_labels, all_preds, average='binary')
    
    return epoch_loss, epoch_acc, epoch_precision, epoch_recall, epoch_f1


def train(data_dir='/opt/airflow/dags/data/chest_xray', 
          epochs=10, 
          batch_size=32, 
          learning_rate=0.001):
    """
    Fonction principale d'entraînement avec tracking MLflow
    """
    print("🚀 Démarrage de l'entraînement...")
    
    # Configuration MLflow
    mlflow.set_tracking_uri("http://mlflow:5000")
    mlflow.set_experiment("pneumonia_detection")
    
    # Détection du device (GPU si disponible)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"📱 Device utilisé: {device}")
    
    with mlflow.start_run(run_name=f"resnet18_{datetime.now().strftime('%Y%m%d_%H%M%S')}"):
        
        # Log des hyperparamètres
        mlflow.log_param("model_architecture", "ResNet18")
        mlflow.log_param("epochs", epochs)
        mlflow.log_param("batch_size", batch_size)
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("optimizer", "Adam")
        mlflow.log_param("device", str(device))
        
        # Chargement des données
        print("📊 Chargement des données...")
        train_loader, val_loader, test_loader, classes = get_data_loaders(data_dir, batch_size)
        print(f"   Classes: {classes}")
        print(f"   Train samples: {len(train_loader.dataset)}")
        print(f"   Val samples: {len(val_loader.dataset)}")
        print(f"   Test samples: {len(test_loader.dataset)}")
        
        # Création du modèle
        print("🧠 Création du modèle...")
        model = create_model(num_classes=len(classes))
        model = model.to(device)
        
        # Définition de la loss et de l'optimizer
        criterion = nn.CrossEntropyLoss()
        optimizer = optim.Adam(model.parameters(), lr=learning_rate)
        
        # Entraînement
        print(f"\n🏋️ Entraînement sur {epochs} epochs...")
        best_val_acc = 0.0
        
        for epoch in range(epochs):
            print(f"\n--- Epoch {epoch+1}/{epochs} ---")
            
            # Entraînement
            train_loss, train_acc = train_epoch(model, train_loader, criterion, optimizer, device)
            print(f"Train - Loss: {train_loss:.4f}, Acc: {train_acc:.4f}")
            
            # Validation
            val_loss, val_acc, val_precision, val_recall, val_f1 = validate(model, val_loader, criterion, device)
            print(f"Val   - Loss: {val_loss:.4f}, Acc: {val_acc:.4f}, Precision: {val_precision:.4f}, Recall: {val_recall:.4f}, F1: {val_f1:.4f}")
            
            # Log des métriques dans MLflow
            mlflow.log_metric("train_loss", train_loss, step=epoch)
            mlflow.log_metric("train_accuracy", train_acc, step=epoch)
            mlflow.log_metric("val_loss", val_loss, step=epoch)
            mlflow.log_metric("val_accuracy", val_acc, step=epoch)
            mlflow.log_metric("val_precision", val_precision, step=epoch)
            mlflow.log_metric("val_recall", val_recall, step=epoch)
            mlflow.log_metric("val_f1", val_f1, step=epoch)
            
            # Sauvegarde du meilleur modèle
            if val_acc > best_val_acc:
                best_val_acc = val_acc
                mlflow.log_metric("best_val_accuracy", best_val_acc)
        
        # Test final
        print("\n🧪 Évaluation sur le test set...")
        test_loss, test_acc, test_precision, test_recall, test_f1 = validate(model, test_loader, criterion, device)
        print(f"Test - Loss: {test_loss:.4f}, Acc: {test_acc:.4f}, Precision: {test_precision:.4f}, Recall: {test_recall:.4f}, F1: {test_f1:.4f}")
        
        mlflow.log_metric("test_loss", test_loss)
        mlflow.log_metric("test_accuracy", test_acc)
        mlflow.log_metric("test_precision", test_precision)
        mlflow.log_metric("test_recall", test_recall)
        mlflow.log_metric("test_f1", test_f1)
        
        # Sauvegarde du modèle dans MLflow
        print("\n💾 Sauvegarde du modèle dans MLflow...")
        mlflow.pytorch.log_model(model, "model")
        
        # Sauvegarde locale du modèle
        model_path = "/opt/airflow/dags/pneumonia_model.pth"
        torch.save(model.state_dict(), model_path)
        mlflow.log_artifact(model_path)
        
        print(f"\n✅ Entraînement terminé!")
        print(f"   Meilleure accuracy validation: {best_val_acc:.4f}")
        print(f"   Test accuracy: {test_acc:.4f}")
        
        return {
            'best_val_acc': best_val_acc,
            'test_acc': test_acc,
            'test_precision': test_precision,
            'test_recall': test_recall,
            'test_f1': test_f1
        }


if __name__ == "__main__":
    # Pour tester localement
    results = train()
    print(f"\n📈 Résultats finaux: {results}")

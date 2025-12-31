from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ImageUploadForm
import random

def index(request):
    """Page d'accueil"""
    return render(request, 'index.html')

def upload(request):
    """Page d'upload et prédiction"""
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Sauvegarder l'image
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            file_url = fs.url(filename)
            
            # Simulation de prédiction (sans PyTorch pour démo rapide)
            # En production, charger le vrai modèle depuis MLflow
            prediction = random.choice(['NORMAL', 'PNEUMONIA'])
            confidence = random.uniform(75, 95)
            
            probabilities = {
                'NORMAL': confidence if prediction == 'NORMAL' else 100 - confidence,
                'PNEUMONIA': confidence if prediction == 'PNEUMONIA' else 100 - confidence
            }
            
            return render(request, 'result.html', {
                'image_url': file_url,
                'prediction': prediction,
                'confidence': round(confidence, 2),
                'probabilities': probabilities,
            })
    else:
        form = ImageUploadForm()
    
    return render(request, 'upload.html', {'form': form})

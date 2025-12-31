from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(
        label='Radiographie Thoracique',
        help_text='Formats acceptés: JPG, PNG (max 5MB)',
        widget=forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'})
    )

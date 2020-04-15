from django import forms
from django.core.validators import FileExtensionValidator

class UploadFileForm(forms.Form):
    select_audio_file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])
from django.db import models
from constrainedfilefield.fields import ConstrainedFileField
from django.core.validators import FileExtensionValidator

class Song(models.Model):
    song = models.FileField(null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])



# ConstrainedFileField(
#                             null=True,
#                             blank=True,
#                             content_types=['audio/png'],
#                             max_upload_size=10240
#                                     )

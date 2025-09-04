from django.contrib import admin

from .models.photo_model import PhotoModel
from .models.file_model import FileModel

admin.site.register(PhotoModel)
admin.site.register(FileModel)

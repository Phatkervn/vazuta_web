
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
from django_mysql.models import ListCharField

from datetime import datetime, timezone








class App (models.Model):
    appTitle = models.TextField(default="")
    appName = models.CharField(default="",max_length=250)
    appThumb = models.ImageField(upload_to=f'img/app/')
    appLogo  = models.ImageField(upload_to=f'img/app/')
    appType = ListCharField(
        base_field = models.CharField(max_length=50),
        size= 6,
        max_length=(6 * 51)
    )
    appVersion = models.CharField(max_length=100,default="")
    appPublisher = models.CharField(max_length=100,default="")
    appCapacity = models.CharField(max_length=20,default="")
    appsystem = models.CharField(max_length=100,default="")
    appDownload = ListCharField(
        base_field = models.CharField(max_length=600),
        size= 2,
        max_length= 2*601
    )
    appTimeUpload =  models.DateTimeField(auto_now_add=True)
    appContent = RichTextField(default="")
    
    def __str__(self) -> str:
        return self.appName


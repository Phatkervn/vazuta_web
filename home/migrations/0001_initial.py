# Generated by Django 4.0.5 on 2022-07-31 07:59

import ckeditor.fields
from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appTitle', models.TextField(default='')),
                ('appName', models.CharField(default='', max_length=250)),
                ('appThumb', models.ImageField(upload_to='img/app/')),
                ('appLogo', models.ImageField(upload_to='img/app/')),
                ('appType', django_mysql.models.ListCharField(models.CharField(max_length=50), max_length=306, size=6)),
                ('appVersion', models.CharField(default='', max_length=100)),
                ('appPublisher', models.CharField(default='', max_length=100)),
                ('appCapacity', models.CharField(default='', max_length=20)),
                ('appsystem', models.CharField(default='', max_length=100)),
                ('appDownload', django_mysql.models.ListCharField(models.CharField(max_length=600), max_length=1202, size=2)),
                ('appTimeUpload', models.DateTimeField(auto_now_add=True)),
                ('appContent', ckeditor.fields.RichTextField(default='')),
            ],
        ),
    ]
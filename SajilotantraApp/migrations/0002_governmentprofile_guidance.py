# Generated by Django 4.2.7 on 2023-12-14 03:12

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SajilotantraApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GovernmentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Guidance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField()),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]

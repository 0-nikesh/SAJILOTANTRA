# Generated by Django 4.2.7 on 2024-01-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SajilotantraApp', '0013_post_comment_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('reason', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='forget_password_token',
            field=models.CharField(default='', max_length=100),
        ),
    ]

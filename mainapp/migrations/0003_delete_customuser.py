# Generated by Django 5.2 on 2025-05-16 02:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_resume_user_customuser_delete_analysisresult_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

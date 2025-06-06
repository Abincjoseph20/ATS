# Generated by Django 5.0.6 on 2025-05-15 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='address',
            field=models.TextField(default='Not Provided'),
        ),
        migrations.AddField(
            model_name='resume',
            name='ats_score',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='resume',
            name='job_role',
            field=models.CharField(default='Not Specified', max_length=255),
        ),
        migrations.AddField(
            model_name='resume',
            name='matched_keywords',
            field=models.TextField(default='Not Specified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='name',
            field=models.CharField(default='Not Specified', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='qualification',
            field=models.CharField(choices=[('10th', '10th'), ('12th', '12th'), ('Diploma', 'Diploma'), ('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('MBA', 'Master of Business Administration'), ('MCA', 'Master of Computer Applications'), ('PhD', 'Doctor of Philosophy'), ('BTech', 'Bachelor of Technology'), ('MTech', 'Master of Technology'), ('BSc', 'Bachelor of Science'), ('MSc', 'Master of Science'), ('BA', 'Bachelor of Arts'), ('MA', 'Master of Arts'), ('BCom', 'Bachelor of Commerce'), ('MCom', 'Master of Commerce'), ('LLB', 'Bachelor of Laws'), ('LLM', 'Master of Laws'), ('BBA', 'Bachelor of Business Administration'), ('BCA', 'Bachelor of Computer Applications')], default='10th', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='raw_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]

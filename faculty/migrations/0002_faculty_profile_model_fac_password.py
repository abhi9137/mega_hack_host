# Generated by Django 3.0.2 on 2020-01-29 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty_profile_model',
            name='fac_password',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
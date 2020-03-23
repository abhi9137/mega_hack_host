# Generated by Django 3.0.2 on 2020-01-29 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_profile_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fac_id', models.DecimalField(decimal_places=0, max_digits=10, unique=True)),
                ('fac_name', models.CharField(max_length=100)),
                ('fac_course', models.CharField(max_length=60)),
                ('fac_qaulification', models.CharField(max_length=60)),
                ('fac_department', models.CharField(max_length=60)),
                ('fac_designation', models.CharField(max_length=60)),
                ('fac_email', models.EmailField(max_length=200)),
                ('fac_date_of_joining', models.DateField()),
            ],
        ),
    ]

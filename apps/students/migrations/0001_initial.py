# Generated by Django 5.0.2 on 2024-03-13 14:59

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentBulkUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_upload', models.DateTimeField(auto_now=True)),
                ('csv_file', models.FileField(upload_to='students/bulkupload/')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10)),
                ('registration_number', models.CharField(max_length=200, unique=True)),
                ('surname', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('other_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('date_of_birth', models.DateField(default=django.utils.timezone.now)),
                ('date_of_admission', models.DateField(default=django.utils.timezone.now)),
                ('parent_mobile_number', models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')])),
                ('address', models.CharField(blank=True)),
                ('others', models.TextField(blank=True)),
                ('passport', models.ImageField(blank=True, upload_to='students/passports/')),
                ('current_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='coreapp.studentclass')),
            ],
        ),
    ]

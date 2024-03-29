# Generated by Django 5.0.2 on 2024-03-13 14:59

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
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.IntegerField()),
                ('date_paid', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_from_previous_term', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'inactive')], default='active', max_length=20)),
                ('class_for', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.studentclass')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coreapp.academicsession')),
            ],
            options={
                'ordering': ['student', 'term'],
            },
        ),
    ]

# Generated by Django 4.1.4 on 2023-03-02 16:26

import Incident_Management.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Incident_ID', models.CharField(default=Incident_Management.models.incident_char, max_length=12)),
                ('Incident_Detail', models.TextField(max_length=500)),
                ('Incident_DT', models.DateTimeField(auto_now=True)),
                ('Incident_Priority', models.CharField(choices=[('High', 'High'), ('Medium', 'Medium'), ('Low', 'Low')], max_length=50, null=True)),
                ('Incident_Status', models.CharField(choices=[('Open', 'Open'), ('In progress', 'In progress'), ('Closed', 'Closed')], max_length=50, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

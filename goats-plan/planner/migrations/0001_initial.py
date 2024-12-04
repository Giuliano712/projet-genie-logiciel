# Generated by Django 4.2.16 on 2024-12-04 03:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientCompany',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('etat', models.CharField(choices=[('TO DO', 'TO DO'), ('DOING', 'DOING'), ('DONE', 'DONE')], default='TO DO', max_length=100)),
                ('importance', models.CharField(choices=[('Basse', 'Basse'), ('Moyenne', 'Moyenne'), ('Haute', 'Haute')], default='Moyenne', max_length=100)),
                ('deadline', models.CharField(max_length=100)),
            ],
        ),
    ]
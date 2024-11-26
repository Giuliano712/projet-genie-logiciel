# Generated by Django 5.1.3 on 2024-11-19 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Planifieur', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tache',
            name='etat',
            field=models.CharField(choices=[('TO DO', 'TO DO'), ('DOING', 'DOING'), ('DONE', 'DONE')], default='TO DO', max_length=100),
        ),
        migrations.AlterField(
            model_name='tache',
            name='importance',
            field=models.CharField(choices=[('Basse', 'Basse'), ('Moyenne', 'Moyenne'), ('Haute', 'Haute')], default='Moyenne', max_length=100),
        ),
    ]
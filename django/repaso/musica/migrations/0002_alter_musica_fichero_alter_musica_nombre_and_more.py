# Generated by Django 5.0.2 on 2024-05-04 16:18

import musica.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='fichero',
            field=models.FileField(upload_to='musica/media/archivos_mp3', validators=[musica.models.validar_mp3]),
        ),
        migrations.AlterField(
            model_name='musica',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='musica',
            name='tipo_musica',
            field=models.CharField(choices=[('Rock', 'ROCK'), ('Pop', 'POP'), ('Jazz', 'JAZZ'), ('Electrónica', 'ELECTRÓNICA'), ('Clasica', 'CLÁSICA')], max_length=20),
        ),
    ]
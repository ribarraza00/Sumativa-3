# Generated by Django 4.2 on 2023-05-08 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_contacto_alter_personas_apellido_per_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='Consulta',
            field=models.IntegerField(choices=[[0, 'Consulta'], [0, 'Reclamo'], [0, 'Sugerencias'], [0, 'Felicitaciones']]),
        ),
    ]
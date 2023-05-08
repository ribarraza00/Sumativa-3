# Generated by Django 4.2 on 2023-05-08 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_profecion_alter_personas_apellido_per_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomContacto', models.CharField(max_length=50, verbose_name='Nombre ')),
                ('apeContacto', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('correoContacto', models.EmailField(max_length=30, verbose_name='Correo')),
                ('Consulta', models.IntegerField(max_length=20, verbose_name='Tipo de consulta')),
                ('mensaje', models.TextField(max_length=300, verbose_name='Mensaje')),
                ('avisos', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='personas',
            name='apellido_per',
            field=models.CharField(max_length=30, verbose_name='Primer apellido'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='correo_per',
            field=models.EmailField(max_length=30, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='id_per',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Rut usuario'),
        ),
        migrations.AlterField(
            model_name='personas',
            name='nombre_per',
            field=models.CharField(max_length=50, verbose_name='Primer nombre'),
        ),
    ]
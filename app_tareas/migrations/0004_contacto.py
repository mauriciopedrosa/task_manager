# Generated by Django 4.1 on 2022-09-04 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_tareas', '0003_alter_tarea_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('correo', models.EmailField(max_length=254)),
                ('tipo_consulta', models.IntegerField(choices=[[0, 'consulta'], [1, 'reclamo'], [2, 'sugerencia']])),
                ('mensaje', models.TextField()),
            ],
        ),
    ]

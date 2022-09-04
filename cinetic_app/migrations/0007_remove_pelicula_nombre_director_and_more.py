# Generated by Django 4.1 on 2022-09-03 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinetic_app', '0006_rename_id_funcion_boleta_funcion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelicula',
            name='nombre_director',
        ),
        migrations.RemoveField(
            model_name='sala',
            name='capacidad',
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='clasificacion',
            field=models.CharField(choices=[('A', 'Infantil'), ('AA', 'Todo publico'), ('B', 'Mayores de 12'), ('B15', 'Mayores de 15'), ('C', 'Mayores de 18'), ('D', 'Con contenido explicito')], default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(choices=[('ACC', 'Accion'), ('AVR', 'Aventuras'), ('CFN', 'Ciencia ficcion'), ('COM', 'Comedia'), ('RMT', 'Romantica'), ('DRM', 'Drama'), ('TRR', 'Terror')], default='ACC', max_length=3),
        ),
        migrations.AlterField(
            model_name='sala',
            name='tipo_sala',
            field=models.CharField(choices=[('2D', '2D'), ('3D', '3D')], default='2D', max_length=2),
        ),
    ]
# Generated by Django 4.1 on 2022-09-03 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinetic_app', '0009_alter_listaventaproducto_combo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boleta',
            old_name='vende_boletas',
            new_name='venta_boleta',
        ),
    ]

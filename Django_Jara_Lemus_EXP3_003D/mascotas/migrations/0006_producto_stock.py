# Generated by Django 4.2.2 on 2023-07-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0005_alter_producto_idproducto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.IntegerField(blank=True, null=True, verbose_name='Precio'),
        ),
    ]
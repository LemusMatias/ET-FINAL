# Generated by Django 4.2.1 on 2023-06-12 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(blank=True, max_length=50, verbose_name='Nombre de categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idproducto', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='ID Producto')),
                ('nombre', models.CharField(blank=True, max_length=100, verbose_name='Nombre')),
                ('modelo', models.CharField(blank=True, max_length=100, verbose_name='Modelo')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mascotas.categoria', verbose_name='Categoria')),
            ],
        ),
    ]
# Generated by Django 4.1.13 on 2023-11-06 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_oferta_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Oferta',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredientes', '0001_initial'),
        ('hamburguesas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hamburguesa',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='ingredientes.Ingrediente'),
        ),
    ]

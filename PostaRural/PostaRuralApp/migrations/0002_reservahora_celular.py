# Generated by Django 3.2.4 on 2021-06-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PostaRuralApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservahora',
            name='celular',
            field=models.CharField(default='Sin Celular', max_length=300, verbose_name='Celular'),
        ),
    ]

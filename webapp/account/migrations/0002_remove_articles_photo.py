# Generated by Django 4.0.4 on 2022-05-20 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='photo',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-05 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pirates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tesouro',
            name='img_tesouro',
        ),
    ]

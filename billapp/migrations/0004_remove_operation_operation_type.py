# Generated by Django 3.2.7 on 2021-10-02 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0003_auto_20211002_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='operation_type',
        ),
    ]

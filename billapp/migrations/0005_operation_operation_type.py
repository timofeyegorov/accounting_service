# Generated by Django 3.2.7 on 2021-10-02 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0004_remove_operation_operation_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='operation_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='billapp.operationtype'),
        ),
    ]

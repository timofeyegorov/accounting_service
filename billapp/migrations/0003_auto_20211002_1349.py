# Generated by Django 3.2.7 on 2021-10-02 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0002_rename_operatinontag_operationtag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operationtag',
            old_name='operation_tag',
            new_name='tag_name',
        ),
        migrations.RenameField(
            model_name='operationtype',
            old_name='operation_type',
            new_name='type_name',
        ),
        migrations.AddField(
            model_name='operationtag',
            name='type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='billapp.operationtype'),
        ),
    ]

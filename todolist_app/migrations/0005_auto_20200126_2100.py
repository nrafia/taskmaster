# Generated by Django 3.0.2 on 2020-01-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0004_auto_20200125_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='date_created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='tasklist',
            name='date_modified',
            field=models.DateTimeField(),
        ),
    ]

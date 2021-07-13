# Generated by Django 3.2.4 on 2021-06-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0003_auto_20210616_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.TextField(default='Not Started'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(default='2021-06-29'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default='2021-06-29'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-29 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0004_auto_20210629_2231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.ForeignKey(default='Not Started', on_delete=django.db.models.deletion.CASCADE, to='todolist.status'),
        ),
    ]

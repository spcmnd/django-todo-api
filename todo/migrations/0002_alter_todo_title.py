# Generated by Django 4.1.1 on 2022-09-12 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
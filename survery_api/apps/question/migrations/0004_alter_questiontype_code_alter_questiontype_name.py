# Generated by Django 4.2.6 on 2023-10-24 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_insert_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiontype',
            name='code',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='questiontype',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
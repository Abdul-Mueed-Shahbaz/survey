# Generated by Django 4.2.6 on 2023-10-21 16:02

import apps.question.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('update_on', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('option_text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'question_option',
            },
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('update_on', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'question_type',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('update_on', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=apps.question.models.image_upload)),
                ('statement', models.TextField()),
                ('response_text', models.TextField(blank=True, null=True)),
                ('options', models.ManyToManyField(blank=True, to='question.questionoption')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.questiontype')),
            ],
            options={
                'db_table': 'question',
            },
        ),
    ]

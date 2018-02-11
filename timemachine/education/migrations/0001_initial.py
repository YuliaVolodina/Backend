# Generated by Django 2.0.2 on 2018-02-11 03:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('programming_language', models.CharField(max_length=100, verbose_name='programming language')),
                ('level', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='level')),
                ('description', models.TextField(verbose_name='description')),
                ('solution', models.TextField(verbose_name='solution')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]

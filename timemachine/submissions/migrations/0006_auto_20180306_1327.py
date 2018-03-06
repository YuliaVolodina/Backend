# Generated by Django 2.0.2 on 2018-03-06 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_job_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='solution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='restapi.Solution'),
        ),
        migrations.AlterField(
            model_name='job',
            name='testcase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='restapi.TestCase'),
        ),
    ]

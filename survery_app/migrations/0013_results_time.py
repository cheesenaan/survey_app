# Generated by Django 4.0.6 on 2022-09-02 13:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('survery_app', '0012_remove_results_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='time',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]

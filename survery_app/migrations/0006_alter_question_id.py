# Generated by Django 4.0.6 on 2022-08-25 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survery_app', '0005_tally_alter_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
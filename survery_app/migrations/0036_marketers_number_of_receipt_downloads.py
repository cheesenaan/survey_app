# Generated by Django 4.0.6 on 2023-03-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survery_app', '0035_marketers_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketers',
            name='number_of_receipt_downloads',
            field=models.BigIntegerField(default=0),
        ),
    ]

# Generated by Django 4.0.6 on 2022-10-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survery_app', '0027_remove_coupon_attempts_after_expiry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='attempts_after_expiry',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='attempts_after_limit',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
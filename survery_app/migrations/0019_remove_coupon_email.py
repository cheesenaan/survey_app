# Generated by Django 4.0.6 on 2022-10-09 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survery_app', '0018_coupon_report_purchase_successful_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coupon',
            name='email',
        ),
    ]

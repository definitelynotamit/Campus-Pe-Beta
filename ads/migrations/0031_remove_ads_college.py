# Generated by Django 4.0.10 on 2023-03-24 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0030_remove_ads_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='college',
        ),
    ]
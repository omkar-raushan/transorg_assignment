# Generated by Django 2.2.2 on 2021-12-23 07:58

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default="profile_image.png", max_length=255, null=True),
        ),
    ]

# Generated by Django 2.2.2 on 2021-12-23 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20211223_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='profile_image',
            field=models.ImageField(blank=True, default='/profile_image.png', max_length=255, null=True, upload_to=''),
        ),
    ]

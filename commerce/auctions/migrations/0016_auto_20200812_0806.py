# Generated by Django 3.1 on 2020-08-12 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0015_auto_20200812_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, default='images', null=True, upload_to='images'),
        ),
    ]
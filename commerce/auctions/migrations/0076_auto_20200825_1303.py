# Generated by Django 3.1 on 2020-08-25 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0075_auto_20200825_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='title',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='listing_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
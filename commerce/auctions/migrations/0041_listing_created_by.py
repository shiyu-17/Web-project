# Generated by Django 3.1 on 2020-08-21 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0040_remove_listing_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='created_by',
            field=models.CharField(default='Billy', max_length=100),
            preserve_default=False,
        ),
    ]
# Generated by Django 3.1 on 2020-08-24 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0066_auto_20200824_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='listing',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.listing'),
        ),
    ]

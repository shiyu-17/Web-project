# Generated by Django 3.1 on 2020-09-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0100_auto_20200904_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[(3, 'GOLD'), (4, 'SILVER'), (5, 'BRONZE')], max_length=64, null=True),
        ),
    ]
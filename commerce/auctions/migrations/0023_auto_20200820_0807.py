# Generated by Django 3.1 on 2020-08-20 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0022_auto_20200817_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
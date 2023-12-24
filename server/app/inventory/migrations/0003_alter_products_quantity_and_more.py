# Generated by Django 5.0 on 2023-12-23 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_products_track_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='track_inventory',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]

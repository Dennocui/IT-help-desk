# Generated by Django 3.2 on 2022-08-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_remove_asset_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='item_name',
            field=models.CharField(max_length=30, null=True, verbose_name='Item Name'),
        ),
    ]
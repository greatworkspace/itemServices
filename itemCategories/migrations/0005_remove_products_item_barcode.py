# Generated by Django 3.2.6 on 2023-02-02 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemCategories', '0004_alter_products_item_barcode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='item_barcode',
        ),
    ]

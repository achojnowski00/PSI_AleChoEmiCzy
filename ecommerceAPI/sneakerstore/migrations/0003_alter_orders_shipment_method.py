# Generated by Django 4.0.1 on 2022-01-11 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerstore', '0002_shipment_alter_clients_options_alter_orders_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='shipment_method',
            field=models.CharField(max_length=20),
        ),
    ]

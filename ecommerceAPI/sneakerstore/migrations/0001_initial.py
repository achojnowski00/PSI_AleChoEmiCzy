# Generated by Django 4.0.1 on 2022-01-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id_type', models.AutoField(primary_key=True, serialize=False)),
                ('name_type', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Sneakers',
            fields=[
                ('id_sneakers', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('brand_name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('color_way', models.CharField(max_length=45)),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sneakers', to='sneakerstore.type')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id_order', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('purchase_date', models.DateTimeField()),
                ('payment_method', models.CharField(max_length=20)),
                ('payment_date', models.DateTimeField()),
                ('shipment_method', models.CharField(max_length=20)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='sneakerstore.clients')),
                ('id_sneakers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='sneakerstore.sneakers')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-24 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='productsmodel',
            name='categories',
            field=models.ManyToManyField(to='products.productscategorymodel'),
        ),
    ]

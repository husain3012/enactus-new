# Generated by Django 3.1.2 on 2020-11-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_order_transaction_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Lights', 'lights'), ('TableTops', 'tabletops')], default='', max_length=50),
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-20 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='costumer',
            name='address',
            field=models.CharField(max_length=560, null=True),
        ),
        migrations.AddField(
            model_name='costumer',
            name='city',
            field=models.CharField(max_length=560, null=True),
        ),
        migrations.AddField(
            model_name='costumer',
            name='state',
            field=models.CharField(max_length=560, null=True),
        ),
        migrations.AddField(
            model_name='costumer',
            name='zipcode',
            field=models.CharField(max_length=560, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(max_length=560, null=True),
        ),
        migrations.CreateModel(
            name='Order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=0)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
    ]

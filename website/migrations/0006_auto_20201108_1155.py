# Generated by Django 3.1.2 on 2020-11-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20201108_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image1',
            field=models.ImageField(blank=True, default='bg.jpg', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='image2',
            field=models.ImageField(blank=True, default='bg.jpg', upload_to=''),
            preserve_default=False,
        ),
    ]

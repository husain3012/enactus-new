# Generated by Django 3.1.2 on 2020-11-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201108_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='by',
            field=models.CharField(max_length=560, null=True),
        ),
    ]

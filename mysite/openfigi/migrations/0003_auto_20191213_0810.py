# Generated by Django 2.2 on 2019-12-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openfigi', '0002_auto_20191213_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cusip',
            name='timeStamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='isin',
            name='timeStamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='sedol',
            name='timeStamp',
            field=models.DateTimeField(),
        ),
    ]

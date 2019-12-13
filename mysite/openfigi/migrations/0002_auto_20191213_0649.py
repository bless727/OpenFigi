# Generated by Django 2.2 on 2019-12-13 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openfigi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cusip',
            name='exchCode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cusip',
            name='marketSector',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cusip',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cusip',
            name='securityType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cusip',
            name='ticker',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='isin',
            name='exchCode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='isin',
            name='marketSector',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='isin',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='isin',
            name='securityType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='isin',
            name='ticker',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sedol',
            name='exchCode',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sedol',
            name='marketSector',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sedol',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sedol',
            name='securityType',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='sedol',
            name='ticker',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

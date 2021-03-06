# Generated by Django 3.2.6 on 2022-01-16 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0006_auto_20220116_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='county',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='hostName',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='guest',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]

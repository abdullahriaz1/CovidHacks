# Generated by Django 3.2.6 on 2022-01-16 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covidapp', '0005_alter_guest_phonenumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='county',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='hostEmail',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='event',
            name='hostName',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='hostPhoneNumber',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='numVaccinesRequired',
            field=models.BigIntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='event',
            name='state',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='guest',
            name='vaccinationNum',
            field=models.BigIntegerField(default=0),
        ),
    ]
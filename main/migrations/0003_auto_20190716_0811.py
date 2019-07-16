# Generated by Django 2.2.3 on 2019-07-16 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_setup_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='cellmodel',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='component',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='compoundunit',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='encapsulation',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='math',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='reset',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='unit',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='variable',
            name='privacy',
            field=models.IntegerField(default=0),
        ),
    ]
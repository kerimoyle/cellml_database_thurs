# Generated by Django 2.2.4 on 2019-08-15 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_setup_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellmodel',
            name='ready',
        ),
        migrations.RemoveField(
            model_name='component',
            name='ready',
        ),
        migrations.RemoveField(
            model_name='compoundunit',
            name='ready',
        ),
        migrations.RemoveField(
            model_name='encapsulation',
            name='ready',
        ),
        migrations.RemoveField(
            model_name='math',
            name='ready',
        ),
        migrations.RemoveField(
            model_name='reset',
            name='ready',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='ready',
        ),
        migrations.RemoveField(
            model_name='variable',
            name='ready',
        ),
        migrations.AlterField(
            model_name='reset',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 2.2.4 on 2019-10-02 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190923_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='math',
            name='variables',
            field=models.ManyToManyField(blank=True, null=True, related_name='maths', to='main.Variable'),
        ),
    ]

# Generated by Django 2.2.4 on 2019-09-18 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190918_1424'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='parent_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_components', to='main.CellModel'),
        ),
    ]

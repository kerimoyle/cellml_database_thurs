# Generated by Django 2.2.3 on 2019-07-11 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_setup_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='temporarystorage',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stored_files', to='main.Person'),
        ),
    ]
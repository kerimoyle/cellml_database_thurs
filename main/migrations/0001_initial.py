# Generated by Django 2.2.3 on 2019-07-16 12:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CellModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('uploaded_from', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompoundUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_standard', models.BooleanField(default=False)),
                ('symbol', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImportedEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_type', models.CharField(blank=True, max_length=100, null=True)),
                ('source_reference', models.URLField(blank=True, null=True)),
                ('source_id', models.IntegerField(blank=True, default=-1, null=True)),
                ('attribution', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('math_ml', models.TextField(blank=True)),
                ('components', models.ManyToManyField(blank=True, related_name='maths', to='main.Component')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_math_objects', to='main.ImportedEntity')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Variable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('initial_value', models.CharField(max_length=100, null=True)),
                ('interface_type', models.CharField(blank=True, choices=[('Public', 'PU'), ('Private', 'PR'), ('Public and private', 'PP'), ('None', 'NA')], default='NA', max_length=2, null=True)),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variables', to='main.Component')),
                ('equivalent_variables', models.ManyToManyField(blank=True, related_name='_variable_equivalent_variables_+', to='main.Variable')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_variable_objects', to='main.ImportedEntity')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('multiplier', models.IntegerField(default=1, null=True)),
                ('exponent', models.IntegerField(default=1, null=True)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('child_cu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part_of', to='main.CompoundUnit')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_unit_objects', to='main.ImportedEntity')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person')),
                ('parent_cu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='product_of', to='main.CompoundUnit')),
                ('prefix', models.ForeignKey(default=main.models.get_default_prefix, on_delete=main.models.get_default_prefix, to='main.Prefix')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TemporaryStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('tree', models.TextField(blank=True)),
                ('model_name', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stored_files', to='main.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Reset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('order', models.IntegerField(default=0)),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resets', to='main.Component')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_reset_objects', to='main.ImportedEntity')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person')),
                ('reset_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reset_values', to='main.Math')),
                ('test_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_values', to='main.Math')),
                ('test_variable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reset_test_variables', to='main.Variable')),
                ('variable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reset_variables', to='main.Variable')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='math',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person'),
        ),
        migrations.CreateModel(
            name='Encapsulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ready', models.NullBooleanField()),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='Only me', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_encapsulation_objects', to='main.ImportedEntity')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='compoundunit',
            name='imported_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_compoundunit_objects', to='main.ImportedEntity'),
        ),
        migrations.AddField(
            model_name='compoundunit',
            name='models',
            field=models.ManyToManyField(blank=True, related_name='compoundunits', to='main.CellModel'),
        ),
        migrations.AddField(
            model_name='compoundunit',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person'),
        ),
        migrations.AddField(
            model_name='compoundunit',
            name='variables',
            field=models.ManyToManyField(blank=True, related_name='compoundunits', to='main.Variable'),
        ),
        migrations.AddField(
            model_name='component',
            name='imported_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_component_objects', to='main.ImportedEntity'),
        ),
        migrations.AddField(
            model_name='component',
            name='models',
            field=models.ManyToManyField(blank=True, related_name='components', to='main.CellModel'),
        ),
        migrations.AddField(
            model_name='component',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person'),
        ),
        migrations.AddField(
            model_name='cellmodel',
            name='imported_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='imported_cellmodel_objects', to='main.ImportedEntity'),
        ),
        migrations.AddField(
            model_name='cellmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person'),
        ),
    ]

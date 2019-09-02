# Generated by Django 2.2.4 on 2019-08-15 14:02

from django.conf import settings
import django.contrib.postgres.fields
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
            name='Annotation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=100, null=True)),
                ('source', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CellMLSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True, null=True)),
                ('code', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CellModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('uploaded_from', models.CharField(blank=True, max_length=250, null=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_cellmodel_objects', to='main.Annotation')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.CellModel')),
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
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_component_objects', to='main.Annotation')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.Component')),
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
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('is_standard', models.BooleanField(default=False)),
                ('symbol', models.CharField(blank=True, max_length=100, null=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_compoundunit_objects', to='main.Annotation')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.CompoundUnit')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ItemError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hints', models.TextField(blank=True)),
                ('spec', models.CharField(blank=True, max_length=25, null=True)),
                ('fields', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Math',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('math_ml', models.TextField(blank=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_math_objects', to='main.Annotation')),
                ('components', models.ManyToManyField(blank=True, related_name='maths', to='main.Component')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.Math')),
                ('errors', models.ManyToManyField(blank=True, related_name='error_in_math_objects', to='main.ItemError')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.Math')),
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
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('initial_value_constant', models.FloatField(blank=True, null=True)),
                ('interface_type', models.CharField(blank=True, choices=[('Public', 'PU'), ('Private', 'PR'), ('Public and private', 'PP'), ('None', 'NA')], default='NA', max_length=2, null=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_variable_objects', to='main.Annotation')),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='variables', to='main.Component')),
                ('compoundunit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='variables', to='main.CompoundUnit')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.Variable')),
                ('equivalent_variables', models.ManyToManyField(blank=True, related_name='_variable_equivalent_variables_+', to='main.Variable')),
                ('errors', models.ManyToManyField(blank=True, related_name='error_in_variable_objects', to='main.ItemError')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.Variable')),
                ('initial_value_variable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='will_initialise', to='main.Variable')),
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
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('multiplier', models.FloatField(default=1.0, null=True)),
                ('exponent', models.IntegerField(default=1, null=True)),
                ('reference', models.CharField(blank=True, max_length=100, null=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_unit_objects', to='main.Annotation')),
                ('child_cu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='part_of', to='main.CompoundUnit')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.Unit')),
                ('errors', models.ManyToManyField(blank=True, related_name='error_in_unit_objects', to='main.ItemError')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.Unit')),
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
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('order', models.IntegerField(blank=True, null=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_reset_objects', to='main.Annotation')),
                ('component', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resets', to='main.Component')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.Reset')),
                ('errors', models.ManyToManyField(blank=True, related_name='error_in_reset_objects', to='main.ItemError')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.Reset')),
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
                ('privacy', models.CharField(blank=True, choices=[('Public', 'Public'), ('Private', 'Private')], default='private', max_length=9, null=True)),
                ('notes', models.TextField(blank=True)),
                ('cellml_id', models.CharField(blank=True, max_length=100)),
                ('cellml_index', models.IntegerField(default=-1, null=True)),
                ('is_valid', models.NullBooleanField()),
                ('last_checked', models.DateTimeField(blank=True, null=True)),
                ('annotations', models.ManyToManyField(blank=True, related_name='used_by_encapsulation_objects', to='main.Annotation')),
                ('depends_on', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='used_by', to='main.Encapsulation')),
                ('errors', models.ManyToManyField(blank=True, related_name='error_in_encapsulation_objects', to='main.ItemError')),
                ('imported_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.Encapsulation')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='compoundunit',
            name='errors',
            field=models.ManyToManyField(blank=True, related_name='error_in_compoundunit_objects', to='main.ItemError'),
        ),
        migrations.AddField(
            model_name='compoundunit',
            name='imported_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.CompoundUnit'),
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
            model_name='component',
            name='errors',
            field=models.ManyToManyField(blank=True, related_name='error_in_component_objects', to='main.ItemError'),
        ),
        migrations.AddField(
            model_name='component',
            name='imported_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.Component'),
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
            name='errors',
            field=models.ManyToManyField(blank=True, related_name='error_in_cellmodel_objects', to='main.ItemError'),
        ),
        migrations.AddField(
            model_name='cellmodel',
            name='imported_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='imported_to', to='main.CellModel'),
        ),
        migrations.AddField(
            model_name='cellmodel',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Person'),
        ),
    ]

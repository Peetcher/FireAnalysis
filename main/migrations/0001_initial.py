# Generated by Django 3.2.25 on 2024-06-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AirDivisions',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('region', models.IntegerField(blank=True, null=True)),
                ('latitude_min', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('latitude_max', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('longitude_min', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('longitude_max', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('monitoring_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('division_head', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'air_divisions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicationZones',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('short_caption', models.TextField(blank=True, null=True)),
                ('large_threshold', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'application_zones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetectionWays',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('short_caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detection_ways',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DivisionalForestries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('caption', models.TextField(blank=True, null=True)),
                ('municipality', models.IntegerField(blank=True, null=True)),
                ('forestry', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'divisional_forestries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FireCauses',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('short_caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fire_causes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FireExtinguisher',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('tech', models.SmallIntegerField(blank=True, null=True)),
                ('short_caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fire_extinguisher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FireKinds',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('short_caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fire_kinds',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fires',
            fields=[
                ('number', models.TextField(primary_key=True, serialize=False)),
                ('number_2', models.SmallIntegerField(blank=True, null=True)),
                ('datedok', models.DateField(blank=True, null=True)),
                ('divisional_forestry', models.SmallIntegerField(blank=True, null=True)),
                ('quart_number_1', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('quart_number_2', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('quart_number_3', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('detection_datetime', models.DateField(blank=True, null=True)),
                ('detection_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('forest_manager_1', models.SmallIntegerField(blank=True, null=True)),
                ('forest_manager_2', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fires',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FiresDinamics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fire_date', models.DateField(blank=True, null=True)),
                ('datedok', models.DateField(blank=True, null=True)),
                ('delivered_aps_af', models.IntegerField(blank=True, null=True)),
                ('delivered_leaser_af', models.IntegerField(blank=True, null=True)),
                ('delivered_forestguard_af', models.IntegerField(blank=True, null=True)),
                ('delivered_attracted_af', models.IntegerField(blank=True, null=True)),
                ('delivered_mchs_af', models.IntegerField(blank=True, null=True)),
                ('delivered_cargo_af', models.IntegerField(blank=True, null=True)),
                ('delivered_aps_land', models.IntegerField(blank=True, null=True)),
                ('delivered_leaser_land', models.IntegerField(blank=True, null=True)),
                ('delivered_forestguard_land', models.IntegerField(blank=True, null=True)),
                ('delivered_attracted_land', models.IntegerField(blank=True, null=True)),
                ('delivered_mchs_land', models.IntegerField(blank=True, null=True)),
                ('delivered_cargo_land', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('delivered_leaser_hardware', models.IntegerField(blank=True, null=True)),
                ('working_aps', models.IntegerField(blank=True, null=True)),
                ('working_forestguard', models.IntegerField(blank=True, null=True)),
                ('working_attracted', models.IntegerField(blank=True, null=True)),
                ('working_leaser', models.IntegerField(blank=True, null=True)),
                ('working_mchs', models.IntegerField(blank=True, null=True)),
                ('liquidation_date', models.DateField(blank=True, null=True)),
                ('forest_wreathed_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('crowning_fire_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('underground_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('forest_notwreathed_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('nonforest_area', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('large_fire_number', models.IntegerField(blank=True, null=True)),
                ('large_fire_date', models.DateField(blank=True, null=True)),
                ('town', models.TextField(blank=True, null=True)),
                ('azimuth', models.IntegerField(blank=True, null=True)),
                ('town_distance', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'fires_dinamics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FireStates',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('short_caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'fire_states',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ForestManagers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField()),
                ('caption', models.TextField(blank=True, null=True)),
                ('forestry', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'forest_managers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Forestries',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('air_division', models.IntegerField(blank=True, null=True)),
                ('latitude_min', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('latitude_max', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('longitude_min', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
                ('longitude_max', models.DecimalField(blank=True, decimal_places=65535, max_digits=65535, null=True)),
            ],
            options={
                'db_table': 'forestries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipalities',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'municipalities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('caption', models.TextField(blank=True, null=True)),
                ('short_caption', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'regions',
                'managed': False,
            },
        ),
    ]

from django.db import models


class AirDivisions(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    region = models.IntegerField(blank=True, null=True)
    latitude_min = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    latitude_max = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    longitude_min = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    longitude_max = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    monitoring_area = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    division_head = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'air_divisions'


class ApplicationZones(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    short_caption = models.TextField(blank=True, null=True)
    large_threshold = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_zones'


class Departments(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departments'


class DetectionWays(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    short_caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detection_ways'


class DivisionalForestries(models.Model):
    code = models.IntegerField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    municipality = models.IntegerField(blank=True, null=True)
    forestry = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'divisional_forestries'


class FireCauses(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    short_caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fire_causes'


class FireExtinguisher(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    tech = models.SmallIntegerField(blank=True, null=True)
    short_caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fire_extinguisher'


class FireKinds(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    short_caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fire_kinds'


class FireStates(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    short_caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fire_states'


class Fires(models.Model):
    number = models.TextField(primary_key=True)
    number_2 = models.SmallIntegerField(blank=True, null=True)
    datedok = models.DateField(blank=True, null=True)
    department = models.ForeignKey(Departments, models.DO_NOTHING, db_column='department', blank=True, null=True)
    region = models.ForeignKey('Regions', models.DO_NOTHING, db_column='region', blank=True, null=True)
    air_division = models.ForeignKey(AirDivisions, models.DO_NOTHING, db_column='air_division', blank=True, null=True)
    forestry = models.ForeignKey('Forestries', models.DO_NOTHING, db_column='forestry', blank=True, null=True)
    municipality = models.ForeignKey('Municipalities', models.DO_NOTHING, db_column='municipality', blank=True,
                                     null=True)
    divisional_forestry = models.SmallIntegerField(blank=True, null=True)
    quart_number_1 = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    quart_number_2 = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    quart_number_3 = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    application_zone = models.ForeignKey(ApplicationZones, models.DO_NOTHING, db_column='application_zone', blank=True,
                                         null=True)
    latitude = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    detection_datetime = models.DateField(blank=True, null=True)
    detection_way = models.ForeignKey(DetectionWays, models.DO_NOTHING, db_column='detection_way', blank=True,
                                      null=True)
    detection_area = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    fire_kind = models.ForeignKey(FireKinds, models.DO_NOTHING, db_column='fire_kind', blank=True, null=True)
    forest_manager_1 = models.SmallIntegerField(blank=True, null=True)
    forest_manager_2 = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fires'


class FiresDinamics(models.Model):
    fire_date = models.DateField(blank=True, null=True)
    fire_number = models.ForeignKey(Fires, models.DO_NOTHING, db_column='fire_number', blank=True, null=True)
    datedok = models.DateField(blank=True, null=True)
    cause = models.ForeignKey(FireCauses, models.DO_NOTHING, db_column='cause', blank=True, null=True)
    state = models.ForeignKey(FireStates, models.DO_NOTHING, db_column='state', blank=True, null=True)
    delivered_aps_af = models.IntegerField(blank=True, null=True)
    delivered_leaser_af = models.IntegerField(blank=True, null=True)
    delivered_forestguard_af = models.IntegerField(blank=True, null=True)
    delivered_attracted_af = models.IntegerField(blank=True, null=True)
    delivered_mchs_af = models.IntegerField(blank=True, null=True)
    delivered_cargo_af = models.IntegerField(blank=True, null=True)
    delivered_aps_land = models.IntegerField(blank=True, null=True)
    delivered_leaser_land = models.IntegerField(blank=True, null=True)
    delivered_forestguard_land = models.IntegerField(blank=True, null=True)
    delivered_attracted_land = models.IntegerField(blank=True, null=True)
    delivered_mchs_land = models.IntegerField(blank=True, null=True)
    delivered_cargo_land = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    delivered_leaser_hardware = models.IntegerField(blank=True, null=True)
    working_aps = models.IntegerField(blank=True, null=True)
    working_forestguard = models.IntegerField(blank=True, null=True)
    working_attracted = models.IntegerField(blank=True, null=True)
    working_leaser = models.IntegerField(blank=True, null=True)
    working_mchs = models.IntegerField(blank=True, null=True)
    liquidation_date = models.DateField(blank=True, null=True)
    forest_wreathed_area = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    crowning_fire_area = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    underground_area = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    forest_notwreathed_area = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    nonforest_area = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    large_fire_number = models.IntegerField(blank=True, null=True)
    large_fire_date = models.DateField(blank=True, null=True)
    town = models.TextField(blank=True, null=True)
    azimuth = models.IntegerField(blank=True, null=True)
    town_distance = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fires_dinamics'


class ForestManagers(models.Model):
    code = models.IntegerField()
    caption = models.TextField(blank=True, null=True)
    forestry = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forest_managers'


class Forestries(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    air_division = models.IntegerField(blank=True, null=True)
    latitude_min = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    latitude_max = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    longitude_min = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)
    longitude_max = models.DecimalField(max_digits=13, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'forestries'


class Municipalities(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipalities'


class Regions(models.Model):
    code = models.IntegerField(primary_key=True)
    caption = models.TextField(blank=True, null=True)
    short_caption = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regions'

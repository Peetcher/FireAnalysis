from rest_framework import serializers
from django.contrib.auth.models import User
from .models import AirDivisions, ApplicationZones, Departments, DetectionWays, DivisionalForestries, FireCauses, \
    FireExtinguisher, FireKinds, FireStates, Fires, FiresDinamics, ForestManagers, Forestries, Municipalities, Regions


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwars = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class AirDivisionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirDivisions
        fields = '__all__'


class ApplicationZonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationZones
        fields = '__all__'


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'


class DetectionWaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectionWays
        fields = '__all__'


class DivisionalForestriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DivisionalForestries
        fields = '__all__'


class FireCausesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireCauses
        fields = '__all__'


class FireExtinguisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireExtinguisher
        fields = '__all__'


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = '__all__'


class ForestriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forestries
        fields = '__all__'


class MunicipalitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipalities
        fields = '__all__'


class FireKindsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireKinds
        fields = '__all__'


class FireStatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FireStates
        fields = '__all__'


class ForestManagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForestManagers
        fields = '__all__'


class FiresSerializer(serializers.ModelSerializer):
    department = DepartmentsSerializer()
    region = RegionsSerializer()
    air_division = AirDivisionsSerializer()
    forestry = ForestriesSerializer()
    municipality = MunicipalitiesSerializer()
    application_zone = ApplicationZonesSerializer()
    detection_way = DetectionWaysSerializer()
    fire_kind = FireKindsSerializer()

    class Meta:
        model = Fires
        fields = '__all__'


class FiresDinamicsSerializer(serializers.ModelSerializer):
    fire_number = FiresSerializer()
    cause = FireCausesSerializer()
    state = FireStatesSerializer()

    class Meta:
        model = FiresDinamics
        fields = '__all__'






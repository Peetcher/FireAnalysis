from rest_framework import viewsets
from django.utils.dateparse import parse_date
from .serializers import *
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import FiresDinamicsSerializer
from .models import *


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class AirDivisionsViewSet(viewsets.ModelViewSet):
    queryset = AirDivisions.objects.all()
    serializer_class = AirDivisionsSerializer


class FiresDinamicsListView(generics.ListAPIView):
    serializer_class = FiresDinamicsSerializer

    def get_queryset(self):
        queryset = FiresDinamics.objects.all()
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)

        if start_date:
            start_date = parse_date(start_date)
        if end_date:
            end_date = parse_date(end_date)

        if start_date and end_date:
            queryset = queryset.filter(fire_date__range=(start_date, end_date))
        elif start_date:
            queryset = queryset.filter(fire_date__gte=start_date)
        elif end_date:
            queryset = queryset.filter(fire_date__lte=end_date)

        return queryset
# class ApplicationZonesViewSet(viewsets.ModelViewSet):
#     queryset = ApplicationZones.objects.all()
#     serializer_class = ApplicationZonesSerializer
#
#
# class FiresViewSet(viewsets.ModelViewSet):
#     queryset = Fires.objects.all()
#     serializer_class = FiresSerializer

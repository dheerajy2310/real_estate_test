from rest_framework import serializers
from . import models

class ApartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Apartment
        fields = '__all__'
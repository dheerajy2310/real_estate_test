from django.shortcuts import render
from . import models
from rest_framework import viewsets
from . import serializers
from django_filters.rest_framework import DjangoFilterBackend 

class ApartmentViewset(viewsets.ModelViewSet):
    queryset = models.Apartment.objects.all()
    serializer_class = serializers.ApartmentSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = '__all__'

    def get_queryset(self):
        queryset = models.Apartment.objects.all()
        price_range = self.request.query_params.get('price_range') # example: 10,000 - 15,000
        sort_by_date = self.request.query_params.get('sort_by') # example: newest first/ oldest first
        location = self.request.query_params.get('location') # example: india, USA
        selected_bedrooms = self.request.query_params.get('selected_bedrooms') # [1,2,4]
        if len(selected_bedrooms) > 0:
            queryset = queryset.filter(bedrooms__in=selected_bedrooms).all()
        elif price_range:
            min_price, max_price = price_range.remove(',').remove(' ').split('-')
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price).all()
        elif sort_by_date:
            if sort_by_date == 'newest first':
                queryset = queryset.order_by('-posted_date')
            else:
                queryset = queryset.order_by('posted_date')
        elif location:
            queryset = queryset.filter(place=location)
        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
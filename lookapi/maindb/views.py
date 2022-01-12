from django.shortcuts import render
from rest_framework import generics

from . import serializers
from .models import Ticker

# Create your views here.
class TickerList(generics.ListAPIView):
    serializer_class = serializers.TickerSerializer

    def get_queryset(self):
        search = self.request.GET.get('search')
        if search:
            return Ticker.objects.filter(ticker__iexact=search)
        
        return Ticker.objects.all()
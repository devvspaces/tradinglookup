from django.db.models import fields
from rest_framework import serializers

from .models import Ticker, Sector, Industry


class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'
    
class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'

class TickerSerializer(serializers.ModelSerializer):
    sector = SectorSerializer()
    industry = IndustrySerializer()
    class Meta:
        model = Ticker
        fields = '__all__'
from rest_framework import serializers
from .models import Listings

class ListingsSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(primary_key=True)
    # name = serializers.CharField(max_length=500)
    # host_id = serializers.IntegerField(max_length=50)
    # host_name = serializers.CharField(max_length=500, null=True)
    # neighbourhood = serializers.CharField(max_length=500)
    # latitude = serializers.FloatField(default=0)
    # longitude = serializers.FloatField(default=0)
    # room_type = serializers.CharField(max_length=500)
    # price = serializers.IntegerField(default=0)
    # minimum_nights = serializers.IntegerField(default=0)
    # number_of_reviews = serializers.FloatField(default=0)
    # calculated_host_listings_count = serializers.IntegerField(default=0)
    # availability_365 = serializers.IntegerField(default=0)

    class Meta():   
        model = Listings
        fields = ('id', 'name', 'host_id', 'host_name',
                  'neighbourhood', 'latitude', 'longitude', 
                  'room_type', 'price', 'minimum_nights', 'number_of_reviews', 
                  'calculated_host_listings_count', 'availability_365')

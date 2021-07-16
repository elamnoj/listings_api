from django.db import models

class Listings(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    host_id = models.IntegerField(max_length=50)
    host_name = models.CharField(max_length=500, null=True)
    neighbourhood = models.CharField(max_length=500)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    room_type = models.CharField(max_length=500)
    price = models.IntegerField(default=0)
    minimum_nights = models.IntegerField(default=0)
    number_of_reviews = models.FloatField(default=0)
    calculated_host_listings_count = models.IntegerField(default=0)
    availability_365 = models.IntegerField(default=0)

    def __str___(self):
        return self.neighbourhood

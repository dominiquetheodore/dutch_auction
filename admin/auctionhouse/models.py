from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User

# Create your models here.
class AuctionListing(models.Model):
    name = models.CharField(max_length=50)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    startBid = models.DecimalField(decimal_places=2, max_digits=7)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imageUrl = models.URLField(blank=True)
    active = models.BooleanField()

    def __str__(self):
        return f"{self.id} : {self.name} i \nPosted at : {self.startDate}\nValue : {self.startBid}\nDescription : {self.description}\nPosted By : {self.user.username} Active Status: {self.active}"


class Bid(models.Model):
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bidValue = models.DecimalField(decimal_places=2, max_digits=7)
    auctionListing = models.ForeignKey(
        AuctionListing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} : {self.user.username} bid {self.bidValue} on {self.auctionListing.name} at {self.date}"
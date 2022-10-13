from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Bid(models.Model):
    bid = models.IntegerField()
    user = models.ForeignKey(User,on_delete= models.CASCADE, related_name="bid")

    def __str__(self):
        return f"Bid of {self.bid} by the {self.user} "

class Auction_Listing(models.Model):
    title = models.CharField(max_length=64,blank= False)
    description = models.CharField(max_length=700)
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="auctionlistings", default=None)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, related_name="auctionbid", default=None)
    image = models.URLField(max_length=400)
    catagory = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} listing by the user {self.owner}"
from django.contrib import admin

# Register your models here.
from .models import AuctionListing, Bid

# Register your models here.
class AuctionListingAdmin(admin.ModelAdmin):
    pass
admin.site.register(AuctionListing, AuctionListingAdmin)

class BidAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bid, BidAdmin)
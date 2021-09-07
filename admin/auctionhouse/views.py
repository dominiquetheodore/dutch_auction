from django.shortcuts import get_object_or_404, render
from .models import AuctionListing, Bid

def index(request):
    auctions = AuctionListing.objects.order_by('startDate')[:5]
    context = {'auctions': auctions}
    return render(request, 'index.html', context)

def detail(request, auction_id): 
    auction = get_object_or_404(AuctionListing, pk=auction_id)
    return render(request, 'detail.html', {'auction': auction})
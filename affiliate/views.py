from django.shortcuts import render
from .models import AffiliateModel
# Create your views here.


def index(request):
    items = AffiliateModel.objects.all()
    context = {
        "items": items
    }
    for item in items:
        print(item.title)
    return render(request, 'index.html', context)

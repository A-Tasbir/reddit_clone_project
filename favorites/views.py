from django.shortcuts import render
from .models import Favorite

def favorite_list(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user)
    else:
        favorites = []
    return render(request, 'favorites/favorite_list.html', {'favorites': favorites})

from django.shortcuts import render
from .models import Tip

def tips_view(request):
    tips = Tip.objects.all()
    return render(request, 'tips/result.html', {'tips': tips})
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'quiz/home.html', {'is_authenticated': request.user.is_authenticated})
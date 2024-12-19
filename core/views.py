from django.shortcuts import render
from .models import Message

# Create your views here.


def main(request):
    return render(request, 'core/main.html')
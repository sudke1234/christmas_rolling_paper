from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

def index(request):
    return render(request, 'board/index.html')

def decoration_selected_view(request):
    return render(request, 'board/decoration_selected.html')
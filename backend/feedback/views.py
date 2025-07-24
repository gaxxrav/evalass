from django.http import JsonResponse

def ping(request):
    return JsonResponse({"status": "ok"})
from django.shortcuts import render

# Create your views here.

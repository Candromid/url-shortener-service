import json

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import Link
from .utils import generate_short_code

@csrf_exempt
def shorten_url(request):
    if request.method != "POST":
        return JsonResponse(
            {"error" : "Only POST method allowed"},
            status = 405
        )
    
    try:
        data = json.loads(request.body)
    
    except json.JSONDecodeError:
        return JsonResponse(
            {'error': 'Invalid JSON'},
            status=400
        )
    
    original_url = data.get("url")
    
    if not original_url:
        return JsonResponse(
            {'error': 'URL is required'},
            status=400
        )
        
    short_code = generate_short_code()
    
    link = Link.objects.create(
        original_url = original_url,
        short_code = short_code
    )
    
    short_url = f"http://{request.get_host()}/{link.short_code}"
    
    return JsonResponse(
        {"short_url":short_url},
        status = 201
    )
# Create your views here.

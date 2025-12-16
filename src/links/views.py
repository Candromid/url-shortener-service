import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Link
from .utils import generate_short_code

from django.shortcuts import redirect, get_object_or_404


@csrf_exempt
def shorten_url(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST allowed'}, status=405)

    data = json.loads(request.body)
    original_url = data.get('url')

    if not original_url:
        return JsonResponse({'error': 'URL is required'}, status=400)

    link = Link.objects.create(
        original_url=original_url,
        short_code=generate_short_code()
    )

    return JsonResponse(
        {'short_url': f"http://{request.get_host()}/{link.short_code}"},
        status=201
    )
    
    
def redirect_to_original(request, short_code):
    """
    Получаем short_code из URL, ищем ссылку в БД
    и делаем редирект на оригинальный URL
    """
    
    link = get_object_or_404(Link, short_code=short_code)
    return redirect(link.original_url)





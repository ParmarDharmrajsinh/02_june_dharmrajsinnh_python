from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to BlogX REST API",
        "endpoints": [
            "/api/posts/",
            "/admin/"
        ]
    })
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Welcome to BlogX API",
        "routes": {
            "admin": "/admin/",
            "api": "/api/",
            "accounts": "/api/accounts/"
        }
    })

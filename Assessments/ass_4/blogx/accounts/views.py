from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        if User.objects.filter(username=data['username']).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(
            username=data['username'],
            password=data['password']
        )
        return JsonResponse({"message": "User registered successfully"})

    return JsonResponse({"error": "POST method required"}, status=400)


@csrf_exempt
def login(request):
    return JsonResponse({"message": "Login endpoint ready"})

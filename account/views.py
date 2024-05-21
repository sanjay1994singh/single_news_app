import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from django.contrib.auth import authenticate, login


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = request.POST
        mobile_number = data.get('mobile_number')
        password = data.get('password')

        if not mobile_number:
            return JsonResponse({'error': 'Mobile number is required'}, status=400)

        if not password:
            return JsonResponse({'error': 'Password is required'}, status=400)

        # Generate a unique username
        username = str(uuid.uuid4())[:30]  # Generate a random UUID and truncate it to maximum length 30 characters
        if CustomUser.objects.filter(mobile_number=mobile_number).exists():
            return JsonResponse({'error': 'Mobile number already registered'}, status=400)

        # Create the user
        user = CustomUser(username=username,
                          mobile_number=mobile_number,
                          )
        user.set_password(password)
        user.save()

        return JsonResponse({'message': 'User registered successfully', 'username': username}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = request.POST
        mobile_number = data.get('mobile_number')
        password = data.get('password')

        if not mobile_number:
            return JsonResponse({'error': 'Mobile is required'}, status=400)

        if not password:
            return JsonResponse({'error': 'Password is required'}, status=400)

        user_obj = CustomUser.objects.filter(mobile_number__exact=mobile_number)
        if user_obj:
            username = user_obj[0].username
        else:
            return JsonResponse({'error': 'This mobile number is not registered is required'}, status=400)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

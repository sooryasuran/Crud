from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate


@csrf_exempt
def login_view(request):
    print('hi')
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        print('hi',username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                type = 'staff'
            elif user.is_student:
                type = 'student'
                result = user.is_authenticated
    try:
        result = user.is_authenticated
        data = {
            'status':True,
            'result': {
                'id': user.id,
                'name': user.username,
                'email': user.email,
                'type': type
            }
        }
    except:
        data = {
            'status': False
        }
    return JsonResponse(data, safe=False)
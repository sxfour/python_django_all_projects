from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PostgreSQL_app.models import Users
from PostgreSQL_app.serializers import UsersSerializer


# Create your views here.

# API для управления response сервера -> клиенту с использованием json
@csrf_exempt
def users_api(request, id=0):
    def get_method():
        return JsonResponse(UsersSerializer(Users.objects.all(), many=True).data, safe=False)

    def post_method():
        users_serializer = UsersSerializer(data=JSONParser().parse(request))
        if users_serializer.is_valid():
            users_serializer.save()

            return JsonResponse('Запись успешно добавлена', safe=False)

    def put_method():
        users_data = JSONParser().parse(request)
        users = Users.objects.get(user_id=users_data['user_id'])
        users_serializer = UsersSerializer(users, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()

            return JsonResponse('Обновлено успешно', safe=False)

    def delete_method():
        users = Users.objects.get(user_id=id)
        users.delete()

        return JsonResponse("Запись удалена успешно", safe=False)

    req_methods = {
        'GET': get_method,
        'POST': post_method,
        'PUT': put_method,
        'DELETE': delete_method,
    }

    return req_methods.get(request.method)()

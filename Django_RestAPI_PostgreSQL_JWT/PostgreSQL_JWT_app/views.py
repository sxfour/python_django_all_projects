from rest_framework.decorators import api_view, permission_classes

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PostgreSQL_JWT_app.models import Users
from PostgreSQL_JWT_app.serializers import UsersSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from PostgreSQL_JWT_conf.settings import MAX_LEN


# API для управления response сервера -> клиенту с использованием json, декораторы для обработки токена JWT
# Декоратор @csrf, обеспечивающий защиту CsrfViewMiddleware для представления, не обязательно с такой аутентификацией
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def users_api(request, id_resp=0):
    def get_method_all():
        if not bool(request.parser_context.get('args')):
            return JsonResponse(UsersSerializer(Users.objects.all(), many=True).data, safe=False)

    def get_method_by_id():
        if int(request.parser_context.get('args')[0]) <= MAX_LEN:
            return JsonResponse(UsersSerializer(Users.objects.get(user_id=id_resp), many=False).data, safe=False)

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
        users = Users.objects.get(user_id=id_resp)
        users.delete()

        return JsonResponse("Запись удалена успешно", safe=False)

    req_methods = {
        # Фильтрация GET запроса, доступны только цифры из re_path.
        'GET': (get_method_by_id if request.parser_context.get('args') else get_method_all),
        'POST': post_method,
        'PUT': put_method,
        'DELETE': delete_method,
    }

    return req_methods.get(request.method)()


# Пример класса с возвращением JSON, с использованием токена JWT
class TestJWTView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self):
        return Response({'message': f'Hello, JWT Auth!', 'header_info': self.headers})

from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from jwt_upload_app.serializers import DocumentsSerializer
from jwt_upload_app.models import Documents


# Create your views here.
# API для отправки документов .pdf, .zip в POST запросе к серверу.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def users_api(request):
    def get_method_all():
        data = Documents.objects.all()
        serializer = DocumentsSerializer(data, many=True)

        return Response(serializer.data)

    def post_method_sent():
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'Файл успешно отправлен'})

    req_methods = {
        'GET': get_method_all,
        'POST': post_method_sent,
    }

    return req_methods.get(request.method)()

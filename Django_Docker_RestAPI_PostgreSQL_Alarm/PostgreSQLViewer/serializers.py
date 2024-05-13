from rest_framework import serializers
from PostgreSQLViewer.models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

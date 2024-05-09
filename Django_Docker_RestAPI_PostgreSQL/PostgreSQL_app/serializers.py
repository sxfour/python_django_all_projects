from rest_framework import serializers
from PostgreSQL_app.models import Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

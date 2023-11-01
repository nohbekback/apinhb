from rest_framework import serializers
from .models import TLogin, TSession, TUser

class MiModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = TLogin, TSession, TUser
        fields = '__all__'

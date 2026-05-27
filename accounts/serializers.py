from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUser

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, trim_whitespace=False)

    def validate(self, data):
        #data en body del request
        user = authenticate(username= data['username'], password=data['password'])

        if user:
            data['user'] = user
            return data

        raise serializers.ValidationError("Credenciales inválidas")

class AssignRoleSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=[
        'admin', 'user', 'guest', 'almacen', 'inventario', 'cliente', 'proveedor'
    ])


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'is_active']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar información personalizada al token
        token['role'] = user.role

        return token

class RegisterAPIView(serializers.Serializer):
    pass

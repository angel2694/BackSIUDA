from rest_framework import serializers
from .models import CustomUser, Modulo, RolModulo, ROLE_CHOICES
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.conf import settings

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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'is_active']

class AssignRoleSerializer(serializers.Serializer):
    role = serializers.ChoiceField(choices=ROLE_CHOICES)

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password2': 'Las contraseñas no coinciden.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.role = 'guest'  # Asigna el rol 'guest' por defecto
        user.save()
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role']
        read_only_fields = ['id', 'username', 'role']

class ChangePasswordSerializer(serializers.Serializer):
    password_actual = serializers.CharField(write_only=True)
    password_nueva = serializers.CharField(write_only=True, min_length=6)
    password_nueva2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password_nueva'] != data['password_nueva2']:
            raise serializers.ValidationError({'password_nueva2': 'Las contraseñas no coinciden.'})
        return data
    
class ModuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modulo
        fields = ['id', 'nombre', 'url', 'icono']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        modulos = Modulo.objects.filter(
            rol_modulos__rol=user.role,
            rol_modulos__activo=True,
            activo=True
        )

        # Agregar información personalizada al token
        token['role'] = user.role
        token['username'] = user.username
        token['modulos'] = ModuloSerializer(modulos, many=True).data

        return token

#revisar con login 
class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError('No existe una cuenta con ese email.')
        return value

class PasswordResetConfirmSerializer(serializers.Serializer):
    uid   = serializers.CharField()
    token = serializers.CharField()
    password_nueva  = serializers.CharField(write_only=True, min_length=6)
    password_nueva2 = serializers.CharField(write_only=True)

    def validate(self, data):
        if data['password_nueva'] != data['password_nueva2']:
            raise serializers.ValidationError({'password_nueva2': 'Las contraseñas no coinciden.'})
        return data
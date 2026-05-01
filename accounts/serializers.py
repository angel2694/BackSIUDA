from rest_framework import serializers
from django.contrib.auth import authenticate

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
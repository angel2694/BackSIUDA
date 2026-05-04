from rest_framework import status

from .serializers import LoginSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LoginAPIView(APIView):
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {'detail': 'Credenciales inválidas'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        # serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)

        return Response({
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            },
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_protected(request):
    return Response({"message": "OK"})
from tokenize import Token

from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['GET'], detail=False, url_path='me')
    def me(self, request, *args, **kwargs):
        user: User = request.user
        user_payload = {
            'id': user.pk,
            'email': user.email
        }
        return Response(data=user_payload, status=status.HTTP_200_OK)
    
    @action(methods=['POST'], detail=False, url_path='login',  permission_classes=[AllowAny])
    def login(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if not user:
            return Response({'error': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
        
        if user.check_password(str(password)):
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
     
    
    @action(methods=['POST'], detail=False, url_path='register',  permission_classes=[AllowAny])
    def register(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

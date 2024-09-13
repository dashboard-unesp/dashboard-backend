from tokenize import Token
import bcrypt
from django.http import HttpResponse

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ReadOnlyModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from users.models import User
from users.serializers import UserSerializer
from rest_framework.decorators import action

class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False, url_path='me')
    def me(self, request, *args, **kwargs):
        return Response(data={'test':'me'},status=status.HTTP_401_UNAUTHORIZED)
    
    @action(methods=['POST'], detail=False, url_path='login')
    def login(self, request):
            password, email = request.data
            user = User.objects.all()
            if not user:
                return Response(data={'message': 'user not found'}, status=status.HTTP_404_NOT_FOUND)
            hash_password = bcrypt.hashpw(password, bcrypt.gensalt(rounds=10))
            if hash_password != user.password:
                return Response(data={'message': 'wrong password'}, status=status.HTTP_401_UNAUTHORIZED)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})

class RegisterViewSet(ViewSet):
    allowed_methods=['POST']
    serializer_class= UserSerializer
    queryset=User.objects.all()


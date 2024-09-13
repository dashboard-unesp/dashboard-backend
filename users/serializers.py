import bcrypt
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

    def create(self, validated_data):
        user = super().create(validated_data)
        hashed_password = bcrypt.hashpw(validated_data['password'].encode('utf-8'), bcrypt.gensalt(rounds=10))
        user.set_password(hashed_password)
        user.save()
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField()

    class Meta:
        model = User
        fields = ('email', 'password')
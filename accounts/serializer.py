from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=128)
    class Meta:
        model = CustomUser
        fields = ['username','password','confirm','email','first_name','last_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('password va  confirm bir xil emas')
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
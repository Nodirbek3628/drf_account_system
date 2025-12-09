from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    confirm = serializers.CharField(max_length=128)
    class Meta:
        model = CustomUser
        fields = ['username','password','confirm','email','first_name','last_name']

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm']:
            raise serializers.ValidationError('password va  confirm bir xil emas')
        
        return super().validate(attrs)
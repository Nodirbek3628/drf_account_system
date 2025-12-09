from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication


from rest_framework import status

from .serializer import RegisterSerializer, UserSerializer,LoginSerializer


class RegisterView(APIView):

    def post(self,request:Request)->Response:
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()

            user_json = UserSerializer(user).data

            return Response(user_json,status=status.HTTP_201_CREATED)

        
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
            
class LoginView(APIView):

    def post(self,request:Request)->Response:
        serilizer = LoginSerializer(data=request.data)

        if serilizer.is_valid(raise_exception=True):
            data = serilizer.validated_data
            user = authenticate(username=data['username'],password=data['password'])

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'Token': token.key}, status=status.HTTP_200_OK)
            
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self,request:Request)->Response:
        request.user.auth_token.delete()

        return Response({'message':'Logout boldingiz'},status=status.HTTP_204_NO_CONTENT)
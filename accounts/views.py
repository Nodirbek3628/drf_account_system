from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework import status

from .serializer import RegisterSerializer


class RegisterView(APIView):

    def post(self,request:Request)->Response:
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            return Response(serializer.validated_data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
            


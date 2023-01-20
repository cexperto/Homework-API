from django.shortcuts import render
from .serializer import RegisterSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.


class SignUpView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)
        # print(serializer)
        # print('*'*100)
        if serializer.is_valid():
            # import pdb; pdb.set_trace()
            serializer.save()
            response = {
                'message': 'User created successfully',
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



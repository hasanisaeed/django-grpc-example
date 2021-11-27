from django_grpc_framework import generics

import auth_pb2
import grpc

import book_pb2
from account.models import Book, User, generate_token
from account.serializers import UserProtoSerializer, BookProtoSerializer, LoginUserPairSerializer


class UserService(generics.ModelService):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer


class BookService(generics.ModelService):
    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookProtoSerializer

    def Retrieve(self, request, context):
        print(request)


class LoginService(generics.ModelService):
    serializer_class = LoginUserPairSerializer

    @staticmethod
    def Login(request, context):
        try:
            from google.protobuf import message
            response = auth_pb2.LoginResponse()
            username = request.username
            password = request.password
            user = User.objects.get(username=username)
            valid = user.check_password(password)
            if valid:
                token = generate_token(user)
                response.token = token
                return response
            else:
                return grpc.StatusCode.UNAUTHENTICATED
        except Exception as e:
            print(e)
            return grpc.StatusCode.NOT_FOUND

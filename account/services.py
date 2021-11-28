import datetime

import grpc
import jwt
from django_grpc_framework import generics

from account.models import Book, User
from account.serializers import UserProtoSerializer, BookProtoSerializer, LoginUserPairSerializer
from proto.auth import auth_pb2
from quickstart.settings import TOKEN_EXPIRATION, JWT_SECRET


class UserService(generics.ModelService):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer


class BookService(generics.ModelService):
    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookProtoSerializer

    def Retrieve(self, request, context):
        print(request)

    def UserBook(self, request, context):
        print(request)


def generate_token(user):
    user_info = {
        'username': user.username,
        'email': user.email,
        'user_id': user.id
    }
    return jwt.encode({
        'user_info': user_info,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRATION)
    }, JWT_SECRET, algorithm='HS256')


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
            else:
                response.status = grpc.StatusCode.UNAUTHENTICATED
            return response
        except Exception as e:
            return grpc.StatusCode.UNAUTHENTICATED

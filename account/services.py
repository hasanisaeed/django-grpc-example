import datetime

import grpc
import jwt
from django.conf.global_settings import SECRET_KEY
from django.db.models import QuerySet
from django.utils.decorators import classonlymethod
from django_grpc_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from account.authenticate import IsAuthenticated
from account.models import Book, User
from account.serializers import UserProtoSerializer, BookProtoSerializer, LoginUserPairSerializer
from proto import auth_pb2
from proto.book_pb2 import UserBooksResponse
from quickstart.settings import TOKEN_EXPIRATION, JWT_SECRET


class UserService(generics.ModelService):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserProtoSerializer


class BookService(generics.ModelService):
    lookup_field = 'id'
    queryset = Book.objects.all()
    serializer_class = BookProtoSerializer

    def __new__(cls, *args, **kwargs):
        if hasattr(cls, 'permission_class'):
            for i in getattr(cls, 'permission_class'):
                print(i())
            permissions = [permission() for permission in getattr(cls, 'permission_class')]
            print(permissions)
        return super(cls.__class__, cls).__new__(cls, *args, **kwargs)

    @classmethod
    def as_servicer(cls, **kwargs):
        from functools import update_wrapper
        update_wrapper(BookService, cls, updated=())
        return super(BookService, cls).as_servicer(**kwargs)

    def UserBookList(self, request, context):
        # auth = IsAuthenticated(UserBooksResponse,
        #                        jwt_key=JWT_SECRET,
        #                        permission_admin=True)
        # x = auth.do_authentication(context)
        # print(f'>> AUTH: {x}')
        pass

    def Retrieve(self, request, context):
        print(request)

    def UserBook(self, request, context):
        print(request)


def generate_token(user):
    user_info = {'username': user.username,
                 'email': None,
                 'is_superuser': user.is_superuser,
                 'user_id': user.id
                 }
    return jwt.encode({'user_info': user_info,
                       'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)  # TOKEN_EXPIRATION)
                       }, JWT_SECRET, algorithm='HS256')


class LoginService(generics.ModelService, TokenObtainPairView):

    def Login(self, request, context):
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

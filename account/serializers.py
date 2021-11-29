from django_grpc_framework import proto_serializers
from account.models import Book, User
from proto import user_pb2, book_pb2


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = user_pb2.User
        fields = ['id', 'username', 'email', 'groups']


class BookProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Book
        proto_class = book_pb2.Book
        fields = '__all__'


class LoginUserPairSerializer:

    def validate(self):
        return {'id': 1,
                'access_token': ' data[]',
                'refresh_token': 'refresh'}
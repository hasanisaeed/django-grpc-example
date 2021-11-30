from django_grpc_framework import proto_serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

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


class LoginUserPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(LoginUserPairSerializer, self).validate(attrs)
        output = {'user': self.user.phone,
                  'id': self.user.id,
                  'access_token': data['access'],
                  'refresh_token': data['refresh'], }
        return output

from account import views
from account.services import UserService, BookService, LoginService
from proto import user_pb2_grpc, book_pb2_grpc, auth_pb2_grpc

from django.urls import path

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),
]


def grpc_handlers(server):
    user_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)
    book_pb2_grpc.add_BookControllerServicer_to_server(BookService.as_servicer(), server)
    auth_pb2_grpc.add_AuthenticationServicer_to_server(LoginService.as_servicer(), server)

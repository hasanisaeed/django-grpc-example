from account.services import UserService, BookService, LoginService
from proto.auth import auth_pb2_grpc
from proto.book import book_pb2_grpc
from proto.user import user_pb2_grpc

urlpatterns = []


def grpc_handlers(server):
    user_pb2_grpc.add_UserControllerServicer_to_server(UserService.as_servicer(), server)
    book_pb2_grpc.add_BookControllerServicer_to_server(BookService.as_servicer(), server)
    auth_pb2_grpc.add_AuthenticationServicer_to_server(LoginService.as_servicer(), server)

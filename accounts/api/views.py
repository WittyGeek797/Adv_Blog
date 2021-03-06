from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView
)
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from rest_framework.pagination import(
    LimitOffsetPagination,
    PageNumberPagination,
)

from posts.api.pagination import PostLimitOffsetPagination, PagePageNumberPagination
from posts.api.permissions import IsOwnerOrReadOnly
from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permissions_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permissions_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

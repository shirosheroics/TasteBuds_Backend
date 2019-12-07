from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import (
	CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from .serializers import (
	UserCreateSerializer, 
	UserLoginSerializer,
    # ItemListSerializer,
    # ItemDetailSerializer,
    # ItemCreateSerializer
    # ListSerializer,  
    # DetailSerializer,
    # RetrieveUpdateAPIView
)
from rest_framework.filters import OrderingFilter, SearchFilter
# from app_name.models import ModelName
# from .models import Item
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
# from .permissions import IsOwner

# Create your views here.

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        my_data = request.data
        serializer = UserLoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)

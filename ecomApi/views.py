from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .models import Slider
from .models import User
from .models import Category
from .models import Orders
from .serializers import ProductSerializer
from .serializers import SliderSerializer
from .serializers import SliderSerializer
from .serializers import UserSerializer
from .serializers import CategorySerializer
from .serializers import OrdersSerializer
from .serializers import GoogleuserSerializer

# all product api functions
class Productlist(APIView):
    def get(self,request):
        try:
            id = request.query_params['id']
            if id != None:
                products = Product.objects.get(id = id)
                serializer = ProductSerializer(products)
        except:
            products = Product.objects.all()
            serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
# dynamic slider img api
class Sliderlist(APIView):
    def get(self,request):
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        pass

# users api
class Userlist(APIView):
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)
        
    def post(self,request):
        pass
# category api
class Catelist(APIView):
    def get(self,request):
        categoris = Category.objects.all()
        serializers = CategorySerializer(categoris,many=True)
        return Response(serializers.data)
# orders list are here
class Orderlist(APIView):
    def get(self,request):
        orders = Orders.objects.all()
        serializers = OrdersSerializer(orders,many=True)
        return Response(serializers.data)

    def post(self,request):
        serializers = OrdersSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            print('yes')
            return Response(serializers.data)
        else:
            print(serializers.errors)
            return Response(serializers.errors)
            
# user who logged in via google
class Googleuserlist(APIView):
    def get(self,request):
        return Response(data="Google user are so tough")
    def post(self,request):
        serializers = GoogleuserSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            print(serializers.errors)
            return Response(serializers.errors)
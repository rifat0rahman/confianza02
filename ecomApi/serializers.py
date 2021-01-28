from rest_framework import serializers
from .models import Product
from .models import Slider
from .models import Category
from .models import Orders
from .models import Googleuser
from django.contrib.auth.models import User
from djoser.serializers import UserCreateSerializer,UserSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'


class UserSerializer(UserCreateSerializer):
	class Meta(UserSerializer.Meta):
		model:User
		fields:'__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OrdersSerializer(serializers.ModelSerializer):
    cart:serializers.JSONField()
    pricing:serializers.JSONField()
    class Meta:
        model = Orders
        fields = '__all__'
class GoogleuserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Googleuser
        fields = '__all__'
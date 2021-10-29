from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['user', 'name', 'image','brand', 'category', 'description',
                  'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']

class ReviewSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Review
        fields = ['user', 'name', 'brand', 'category', 'description',
                  'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id'] 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'name', 'brand', 'category', 'description', 'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['name', 'brand', 'category', 'description', 'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['name', 'brand', 'category', 'description',
                  'rating', 'numReview', 'price', 'countInStock', 'createdAt', '_id']

from rest_framework import serializers
from .models import *


class ProductSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Product
        fields = ['user', 'name', 'image','brand', 'category', 'description',
                  'rating', 'numReview', 'price', 'countInStock', '_id']

class ReviewSerializer(serializers.ModelSerializer):  

    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Review
        fields = ['user', 'name', 'product', 'rating', 'comment', '_id'] 

class OrderSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Order
        fields = ['user', 'paymentMethod' ,'taxPrice', 'shippingPrice',
                  'totalPrice', 'isPaid', 'paidAt', 'isDelivered', 'deliveredAt', '_id']

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = ['name', 'order', 'product', 'qty', 'image', 'price', '_id']

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ['order', 'address', 'city', 'postalCode',
                  'country', 'shippingPrice', '_id']

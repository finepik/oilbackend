from rest_framework import serializers
from salagubmaslo.cart.models import *


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ("id", "anonymous", "id_for_anon", "time_create", "user")



class CartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ("id", "title", "price", "discount", "count", "image_cart", "cart")
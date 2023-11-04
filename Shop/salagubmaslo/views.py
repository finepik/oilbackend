from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class OilCatalogAPIView(APIView):
    def get(self, request):
        sort = self.request.query_params.get('sort_price', None)
        volume = self.request.query_params.get('volume', None)
        if sort == 'up':
            data = Oil.objects.order_by('price')
        elif sort == 'down':
            data = Oil.objects.order_by('-price')
        else:
            data = Oil.objects.all()
        if not volume is None:
            data = data.filter(volume=volume)
        data = OilCatalogSerializer(data, many=True).data
        return Response({'oil_products': data})

class OilProductAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            # конкретная запись в таблице
            product = Oil.objects.get(pk=pk)
        except:
            return Response({"error": "Method GET not allowed"})

        return Response({"oil_product": OilSerializer(product).data})

class OilMealProductAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            # конкретная запись в таблице
            product = OilMeal.objects.get(pk=pk)
        except:
            return Response({"error": "Method GET not allowed"})

        return Response({"oil_meal_product": OilMealSerializer(product).data})

class OilMealCatalogAPIView(APIView):
    def get(self, request):
        sort = self.request.query_params.get('sort_price', None)
        volume = self.request.query_params.get('volume', None)
        if sort == 'up':
            data = OilMeal.objects.order_by('price')
        elif sort == 'down':
            data = OilMeal.objects.order_by('-price')
        else:
            data = OilMeal.objects.all()
        if not volume is None:
            data = data.filter(volume=volume)
        data = OilMealCatalogSerializer(data, many=True).data
        return Response({'oil_meal_products': data})


class EquipmentPressProductAPIView(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            # конкретная запись в таблице
            product = EquipmentPress.objects.get(pk=pk)
        except:
            return Response({"error": "Method GET not allowed"})

        return Response({"equipment_press_product": EquipmentPressSerializer(product).data})


class EquipmentPressCatalogAPIView(APIView):
    def get(self, request):
        sort = self.request.query_params.get('sort_price', None)
        # start = self.request.query_params.get('start_price', None)
        # stop = self.request.query_params.get('stop_price', None)
        # from-to sort
        # if (not start is None) and (not stop is None):
        #     data = EquipmentPressCatalogSerializer(EquipmentPress.objects.filter(price__lte=stop).filter(price__gte=start),
        #                                            many=True).data
        # elif not start is None:
        #     data = EquipmentPressCatalogSerializer(
        #         EquipmentPress.objects.filter(price__gte=start), many=True).data
        # elif not stop is None:
        #     data = EquipmentPressCatalogSerializer(
        #         EquipmentPress.objects.filter(price__lte=stop), many=True).data
        if sort == 'up':
            data = EquipmentPressCatalogSerializer(EquipmentPress.objects.order_by('price'), many=True).data
        elif sort == 'down':
            data = EquipmentPressCatalogSerializer(EquipmentPress.objects.order_by('-price'), many=True).data
        else:
            data = EquipmentPressCatalogSerializer(EquipmentPress.objects.all(), many=True).data
        return Response({'equipment_press_products': data})



class EquipmentSupplementProductAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method GET not allowed"})

        try:
            # конкретная запись в таблице
            product = EquipmentSupplement.objects.get(pk=pk)
        except:
            return Response({"error": "Method GET not allowed"})

        return Response({"equipment_supplement_product": EquipmentSupplementSerializer(product).data})


class EquipmentSupplementCatalogAPIView(APIView):
    def get(self, request):
        sort = self.request.query_params.get('sort_price', None)
        if sort == 'up':
            data = EquipmentSupplementCatalogSerializer(EquipmentSupplement.objects.order_by('price'), many=True).data
        elif sort == 'down':
            data = EquipmentSupplementCatalogSerializer(EquipmentSupplement.objects.order_by('-price'), many=True).data
        else:
            data = EquipmentSupplementCatalogSerializer(EquipmentSupplement.objects.all(), many=True).data
        return Response({'equipment_supplement_products': data})

class QaAPIView(APIView):
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        all_answers = QA.objects.all()
        return Response({'answers': qaSerializer(all_answers, many=True).data})

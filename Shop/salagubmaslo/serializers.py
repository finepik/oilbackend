from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from salagubmaslo.models import *


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # Add custom claims
        token['username'] = user.username
        return token

class OilImageSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = OilImage
        fields = ("id", "title", "image")
    def get_image_url(self, obj):
        return obj.image.url
class OilSerializer(serializers.ModelSerializer):
    oil_image = OilImageSerializer(many=True)

    class Meta:
        model = Oil
        fields = ("id", "title", "sub_title", "volume", "price", "discount", "description",
                  "in_cooking", "use_and_dosage", "composition", "keeping", "recipe", "oil_image")


class OilCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Oil
        fields = ("id", "title", "price", "oil_catalog_image")


class OilMealImageSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = OilMealImage
        fields = ("id", "title", "image")
    def get_image_url(self, obj):
        return obj.image.url


class OilMealSerializer(serializers.ModelSerializer):
    oil_meal_image = OilMealImageSerializer(many=True)

    class Meta:
        model = OilMeal
        fields = ("id", "title", "sub_title", "volume", "price", "discount", "description",
                  "in_cooking", "in_cosmetology", "use_and_dosage", "composition",
                  "keeping", "recipe", "oil_meal_image")


class OilMealCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = OilMeal
        fields = ("id", "title", "price", "oil_meal_catalog_image")


class EquipmentPressImageSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = EquipmentPressImage
        fields = ("id", "title", "image")
    def get_image_url(self, obj):
        return obj.image.url


class EquipmentPressCompositionSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = EquipmentPressComposition
        fields = ("id", "title", "image")
    def get_image_url(self, obj):
        return obj.image.url


class EquipmentPressSerializer(serializers.ModelSerializer):
    equipment_press_image = EquipmentPressImageSerializer(many=True)
    equipment_press_composition = EquipmentPressCompositionSerializer(many=True)

    class Meta:
        model = EquipmentPress
        fields = ("id", "title", "sub_title", "price", "discount", "video_link",
                  "equipment_press_image", "equipment_press_composition")


class EquipmentPressCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentPress
        fields = ("id", "title", "price", "equipment_press_catalog_image")


class EquipmentSupplementImageSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = EquipmentSupplementImage
        fields = ("id", "title", "image")
    def get_image_url(self, obj):
        return obj.image.url


class EquipmentSupplementSerializer(serializers.ModelSerializer):
    equipment_supplement_image = EquipmentSupplementImageSerializer(many=True)

    class Meta:
        model = EquipmentSupplement
        fields = ("id", "title", "sub_title", "price", "discount", "equipment_supplement_construct",
                  "equipment_supplement_construct_image", "equipment_supplement_image")


class EquipmentSupplementCatalogSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipmentSupplement
        fields = ("id", "title", "price", "equipment_supplement_catalog_image")


class qaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QA
        fields = "__all__"
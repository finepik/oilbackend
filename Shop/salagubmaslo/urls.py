from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('oil_products/', OilCatalogAPIView.as_view()),
    path('oil_products/<int:pk>/', OilProductAPIView.as_view()),
    path('oil_meal_products/', OilMealCatalogAPIView.as_view()),
    path('oil_meal_products/<int:pk>/', OilMealProductAPIView.as_view()),
    path('equipment_press_products/', EquipmentPressCatalogAPIView.as_view()),
    path('equipment_press_products/<int:pk>/', EquipmentPressProductAPIView.as_view()),
    path('equipment_supplement_products/', EquipmentSupplementCatalogAPIView.as_view()),
    path('equipment_supplement_products/<int:pk>/', EquipmentSupplementProductAPIView.as_view()),
    path('question_answer/', QaAPIView.as_view()),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
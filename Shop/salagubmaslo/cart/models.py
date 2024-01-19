from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    anonymous = models.BooleanField(default=True, verbose_name="Не авторизован")
    id_for_anon = models.CharField(null=True, blank=True, verbose_name="Id сессии")
    time_create = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='Пользователь', on_delete=models.CASCADE)


class CartItem(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название продукта")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.IntegerField(verbose_name="Скидка в %")
    count = models.IntegerField(verbose_name="Количество")
    image_cart = models.SlugField(null=True, blank=True, verbose_name="Ссылка на изображение продукта")
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE)

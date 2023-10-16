from django.db import models
from django.contrib.auth.models import User

class Oil(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="photos/oil_photos/", blank=True, null=True)
    volume = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    description = models.CharField(max_length=2500)
    in_cooking = models.CharField(max_length=1000)
    in_cosmetology = models.CharField(max_length=1000)
    use_and_dosage = models.CharField(max_length=1000)
    composition = models.CharField(max_length=2500)
    # product = models.ForeignKey(product, verbose_name='Эталонный продукт', on_delete=models.SET(None), null=True)

    def __str__(self):
        return self.title
class QA(models.Model):
    question = models.CharField(max_length=225)
    answer = models.CharField(max_length=1000)

    def __str__(self):
        return self.question
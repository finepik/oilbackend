from django.db import models
from django.contrib.auth.models import User


class OilImage(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="photos/oil_photos/", blank=True, null=True)

    def __str__(self):
        return self.title


class Oil(models.Model):
    title = models.CharField(max_length=1000)
    sub_title = models.CharField(max_length=1000, null=True, blank=True)
    volume = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    description = models.TextField(max_length=5000, null=True, blank=True)
    in_cooking = models.TextField(max_length=5000, null=True, blank=True)
    use_and_dosage = models.TextField(max_length=5000, null=True, blank=True)
    composition = models.TextField(max_length=5000, null=True, blank=True)
    keeping = models.TextField(max_length=5000, null=True, blank=True)
    recipe = models.TextField(max_length=5000, null=True, blank=True)
    oil_catalog_image = models.ImageField(upload_to="photos/oil_photos/catalog/", blank=True, null=True)
    oil_image = models.ManyToManyField(OilImage, related_name="oil_images", verbose_name="Фото масла")

    def __str__(self):
        return self.title


class OilMealImage(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    image = models.ImageField(upload_to="photos/oil_meal_photos/", blank=True, null=True)

    def __str__(self):
        return self.title


class OilMeal(models.Model):
    title = models.CharField(max_length=1000)
    sub_title = models.CharField(max_length=1000, null=True, blank=True)
    volume = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    description = models.TextField(max_length=5000, null=True, blank=True)
    in_cooking = models.TextField(max_length=5000, null=True, blank=True)
    in_cosmetology = models.TextField(max_length=5000, null=True, blank=True)
    use_and_dosage = models.TextField(max_length=5000, null=True, blank=True)
    composition = models.TextField(max_length=5000, null=True, blank=True)
    keeping = models.TextField(max_length=5000, null=True, blank=True)
    recipe = models.TextField(max_length=5000, null=True, blank=True)
    oil_meal_catalog_image = models.ImageField(upload_to="photos/oil_meal_photos/catalog/", blank=True, null=True)
    oil_meal_image = models.ManyToManyField(OilMealImage, related_name="oil_meal_images", verbose_name="Фото жмыха")

    def __str__(self):
        return self.title


class EquipmentPressImage(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="photos/equipment_press_photos/", blank=True, null=True)

    def __str__(self):
        return self.title


class EquipmentPressComposition(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="photos/equipment_press_composition_photos/", blank=True, null=True)

    def __str__(self):
        return self.title


class EquipmentPress(models.Model):
    title = models.CharField(max_length=1000)
    sub_title = models.TextField(max_length=5000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    video_link = models.SlugField(null=True, blank=True)
    equipment_press_catalog_image = models.ImageField(upload_to="photos/equipment_press_photos/catalog/",
                                                      blank=True, null=True)
    equipment_press_image = models.ManyToManyField(EquipmentPressImage, related_name="equipment_press_images",
                                                   verbose_name="Фото пресса")
    equipment_press_composition = models.ManyToManyField(EquipmentPressComposition,
                                                         related_name="equipment_press_composition_images",
                                                         verbose_name="Фото частей конструкции пресса")

    def __str__(self):
        return self.title


class EquipmentSupplementImage(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="photos/equipment_supplement_photos/", blank=True, null=True)

    def __str__(self):
        return self.title


class EquipmentSupplement(models.Model):
    title = models.CharField(max_length=1000)
    sub_title = models.TextField(max_length=5000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.IntegerField()
    description = models.TextField(max_length=5000, null=True, blank=True)
    equipment_supplement_catalog_image = models.ImageField(upload_to="photos/equipment_supplement_photos/catalog/",
                                                           blank=True, null=True)

    equipment_supplement_construct_image = models.ImageField(upload_to="photos/equipment_supplement_photos/construct/",
                                                             blank=True, null=True)
    equipment_supplement_construct = models.TextField(max_length=5000, null=True, blank=True)
    equipment_supplement_image = models.ManyToManyField(EquipmentSupplementImage,
                                                        related_name="equipment_supplement_images",
                                                        verbose_name="Фото дополнений")

    def __str__(self):
        return self.title


class QA(models.Model):
    question = models.CharField(max_length=225)
    answer = models.TextField(max_length=100000)

    def __str__(self):
        return self.question

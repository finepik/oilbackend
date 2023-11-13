from django.db import models
from django.contrib.auth.models import User


class OilImage(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Название фото")
    image = models.ImageField(upload_to="photos/oil_photos/", blank=True, null=True, verbose_name="Фото масла")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Изображения масел'


class Oil(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название масла")
    sub_title = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Краткое описание")
    volume = models.IntegerField(verbose_name="Объем")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.IntegerField(verbose_name="Скидка в %")
    description = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Описание")
    in_cooking = models.TextField(max_length=5000, null=True, blank=True, verbose_name="В кулинарии")
    use_and_dosage = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Применение и дозировка")
    composition = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Содержит")
    keeping = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Хранение")
    recipe = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Рецепт")
    oil_catalog_image = models.ImageField(upload_to="photos/oil_photos/catalog/", blank=True, null=True,
                                          verbose_name="Фото для каталога")
    oil_image = models.ManyToManyField(OilImage, related_name="oil_images", verbose_name="Фото масла")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Масла'


class OilMealImage(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True, verbose_name="Название фото")
    image = models.ImageField(upload_to="photos/oil_meal_photos/", blank=True, null=True,
                              verbose_name="Фото жмыха")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Изображения жмыхов'


class OilMeal(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название жмыха")
    sub_title = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Краткое описание")
    volume = models.IntegerField( verbose_name="Объем")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.IntegerField( verbose_name="Скидка в %")
    description = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Описание")
    in_cooking = models.TextField(max_length=5000, null=True, blank=True, verbose_name="В кулинарии")
    in_cosmetology = models.TextField(max_length=5000, null=True, blank=True, verbose_name="В косметологии")
    use_and_dosage = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Применение и дозировка")
    composition = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Содержит")
    keeping = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Хранение")
    recipe = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Рецепт")
    oil_meal_catalog_image = models.ImageField(upload_to="photos/oil_meal_photos/catalog/", blank=True, null=True,
                                               verbose_name="Фото для каталога")
    oil_meal_image = models.ManyToManyField(OilMealImage, related_name="oil_meal_images", verbose_name="Фото жмыха")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Жмых'


class EquipmentPressImage(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название фото")
    image = models.ImageField(upload_to="photos/equipment_press_photos/", blank=True, null=True, verbose_name="Фото пресса")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Изображения прессов'

class EquipmentPressComposition(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название модуля")
    image = models.ImageField(upload_to="photos/equipment_press_composition_photos/", blank=True, null=True, verbose_name="Фото модуля")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Изображения комплектации прессов'


class EquipmentPress(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название пресса")
    sub_title = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="цена")
    discount = models.IntegerField( verbose_name="Скидка в %")
    video_link = models.SlugField(null=True, blank=True, verbose_name="Ссылка на видео о прессе")
    equipment_press_catalog_image = models.ImageField(upload_to="photos/equipment_press_photos/catalog/",
                                                      blank=True, null=True, verbose_name="Фото для каталога")
    equipment_press_image = models.ManyToManyField(EquipmentPressImage, related_name="equipment_press_images",
                                                   verbose_name="Фото пресса")
    equipment_press_composition = models.ManyToManyField(EquipmentPressComposition,
                                                         related_name="equipment_press_composition_images",
                                                         verbose_name="Фото частей конструкции пресса")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Прессы'


class EquipmentSupplementImage(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название фото")
    image = models.ImageField(upload_to="photos/equipment_supplement_photos/", blank=True, null=True, verbose_name="Фото")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Изображения дополнений'


class EquipmentSupplement(models.Model):
    title = models.CharField(max_length=1000, verbose_name="Название дополнений")
    sub_title = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Краткое описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    discount = models.IntegerField(verbose_name="Скидка в %")
    description = models.TextField(max_length=5000, null=True, blank=True, verbose_name="Описание")
    equipment_supplement_catalog_image = models.ImageField(upload_to="photos/equipment_supplement_photos/catalog/",
                                                           blank=True, null=True, verbose_name="Фото для каталога")

    equipment_supplement_construct_image = models.ImageField(upload_to="photos/equipment_supplement_photos/construct/",
                                                             blank=True, null=True, verbose_name="Фото конструкции дополнения")
    equipment_supplement_construct = models.TextField(max_length=5000, null=True, blank=True)
    equipment_supplement_image = models.ManyToManyField(EquipmentSupplementImage,
                                                        related_name="equipment_supplement_images",
                                                        verbose_name="Фото дополнений")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Дополнения'


class QA(models.Model):
    question = models.CharField(max_length=225, verbose_name="Вопрос")
    answer = models.TextField(max_length=100000, verbose_name="Ответ")

    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = 'Вопросы и ответы '

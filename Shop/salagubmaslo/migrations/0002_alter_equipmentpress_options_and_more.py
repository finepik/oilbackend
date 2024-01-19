# Generated by Django 4.1.5 on 2023-11-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salagubmaslo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipmentpress',
            options={'verbose_name_plural': 'Прессы'},
        ),
        migrations.AlterModelOptions(
            name='equipmentpresscomposition',
            options={'verbose_name_plural': 'Изображения комплектации прессов'},
        ),
        migrations.AlterModelOptions(
            name='equipmentpressimage',
            options={'verbose_name_plural': 'Изображения прессов'},
        ),
        migrations.AlterModelOptions(
            name='equipmentsupplement',
            options={'verbose_name_plural': 'Дополнения'},
        ),
        migrations.AlterModelOptions(
            name='equipmentsupplementimage',
            options={'verbose_name_plural': 'Изображения дополнений'},
        ),
        migrations.AlterModelOptions(
            name='oil',
            options={'verbose_name_plural': 'Масла'},
        ),
        migrations.AlterModelOptions(
            name='oilimage',
            options={'verbose_name_plural': 'Изображения масел'},
        ),
        migrations.AlterModelOptions(
            name='oilmeal',
            options={'verbose_name_plural': 'Жмых'},
        ),
        migrations.AlterModelOptions(
            name='oilmealimage',
            options={'verbose_name_plural': 'Изображения жмыхов'},
        ),
        migrations.AlterModelOptions(
            name='qa',
            options={'verbose_name_plural': 'Вопросы и ответы '},
        ),
        migrations.AlterField(
            model_name='equipmentpress',
            name='discount',
            field=models.IntegerField(verbose_name='Скидка в %'),
        ),
        migrations.AlterField(
            model_name='equipmentpress',
            name='equipment_press_catalog_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/equipment_press_photos/catalog/', verbose_name='Фото для каталога'),
        ),
        migrations.AlterField(
            model_name='equipmentpress',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='цена'),
        ),
        migrations.AlterField(
            model_name='equipmentpress',
            name='sub_title',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='equipmentpress',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название пресса'),
        ),
        migrations.AlterField(
            model_name='equipmentpress',
            name='video_link',
            field=models.SlugField(blank=True, null=True, verbose_name='Ссылка на видео о прессе'),
        ),
        migrations.AlterField(
            model_name='equipmentpresscomposition',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/equipment_press_composition_photos/', verbose_name='Фото модуля'),
        ),
        migrations.AlterField(
            model_name='equipmentpresscomposition',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название модуля'),
        ),
        migrations.AlterField(
            model_name='equipmentpressimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/equipment_press_photos/', verbose_name='Фото пресса'),
        ),
        migrations.AlterField(
            model_name='equipmentpressimage',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название фото'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplement',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplement',
            name='discount',
            field=models.IntegerField(verbose_name='Скидка в %'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplement',
            name='equipment_supplement_catalog_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/equipment_supplement_photos/catalog/', verbose_name='Фото для каталога'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplement',
            name='equipment_supplement_construct_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/equipment_supplement_photos/construct/', verbose_name='Фото конструкции дополнения'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplement',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplement',
            name='sub_title',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplement',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название дополнений'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplementimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/equipment_supplement_photos/', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='equipmentsupplementimage',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название фото'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='composition',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Содержит'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='discount',
            field=models.IntegerField(verbose_name='Скидка в %'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='in_cooking',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='В кулинарии'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='keeping',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Хранение'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='oil_catalog_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/oil_photos/catalog/', verbose_name='Фото для каталога'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='recipe',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='sub_title',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название масла'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='use_and_dosage',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Применение и дозировка'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='volume',
            field=models.IntegerField(verbose_name='Объем'),
        ),
        migrations.AlterField(
            model_name='oilimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/oil_photos/', verbose_name='Фото масла'),
        ),
        migrations.AlterField(
            model_name='oilimage',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Название фото'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='composition',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Содержит'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='discount',
            field=models.IntegerField(verbose_name='Скидка в %'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='in_cooking',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='В кулинарии'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='in_cosmetology',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='В косметологии'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='keeping',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Хранение'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='oil_meal_catalog_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/oil_meal_photos/catalog/', verbose_name='Фото для каталога'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='recipe',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Рецепт'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='sub_title',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Название жмыха'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='use_and_dosage',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Применение и дозировка'),
        ),
        migrations.AlterField(
            model_name='oilmeal',
            name='volume',
            field=models.IntegerField(verbose_name='Объем'),
        ),
        migrations.AlterField(
            model_name='oilmealimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/oil_meal_photos/', verbose_name='Фото жмыха'),
        ),
        migrations.AlterField(
            model_name='oilmealimage',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Название фото'),
        ),
        migrations.AlterField(
            model_name='qa',
            name='answer',
            field=models.TextField(max_length=100000, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='qa',
            name='question',
            field=models.CharField(max_length=225, verbose_name='Вопрос'),
        ),
    ]

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from salagubmaslo.models import *

class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

admin.site.register(QA,SummerAdmin)
admin.site.register(Oil, SummerAdmin)
admin.site.register(OilMeal, SummerAdmin)
admin.site.register(EquipmentPress, SummerAdmin)
admin.site.register(EquipmentSupplement, SummerAdmin)
admin.site.register(OilMealImage)
admin.site.register(OilImage)
admin.site.register(EquipmentPressImage)
admin.site.register(EquipmentPressComposition)
admin.site.register(EquipmentSupplementImage)
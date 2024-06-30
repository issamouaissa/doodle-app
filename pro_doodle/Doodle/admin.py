from django.contrib import admin
from .models import Sondage, DateSondage

# Register your models here.

@admin.register(Sondage)
class SondageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lieux', 'date', 'heure')

@admin.register(DateSondage)
class DateSondageAdmin(admin.ModelAdmin):
    list_display = ('sondage', 'date')

    def sondage(self, obj):
        return obj.sondage.name

    def date(self, obj):
        return obj.date 

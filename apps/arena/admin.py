from django.contrib import admin
from .models import Arena, Images


class ArenaAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'address')


admin.site.register(Arena, ArenaAdmin)

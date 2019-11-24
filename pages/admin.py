from django.contrib import admin

from .models import God, Item, Match, Build

admin.site.register(God)
admin.site.register(Item)
admin.site.register(Match)
admin.site.register(Build)
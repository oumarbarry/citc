from django.contrib import admin
from .models import *

admin.site.register(ModifierListeFormation)
admin.site.register(Presentation)
admin.site.register(ModifierGrille)
admin.site.register(HomeContainer)

@admin.register(ModifierDetailFormation)
class ModifierDetailFormationAdmin(admin.ModelAdmin):
    search_fields = ['id_formation', 'title']

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_filter = ('place_event', )
    search_fields = ['id_events', 'title', 'place_event']
    list_display = ['title', 'place_event', 'date_pub']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_filter = ('publisher', )
    search_fields = ['id_news', 'title', 'publisher']
    list_display = ['title', 'publisher', 'date_pub']

@admin.register(Temoignages)
class TemoignagesAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name', 'degree']
    list_display = ['id', 'name', 'degree', 'date_pub']
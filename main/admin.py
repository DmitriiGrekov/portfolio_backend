from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import SiteModel


@admin.register(SiteModel)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 
                    'link_to_site', 
                    'link_to_rep',
                    'get_image')

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="50" height="60">')

    get_image.short_description = "Фото сайта"
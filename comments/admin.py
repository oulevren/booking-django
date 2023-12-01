from django.contrib import admin
from .models import *
# Register your models here.

class YorumAdmin(admin.ModelAdmin):
    list_display = ['description','rating','is_active']
    search_fields = ['rating','description']
    list_filter = ['rating','description']
    list_editable = ['is_active']

    # prepopulated_fields = {'slug':['title']}
    # readonly_fields = ['title']

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['name','slug']
#     readonly_fields = ['slug']

admin.site.register(Yorum,YorumAdmin)
# admin.site.register(category,CategoryAdmin)
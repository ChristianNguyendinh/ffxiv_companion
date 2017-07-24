from django.contrib import admin
from item_companion.models import Test, Items

class TestAdmin(admin.ModelAdmin):
    fields = ('name', 'age',)
    list_display = ('name', 'age')
    list_filter = ('name', 'age')

class ItemsAdmin(admin.ModelAdmin):
    fields = ('name', 'main_type', 'sub_type', 'ilvl', 'rlvl')
    list_display = ('name', 'main_type', 'sub_type', 'ilvl', 'rlvl')
    list_filter = ('main_type',)
    

admin.site.register(Test, TestAdmin)
admin.site.register(Items, ItemsAdmin)
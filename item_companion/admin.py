from django.contrib import admin
from item_companion.models import Test

# Register your models here.
class TestAdmin(admin.ModelAdmin):
    fields = ('name', 'age',)
    list_display = ('name', 'age')
    list_filter = ('name', 'age')

admin.site.register(Test, TestAdmin)
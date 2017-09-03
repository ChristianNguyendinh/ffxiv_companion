from django.contrib import admin
from item_companion.models import Test, Items, Botany_Node, Miner_Node

class TestAdmin(admin.ModelAdmin):
    fields = ('name', 'age',)
    list_display = ('name', 'age')
    list_filter = ('name', 'age')

class ItemsAdmin(admin.ModelAdmin):
    fields = ('name', 'main_type', 'sub_type', 'iid', 'img', 'ilvl', 'rlvl')
    list_display = ('name', 'main_type', 'sub_type', 'ilvl', 'rlvl')
    list_filter = ('main_type',)
    
class BotanyAdmin(admin.ModelAdmin):
    fields = ('item', 'level', 'node_type', 'zone', 'coords')
    list_display = ('item', 'level', 'node_type', 'zone', 'coords')
    list_filter = ('zone',)

class MinerAdmin(admin.ModelAdmin):
    fields = ('item', 'level', 'node_type', 'zone', 'coords')
    list_display = ('item', 'level', 'node_type', 'zone', 'coords')
    list_filter = ('zone',)

admin.site.register(Test, TestAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Botany_Node, BotanyAdmin)
admin.site.register(Miner_Node, MinerAdmin)
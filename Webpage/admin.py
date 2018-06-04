from django.contrib import admin
from .models import Laptop, Processor, GraphicsCard, StorageDrive, RAM, Display, LaptopInstance

class LaptopsInstanceInline(admin.TabularInline):
    model = LaptopInstance

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand_name', 'processor', 'display_graphics_card', 'ram')
    list_filter = ('brand_name', 'processor', 'graphics_card')
    fields = ['model_name', 'brand_name', ('width', 'height', 'depth'), 'weight', 'processor', 'graphics_card', 'ram', 'storage_drive', 'display', 'operating_system', 'date_of_release']
    inlines = [LaptopsInstanceInline]

@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'base_clock', 'turbo_clock', 'cores', 'threads')
    list_filter = ('manufacturer', 'cores', 'threads')
    fields = ['model_name', 'manufacturer', ('cores', 'threads'), ('base_clock', 'turbo_clock'), 'L3_cache', 'TDP', 'manufacturing_technology']

@admin.register(GraphicsCard)
class GraphicsCardAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'type', 'core_base_speed', 'core_turbo_speed', 'memory', 'memory_speed')
    list_filter = ('manufacturer', 'type', 'memory')
    fields = ['model_name', 'manufacturer', 'type', ('core_base_speed', 'core_turbo_speed'), ('memory', 'memory_speed', 'memory_bus_width'), 'pipelines', ('manufacturing_technology', 'architecture')]

@admin.register(StorageDrive)
class StorageDriveAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'type', 'size', 'read_speed', 'write_speed')
    list_filter = ('manufacturer', 'type', 'size')
    fields = ['model_name', 'manufacturer', 'type', 'size', ('read_speed', 'write_speed')]

@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ('type', 'frequency', 'size')
    list_filter = ('type', 'size', 'frequency')
    fields = ['type', ('size', 'max_size'), 'frequency']

@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    list_display = ('size', 'resolution', 'type')
    list_filter = ('type', 'size', 'resolution')
    fields = ['type', ('size', 'resolution'), 'refresh_rate']

@admin.register(LaptopInstance)
class LaptopInstanceAdmin(admin.ModelAdmin):
    list_display = ('laptop', 'status')
    list_filter = ('status',)

    fieldsets = (
        (None, {
            'fields': ('laptop', 'description', 'id')
        }),
        ('Status', {
            'fields': ('status',)
        }),
    )

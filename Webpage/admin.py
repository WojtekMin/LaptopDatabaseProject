from django.contrib import admin
from .models import Laptop, Processor, GraphicsCard, StorageDrive, RAM, Display

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'brand_name', 'processor', 'display_graphics_card', 'ram')
    list_filter = ('brand_name', 'processor', 'graphics_card')

@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'base_clock', 'turbo_clock', 'cores', 'threads')
    list_filter = ('manufacturer', 'cores', 'threads')

@admin.register(GraphicsCard)
class GraphicsCardAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'type', 'core_base_speed', 'core_turbo_speed', 'memory', 'memory_speed')
    list_filter = ('manufacturer', 'type', 'memory')

@admin.register(StorageDrive)
class StorageDriveAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'manufacturer', 'type', 'size', 'read_speed', 'write_speed')
    list_filter = ('manufacturer', 'type', 'size')

@admin.register(RAM)
class RAMAdmin(admin.ModelAdmin):
    list_display = ('type', 'frequency', 'size')
    list_filter = ('type', 'size', 'frequency')

@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    list_display = ('size', 'resolution', 'type')
    list_filter = ('type', 'size', 'resolution')

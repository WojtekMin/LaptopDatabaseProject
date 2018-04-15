from django.contrib import admin
from .models import Laptop, Processor, GraphicsCard, StorageDrive, RAM, Display
# Register your models here.
admin.site.register(Laptop)
admin.site.register(Processor)
admin.site.register(GraphicsCard)
admin.site.register(StorageDrive)
admin.site.register(RAM)
admin.site.register(Display)


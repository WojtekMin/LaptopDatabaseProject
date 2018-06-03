from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class GraphicsCard(models.Model):
    model_name = models.CharField(max_length=100)

    MANUFACTURER_TYPE = (
        ('AMD', 'AMD'),
        ('Intel', 'Intel'),
        ('Nvidia', 'Nvidia'),
    )

    manufacturer = models.CharField(max_length=8, choices=MANUFACTURER_TYPE, default='Intel', blank=False, help_text='Manufacturer type')

    TYPE = (
        ('Discrete', 'Discrete'),
        ('Integrated', 'Integrated'),
    )

    type = models.CharField(max_length=12, choices=TYPE, default='d', blank=False, help_text='Discrete or integrated')
    architecture = models.CharField(max_length=100)
    core_base_speed = models.IntegerField(help_text="In MHz")
    core_turbo_speed = models.IntegerField(help_text="In MHz")
    memory = models.IntegerField(help_text="In MB")
    memory_speed = models.IntegerField(help_text="In MHz")
    memory_bus_width = models.IntegerField(help_text="In Bits")
    pipelines = models.IntegerField()
    manufacturing_technology = models.IntegerField(help_text="In nm")


    class Meta:
        ordering = ["model_name"]


    def get_absolute_url(self):
        return reverse('graphics_card-detail', args=[str(self.id)])


    def __str__(self):
        return self.manufacturer + " " + self.model_name


class StorageDrive(models.Model):
    model_name = models.CharField(max_length=100)

    MANUFACTURER_TYPE = (
        ('Adata', 'Adata'),
        ('Intel', 'Intel'),
        ('Kingston', 'Kingston'),
        ('Micron','Micron'),
        ('Samsung', 'Samsung'),
        ('SanDisk', 'SanDisk'),
        ('Seagate', 'Seagate'),
        ('Transcend', 'Transcend'),
        ('WD', 'WD'),
    )

    manufacturer = models.CharField(max_length=8, choices=MANUFACTURER_TYPE, default='Samsung', blank=False, help_text='Manufacturer type')

    TYPE = (
        ('HDD', 'HDD'),
        ('SSD', 'SSD'),
    )

    type = models.CharField(max_length=8, choices=TYPE, default='d', blank=False, help_text='HDD or SSD')
    read_speed = models.IntegerField(help_text="In MB/s")
    write_speed = models.IntegerField(help_text="In MB/s")
    size = models.IntegerField(help_text="In GB")

    class Meta:
        ordering = ["model_name"]

    def get_absolute_url(self):
        return reverse('storage_drive-detail', args=[str(self.id)])

    def __str__(self):
        return self.manufacturer + " " + self.model_name



class Laptop(models.Model):
    model_name = models.CharField(max_length=200)

    BRAND_NAME = (
        ('Acer', 'Acer'),
        ('Apple', 'Apple'),
        ('Asus', 'Asus'),
        ('Dell', 'Dell'),
        ('Gigabyte', 'Gigabyte'),
        ('HP', 'HP'),
        ('Huawei', 'Huawei'),
        ('Lenovo', 'Lenovo'),
        ('Microsoft', 'Microsoft'),
        ('MSI', 'MSI'),
        ('Razer', 'Razer'),
    )

    brand_name = models.CharField(max_length=8, choices=BRAND_NAME, default='Acer', blank=False, help_text='Brand name')
    width = models.FloatField(help_text="In cm")
    height = models.FloatField(help_text="In cm")
    depth = models.FloatField(help_text="In cm")
    weight = models.FloatField(help_text="In kg")

    OPERATING_SYSTEM = (
        ('MacOS', 'MacOS'),
        ('Windows 10', 'Windows 10'),
    )

    operating_system = models.CharField(max_length=10, choices=OPERATING_SYSTEM, default='Windows 10', blank=False, help_text='Opearating system')
    date_of_release = models.DateField()
    processor = models.ForeignKey('Processor', on_delete=models.SET_NULL, null=True)
    graphics_card = models.ManyToManyField(GraphicsCard)
    storage_drive = models.ManyToManyField(StorageDrive)
    ram = models.ForeignKey('RAM', on_delete=models.SET_NULL, null=True)
    display = models.ForeignKey('Display', on_delete=models.SET_NULL, null=True)


    def display_graphics_card(self):
        return ', '.join([ GraphicsCard.model_name for GraphicsCard in self.graphics_card.all()[:4] ])
    display_graphics_card.short_description = 'Graphics card'


    def __str__(self):
        return self.brand_name + " " + self.model_name


    def get_absolute_url(self):
        return reverse('laptop-detail', args=[str(self.id)])


class Processor(models.Model):
    model_name = models.CharField(max_length=100)

    MANUFACTURER_TYPE = (
        ('AMD', 'AMD'),
        ('Intel', 'Intel'),
    )

    manufacturer = models.CharField(max_length=8, choices=MANUFACTURER_TYPE, default='Intel', blank=False, help_text='Manufacturer type')
    base_clock = models.FloatField(help_text="In GHz")
    turbo_clock = models.FloatField(help_text="In GHz")
    L3_cache = models.IntegerField(help_text="In MB")
    cores = models.IntegerField()
    threads = models.IntegerField()
    TDP = models.IntegerField(help_text="In Watts")
    manufacturing_technology = models.IntegerField(help_text="In nm")

    class Meta:
        ordering = ["model_name"]

    def get_absolute_url(self):
        return reverse('processor-detail', args=[str(self.id)])

    def __str__(self):
        return self.manufacturer + " " + self.model_name



class RAM(models.Model):

    TYPE = (
        ('DDR3', 'DDR3'),
        ('DDR4', 'DDR4'),
    )

    type = models.CharField(max_length=8, choices=TYPE, default='DDR4', blank=False, help_text='DDR3 or DDR4')
    frequency = models.IntegerField(help_text="In MHz")
    size = models.CharField(max_length=100, help_text="In MB")
    max_size = models.IntegerField(help_text="In MB")

    class Meta:
        ordering = ["size"]

    def get_absolute_url(self):
        return reverse('storage_drive-detail', args=[str(self.id)])

    def __str__(self):
        return self.type + " " + self.size + " MB"


class Display(models.Model):

    TYPE = (
        ('IPS', 'IPS'),
        ('TN', 'TN'),
    )

    type = models.CharField(max_length=8, choices=TYPE, default='IPS', blank=False, help_text='IPS or TN type of display')
    refresh_rate = models.IntegerField(help_text="In Hz")
    size = models.CharField(max_length=20, help_text="In inches")
    resolution = models.CharField(max_length=100, help_text="Horizontal on verical resolution")

    class Meta:
        ordering = ["size"]

    def get_absolute_url(self):
        return reverse('storage_drive-detail', args=[str(self.id)])

    def __str__(self):
        return self.size + " inches " + self.resolution + " px"


# Generated by Django 2.0.2 on 2018-04-23 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0012_auto_20180416_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagedrive',
            name='manufacturer',
            field=models.CharField(choices=[('Adata', 'Adata'), ('Intel', 'Intel'), ('Kingston', 'Kingston'), ('Micron', 'Micron'), ('Samsung', 'Samsung'), ('SanDisk', 'SanDisk'), ('Seagate', 'Seagate'), ('Transcend', 'Transcend'), ('WD', 'WD')], default='Samsung', help_text='Manufacturer type', max_length=8),
        ),
    ]

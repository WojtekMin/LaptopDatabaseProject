# Generated by Django 2.0.2 on 2018-05-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0013_auto_20180423_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='operating_system',
            field=models.CharField(choices=[('MacOS', 'MacOS'), ('Windows 10', 'Windows 10')], default='w', help_text='Opearating system', max_length=1),
        ),
    ]

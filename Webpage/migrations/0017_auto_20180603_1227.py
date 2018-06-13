# Generated by Django 2.0.2 on 2018-06-03 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0016_auto_20180603_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagedrive',
            name='type',
            field=models.CharField(choices=[('HDD', 'HDD'), ('SSD', 'SSD')], default='d', help_text='HDD or SSD', max_length=8),
        ),
    ]

# Generated by Django 2.0.2 on 2018-04-15 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0007_auto_20180415_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ram',
            name='size',
            field=models.CharField(help_text='In MB', max_length=100),
        ),
    ]
# Generated by Django 2.0.2 on 2018-06-16 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Webpage', '0023_auto_20180616_2209'),
    ]

    operations = [
        migrations.CreateModel(
            name='DreamLaptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.FloatField(help_text='In kg')),
                ('operating_system', models.CharField(choices=[('MacOS', 'MacOS'), ('Windows', 'Windows'), ('Linux', 'Linux')], default='Windows', help_text='Opearating system', max_length=10)),
                ('creator', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('display', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Webpage.Display')),
                ('graphics_card', models.ManyToManyField(to='Webpage.GraphicsCard')),
                ('processor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Webpage.Processor')),
                ('ram', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Webpage.RAM')),
                ('storage_drive', models.ManyToManyField(to='Webpage.StorageDrive')),
            ],
            options={
                'permissions': (('can_see_all_dream_laptops', 'See all created dream laptops'), ('can_create_dream_laptop', 'Create new dream laptop on the webpage')),
            },
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='status',
        ),
        migrations.RemoveField(
            model_name='laptop',
            name='user',
        ),
    ]
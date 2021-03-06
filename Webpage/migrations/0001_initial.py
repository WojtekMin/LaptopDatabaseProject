# Generated by Django 2.0.2 on 2018-04-15 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200)),
                ('brand_name', models.CharField(max_length=200)),
                ('dimensions', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('operating_system', models.CharField(max_length=200)),
                ('date_of_release', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('base_clock', models.FloatField(help_text='In GHz')),
                ('turbo_clock', models.FloatField(help_text='In GHz')),
                ('L3_cache', models.IntegerField(help_text='In MB')),
                ('cores', models.IntegerField()),
                ('threads', models.IntegerField()),
                ('TDP', models.IntegerField(help_text='In Watts')),
                ('manufacturing_technology', models.IntegerField(help_text='In nm')),
            ],
            options={
                'ordering': ['model_name'],
            },
        ),
        migrations.AddField(
            model_name='laptop',
            name='processor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Webpage.Processor'),
        ),
    ]

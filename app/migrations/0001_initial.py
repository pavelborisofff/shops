# Generated by Django 4.0 on 2021-12-21 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'db_table': 'cities',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_street', to='app.city')),
            ],
            options={
                'verbose_name_plural': 'Streets',
                'db_table': 'streets',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Shop ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_shop', to='app.street')),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='street_shop', to='app.street')),
            ],
            options={
                'verbose_name_plural': 'Shops',
                'db_table': 'shops',
                'ordering': ('name',),
            },
        ),
    ]

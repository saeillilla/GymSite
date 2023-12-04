# Generated by Django 4.2.7 on 2023-11-15 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Disctrict',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VEHICLE_NAME', models.CharField(max_length=20)),
                ('VEHICLE_MODEL', models.CharField(max_length=20)),
                ('VEHICLE_COLOR', models.CharField(max_length=20)),
                ('VEHICLE_MILEAGE', models.IntegerField()),
                ('VEHICLE_NUMBER', models.CharField(max_length=20)),
                ('VEHICLE_INSURANCE', models.CharField(max_length=20)),
                ('ACCIDENT_RECORD', models.CharField(max_length=20)),
                ('VEHICLE_FINE_RECORD', models.CharField(max_length=20)),
                ('photo1', models.ImageField(upload_to='static/img')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo1', models.ImageField(upload_to='static/img')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('photo3', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('photo4', models.ImageField(blank=True, null=True, upload_to='static/img')),
                ('address', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.category')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.disctrict')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

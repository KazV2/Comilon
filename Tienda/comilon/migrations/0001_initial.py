# Generated by Django 4.0.5 on 2022-07-12 18:56

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
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, null=True)),
                ('precio', models.FloatField(null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('fec_creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('proveedor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='comilon.proveedor')),
            ],
        ),
    ]
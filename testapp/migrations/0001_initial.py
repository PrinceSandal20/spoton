# Generated by Django 3.2.8 on 2022-02-07 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentIn_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product-name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, verbose_name='des')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('stock', models.PositiveIntegerField(verbose_name='stock')),
                ('available', models.BooleanField(default=True, verbose_name='available')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('date_rentIn', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

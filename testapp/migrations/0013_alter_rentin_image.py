# Generated by Django 3.2.8 on 2022-02-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0012_alter_rentin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentin',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='product/images/'),
        ),
    ]

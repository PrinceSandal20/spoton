# Generated by Django 3.2.8 on 2022-02-07 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20220207_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentin',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
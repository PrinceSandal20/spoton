# Generated by Django 3.2.8 on 2022-02-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_alter_rentin_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentin',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

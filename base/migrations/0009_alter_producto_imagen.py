# Generated by Django 4.1.6 on 2023-02-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_servicio_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, default='../base/static/img/default/', null=True, upload_to='../base/static/img/upload/'),
        ),
    ]

# Generated by Django 4.1.6 on 2023-02-03 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_pedido_productos_alter_pedido_servicios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='imagen',
            field=models.ImageField(blank=True, default='../base/static/img/default/', null=True, upload_to='../base/static/img/upload/'),
        ),
    ]

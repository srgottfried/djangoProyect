# Generated by Django 4.1.6 on 2023-02-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagen', models.ImageField(null=True, upload_to='app/static/img/')),
            ],
        ),
    ]
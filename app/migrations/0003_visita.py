# Generated by Django 5.2.1 on 2025-06-12 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_product_image_url_alter_product_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('url', models.CharField(max_length=255)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0003_rename_descripcion_gif_descripcion_gif_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='dataset_limpio',
            field=models.FileField(blank=True, null=True, upload_to='datasets/cleaned/'),
        ),
        migrations.AddField(
            model_name='proyecto',
            name='dataset_original',
            field=models.FileField(blank=True, null=True, upload_to='datasets/originals/'),
        ),
    ]

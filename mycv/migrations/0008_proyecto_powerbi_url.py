# Generated by Django 5.0.7 on 2024-07-23 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0007_alter_proyecto_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='powerbi_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

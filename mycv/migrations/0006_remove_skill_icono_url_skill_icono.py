# Generated by Django 5.0.6 on 2024-07-09 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0005_skill_proyecto_skills'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='icono_url',
        ),
        migrations.AddField(
            model_name='skill',
            name='icono',
            field=models.FileField(blank=True, null=True, upload_to='skill_icons/'),
        ),
    ]

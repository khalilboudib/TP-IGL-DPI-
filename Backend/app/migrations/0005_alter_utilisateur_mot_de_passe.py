# Generated by Django 5.0.7 on 2024-12-20 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_dpi_date_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='mot_de_passe',
            field=models.CharField(max_length=30),
        ),
    ]
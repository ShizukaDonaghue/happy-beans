# Generated by Django 3.2.18 on 2023-03-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0003_auto_20230314_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name=''),
        ),
    ]
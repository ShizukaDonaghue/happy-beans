# Generated by Django 3.2.18 on 2023-03-27 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0004_alter_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='meal',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

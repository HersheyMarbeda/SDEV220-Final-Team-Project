# Generated by Django 4.2.17 on 2024-12-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Store', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='thumbs_down',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='thumbs_up',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

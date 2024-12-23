# Generated by Django 5.1.4 on 2024-12-19 15:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_car_order_book_category_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='book',
            new_name='car',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='book',
            name='categories',
        ),
        migrations.AddField(
            model_name='book',
            name='categories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='books.category'),
            preserve_default=False,
        ),
    ]
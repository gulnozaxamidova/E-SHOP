# Generated by Django 3.2.9 on 2022-01-04 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_alter_products_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='description',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='status',
        ),
        migrations.RemoveField(
            model_name='categories',
            name='trending',
        ),
        migrations.RemoveField(
            model_name='products',
            name='meta_description',
        ),
        migrations.RemoveField(
            model_name='products',
            name='meta_keywords',
        ),
        migrations.RemoveField(
            model_name='products',
            name='meta_title',
        ),
        migrations.RemoveField(
            model_name='products',
            name='original_price',
        ),
    ]

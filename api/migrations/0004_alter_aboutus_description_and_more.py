# Generated by Django 5.1.3 on 2024-11-13 15:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_aboutus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='short_description',
            field=ckeditor.fields.RichTextField(verbose_name='Short Description'),
        ),
        migrations.AlterField(
            model_name='service',
            name='short_description',
            field=ckeditor.fields.RichTextField(verbose_name='Short Description'),
        ),
    ]

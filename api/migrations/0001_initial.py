# Generated by Django 5.1.3 on 2024-11-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Service Title')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services/', verbose_name='Service Image')),
            ],
        ),
    ]

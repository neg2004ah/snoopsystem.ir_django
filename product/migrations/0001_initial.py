# Generated by Django 4.2.2 on 2024-01-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('image1', models.ImageField(default='default.jpg', upload_to='product')),
                ('image2', models.ImageField(default='default.jpg', upload_to='product')),
                ('image3', models.ImageField(default='default.jpg', upload_to='product')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('published_date', models.DateTimeField()),
                ('category', models.ManyToManyField(to='product.category')),
            ],
            options={
                'ordering': ('-created_date',),
            },
        ),
    ]

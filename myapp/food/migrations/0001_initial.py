# Generated by Django 4.1.7 on 2023-03-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('image', models.CharField(default='https://upload.wikimedia.org/wikipedia/commons/e/e0/PlaceholderLC.png', max_length=400)),
            ],
        ),
    ]

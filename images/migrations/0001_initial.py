# Generated by Django 3.1.2 on 2021-02-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portrait', models.TextField()),
                ('image', models.ImageField(upload_to='pictures')),
            ],
        ),
    ]

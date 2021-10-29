# Generated by Django 3.2.8 on 2021-10-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LibrarySet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('author', models.CharField(max_length=100)),
                ('publication', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
    ]
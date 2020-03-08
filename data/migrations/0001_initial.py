# Generated by Django 3.0.4 on 2020-03-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Copo',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=20)),
                ('course_code', models.CharField(max_length=15)),
            ],
        ),
    ]
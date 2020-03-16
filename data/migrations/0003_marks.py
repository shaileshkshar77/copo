# Generated by Django 3.0.4 on 2020-03-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('data', '0002_delete_copo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('course_code', models.CharField(max_length=15)),
                ('usn', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('cie1', models.IntegerField()),
                ('cie2', models.IntegerField()),
                ('cie3', models.IntegerField()),
                ('quiz1', models.IntegerField()),
                ('quiz2', models.IntegerField()),
                ('quiz3', models.IntegerField()),
                ('experiental_learning', models.IntegerField()),
                ('see', models.IntegerField()),
                ('survey', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 3.2.5 on 2021-07-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('courseNumber', models.IntegerField()),
                ('instructorName', models.CharField(max_length=60)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
# Generated by Django 4.2 on 2023-05-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='id',
            field=models.AutoField(max_length=6, primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HyliApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

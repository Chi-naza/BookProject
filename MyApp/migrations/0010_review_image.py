# Generated by Django 3.2.4 on 2021-07-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0009_auto_20210712_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='bookImages/review'),
        ),
    ]

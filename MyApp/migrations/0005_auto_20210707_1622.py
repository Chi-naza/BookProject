# Generated by Django 3.2.4 on 2021-07-07 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='book_id',
            field=models.BigIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

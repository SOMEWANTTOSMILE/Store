# Generated by Django 4.2.11 on 2024-03-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cashback_points',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

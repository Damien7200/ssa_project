# Generated by Django 5.1.2 on 2024-12-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reason',
            field=models.CharField(default='None', max_length=100),
        ),
    ]

# Generated by Django 3.1.5 on 2021-01-31 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210131_0707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='choice_text',
            field=models.TextField(default=''),
        ),
    ]

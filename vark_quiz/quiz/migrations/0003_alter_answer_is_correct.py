# Generated by Django 4.2.18 on 2025-01-25 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_answer_letter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_correct',
            field=models.BooleanField(default=True),
        ),
    ]

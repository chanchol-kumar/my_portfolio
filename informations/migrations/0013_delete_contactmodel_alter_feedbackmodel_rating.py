# Generated by Django 5.0.1 on 2024-01-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0012_usercontactmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactModel',
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='rating',
            field=models.CharField(choices=[('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')], max_length=30),
        ),
    ]

# Generated by Django 4.2.3 on 2024-01-07 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0003_feedbackmodel_image_alter_feedbackmodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='image',
            field=models.ImageField(upload_to='feedback_images'),
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0002_rename_star_feedbackmodel_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='feedback_images'),
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='rating',
            field=models.CharField(blank=True, choices=[('*', '*'), ('**', '**'), ('***', '***'), ('****', '****'), ('*****', '*****')], max_length=30, null=True),
        ),
    ]
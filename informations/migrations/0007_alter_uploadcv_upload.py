# Generated by Django 4.2.3 on 2024-01-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0006_contactmodel_projectmodel_uploadcv_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcv',
            name='upload',
            field=models.FileField(upload_to='templates/cv_pdfs/'),
        ),
    ]

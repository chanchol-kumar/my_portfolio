# Generated by Django 5.0.1 on 2024-01-08 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0010_skillmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/blog_img/'),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='link_text',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]

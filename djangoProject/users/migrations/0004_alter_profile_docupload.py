# Generated by Django 3.2.5 on 2021-07-22 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_docupload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='docupload',
            field=models.FileField(upload_to='files/'),
        ),
    ]

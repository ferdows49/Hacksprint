# Generated by Django 3.0.7 on 2020-08-22 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userpanel', '0006_profile_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='userpanel/default-user.jpg', upload_to='userpanel'),
        ),
    ]
# Generated by Django 2.0.4 on 2018-04-06 20:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('nuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nftgapiuser',
            name='jwt_secret',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
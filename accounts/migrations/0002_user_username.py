# Generated by Django 3.2.3 on 2021-07-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=1, max_length=128, unique=True, verbose_name='Username'),
            preserve_default=False,
        ),
    ]

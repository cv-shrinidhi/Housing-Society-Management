# Generated by Django 2.2.5 on 2020-03-04 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
# Generated by Django 3.1 on 2020-08-26 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200826_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fetured',
            field=models.CharField(default='False', max_length=5),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='blog'),
        ),
    ]

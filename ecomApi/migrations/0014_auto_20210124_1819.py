# Generated by Django 3.1.3 on 2021-01-24 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomApi', '0013_auto_20210108_0208'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['timestamp']},
        ),
        migrations.AddField(
            model_name='product',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

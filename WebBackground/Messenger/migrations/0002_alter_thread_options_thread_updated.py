# Generated by Django 5.0.1 on 2024-01-31 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Messenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['updated']},
        ),
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
# Generated by Django 4.0.4 on 2022-06-03 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmodel', '0008_mensaje'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mensaje',
            old_name='leido',
            new_name='is_read',
        ),
        migrations.RenameField(
            model_name='mensaje',
            old_name='mensaje',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='mensaje',
            old_name='receptor',
            new_name='receiver',
        ),
        migrations.RenameField(
            model_name='mensaje',
            old_name='emisor',
            new_name='sender',
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-06 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmodel', '0010_alter_mensaje_receiver_alter_mensaje_sender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Mensaje',
        ),
    ]

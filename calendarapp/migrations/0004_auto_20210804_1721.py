# Generated by Django 3.1.12 on 2021-08-04 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_auto_20210804_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='color',
            field=models.CharField(choices=[('#FF0000', 'Rojo'), ('#0000FF', 'Azul'), ('#FFFF00', 'Amarillo'), ('#800080', 'Morado')], max_length=80),
        ),
    ]

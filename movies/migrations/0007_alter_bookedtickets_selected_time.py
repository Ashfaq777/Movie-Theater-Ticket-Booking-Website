# Generated by Django 4.0.3 on 2022-08-20 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_bookedtickets_booking_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedtickets',
            name='selected_time',
            field=models.CharField(choices=[('1', '10:00 AM'), ('2', '12:00 PM'), ('3', '2:00 PM'), ('4', '4:00 PM')], default='1', max_length=255, null=True),
        ),
    ]

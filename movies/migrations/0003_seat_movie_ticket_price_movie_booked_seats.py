# Generated by Django 4.0.3 on 2022-08-18 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_theater_theater_theater_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_no', models.IntegerField()),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=555)),
                ('purchase_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='ticket_price',
            field=models.IntegerField(default=300),
        ),
        migrations.AddField(
            model_name='movie',
            name='booked_seats',
            field=models.ManyToManyField(blank=True, to='movies.seat'),
        ),
    ]

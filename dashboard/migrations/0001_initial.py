# Generated by Django 2.1.2 on 2020-02-14 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_code', models.CharField(max_length=5)),
                ('line_name', models.CharField(max_length=20)),
                ('beg_station', models.CharField(max_length=20)),
                ('end_station', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.IntegerField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('no_of_car', models.IntegerField()),
                ('speed', models.CharField(max_length=5)),
                ('category', models.CharField(max_length=5)),
                ('days', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st_code', models.CharField(max_length=5)),
                ('st_name', models.CharField(max_length=20)),
                ('line_code', models.ManyToManyField(to='dashboard.Line')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='route_end',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dest_station', to='dashboard.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='route_line',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Line'),
        ),
        migrations.AddField(
            model_name='route',
            name='route_start',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source_station', to='dashboard.Station'),
        ),
        migrations.AddField(
            model_name='route',
            name='stops',
            field=models.ManyToManyField(to='dashboard.Station'),
        ),
    ]
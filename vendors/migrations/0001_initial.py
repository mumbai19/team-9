# Generated by Django 2.2.3 on 2019-07-20 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SeedsProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_name', models.CharField(max_length=100)),
                ('seed_name', models.CharField(max_length=100)),
                ('exweather', models.TextField()),
                ('exph', models.FloatField()),
                ('price', models.FloatField()),
            ],
        ),
    ]

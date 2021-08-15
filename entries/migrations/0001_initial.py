# Generated by Django 2.2.24 on 2021-08-15 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_title', models.CharField(max_length=255)),
                ('trophy_names', models.TextField()),
                ('is_winner', models.BooleanField()),
                ('audience_honor', models.BooleanField()),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('street_address', models.TextField()),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zipcode', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('is_individual', models.BooleanField()),
                ('is_organization', models.BooleanField()),
                ('company', models.CharField(max_length=255)),
            ],
        ),
    ]

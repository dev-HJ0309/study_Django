# Generated by Django 4.2.4 on 2023-08-02 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_email', models.CharField(max_length=50, unique=True)),
                ('member_password', models.CharField(max_length=50)),
                ('member_name', models.TextField(blank=True)),
                ('member_age', models.PositiveSmallIntegerField(default=0)),
                ('member_status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_member',
            },
        ),
    ]
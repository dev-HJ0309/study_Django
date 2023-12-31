# Generated by Django 4.2.4 on 2023-08-02 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=50, unique=True)),
                ('post_content', models.TextField(blank=True)),
                ('post_status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tbl_post',
            },
        ),
    ]

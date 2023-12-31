# Generated by Django 4.2.4 on 2023-08-04 16:24

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
                ('create_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('post_title', models.CharField(blank=True, max_length=200)),
                ('post_content', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'tbl_post',
                'ordering': ['-id'],
            },
        ),
    ]

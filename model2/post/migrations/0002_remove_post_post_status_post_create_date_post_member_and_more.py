# Generated by Django 4.2.4 on 2023-08-03 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_options_member_create_date_and_more'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_status',
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.member'),
        ),
        migrations.AddField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_title',
            field=models.CharField(max_length=50),
        ),
    ]

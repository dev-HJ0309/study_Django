# Generated by Django 4.2.4 on 2023-08-03 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_options_member_create_date_and_more'),
        ('post', '0002_remove_post_post_status_post_create_date_post_member_and_more'),
        ('reply', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='reply_title',
        ),
        migrations.AddField(
            model_name='reply',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.member'),
        ),
        migrations.AddField(
            model_name='reply',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='post.post'),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_depth',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='reply_group_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='reply',
            name='update_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='reply',
            name='reply_status',
            field=models.CharField(choices=[('Y', '일반 댓글'), ('N', '비밀 댓글')], default='Y', max_length=1),
        ),
    ]

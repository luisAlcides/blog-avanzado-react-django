# Generated by Django 4.2.1 on 2023-05-28 15:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_id_alter_post_blog_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='blog_uuid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
# Generated by Django 2.2.3 on 2022-12-31 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0010_alter_post_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

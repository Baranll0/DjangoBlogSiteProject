# Generated by Django 4.1 on 2022-10-23 12:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0008_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=50000),
        ),
    ]
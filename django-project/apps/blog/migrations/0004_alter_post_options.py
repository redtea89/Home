# Generated by Django 4.0.4 on 2022-06-12 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['updated_at']},
        ),
    ]

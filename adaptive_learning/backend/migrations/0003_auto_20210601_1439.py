# Generated by Django 3.1.5 on 2021-06-01 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_add_root_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]

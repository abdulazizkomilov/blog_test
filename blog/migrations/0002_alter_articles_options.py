# Generated by Django 4.1.7 on 2023-03-24 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('title',), 'verbose_name': 'Maqola', 'verbose_name_plural': 'Maqolalar'},
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='description',
            field=models.CharField(blank=True, default='none', max_length=300),
        ),
    ]

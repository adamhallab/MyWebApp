# Generated by Django 3.1.7 on 2021-04-02 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210402_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacation', to=settings.AUTH_USER_MODEL),
        ),
    ]

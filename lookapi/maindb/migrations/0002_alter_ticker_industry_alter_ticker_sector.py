# Generated by Django 4.0.1 on 2022-01-12 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maindb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticker',
            name='industry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maindb.industry'),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maindb.sector'),
        ),
    ]
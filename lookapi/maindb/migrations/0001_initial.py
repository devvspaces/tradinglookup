# Generated by Django 4.0.1 on 2022-01-11 18:13

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('ticker', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('featured_image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('market_cap', models.PositiveBigIntegerField()),
                ('dividend', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ceo', models.CharField(max_length=30, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('employees', models.BigIntegerField(null=True)),
                ('location', models.CharField(max_length=80, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('industry', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='maindb.industry')),
                ('sector', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='maindb.sector')),
            ],
        ),
    ]

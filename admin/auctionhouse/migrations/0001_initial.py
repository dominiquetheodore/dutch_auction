# Generated by Django 3.1.3 on 2021-09-06 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('startBid', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.CharField(max_length=250)),
                ('imageUrl', models.URLField(blank=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('bidValue', models.DecimalField(decimal_places=2, max_digits=7)),
                ('auctionListing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionhouse.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionhouse.user')),
            ],
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctionhouse.user'),
        ),
    ]
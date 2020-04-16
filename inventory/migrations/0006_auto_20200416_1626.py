# Generated by Django 3.0.5 on 2020-04-16 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_remove_donor_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemdonated',
            name='price',
        ),
        migrations.CreateModel(
            name='RecordDonation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
                ('notes', models.TextField(max_length=150)),
                ('record_donation', models.DateField()),
                ('itemdonated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.ItemDonated')),
            ],
        ),
        migrations.CreateModel(
            name='HospitalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('serial_number', models.CharField(max_length=150)),
                ('quantity', models.CharField(max_length=150)),
                ('notes', models.TextField(max_length=150)),
                ('itemdonated', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.ItemDonated')),
            ],
        ),
    ]

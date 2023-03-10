# Generated by Django 4.0.6 on 2022-12-19 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('address1', models.CharField(blank=True, max_length=32, null=True)),
                ('address2', models.CharField(blank=True, max_length=32, null=True)),
                ('city', models.CharField(blank=True, max_length=32, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=8, null=True)),
                ('phone_number1', models.CharField(blank=True, max_length=32, null=True)),
                ('phone_number2', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(max_length=32)),
                ('sin', models.CharField(max_length=32)),
                ('dob', models.DateField()),
                ('agent', models.CharField(blank=True, max_length=32, null=True)),
                ('collection_amount', models.FloatField(blank=True, null=True)),
                ('collection_date', models.DateField(blank=True, null=True)),
                ('last_agent', models.CharField(blank=True, max_length=32, null=True)),
                ('last_crawl', models.DateTimeField(blank=True, null=True)),
                ('last_result', models.CharField(blank=True, max_length=32, null=True)),
                ('prioritize_local', models.BooleanField(blank=True, null=True)),
                ('prioritize_global', models.BooleanField(blank=True, null=True)),
                ('file_upload', models.FileField(blank=True, null=True, upload_to='')),
                ('province', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='main.province')),
            ],
        ),
    ]

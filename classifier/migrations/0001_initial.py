# Generated by Django 5.0.4 on 2024-05-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('file', models.FileField(upload_to='models/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
    ]

# Generated by Django 5.1.4 on 2024-12-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password_one', models.CharField(max_length=128)),
                ('password_two', models.CharField(max_length=128)),
            ],
        ),
    ]
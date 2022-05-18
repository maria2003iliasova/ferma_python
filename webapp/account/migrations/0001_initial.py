# Generated by Django 4.0.4 on 2022-05-18 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('time_create', models.DateField()),
                ('time_update', models.DateField()),
                ('is_published', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_create', models.DateField()),
                ('time_update', models.DateField()),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.articles')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.CreateModel(
            name='Bron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_date', models.DateField()),
                ('departure_date', models.DateField()),
                ('adults_count', models.IntegerField()),
                ('children_count', models.IntegerField()),
                ('pets_count', models.IntegerField()),
                ('info', models.BooleanField()),
                ('house_count', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user'),
        ),
    ]
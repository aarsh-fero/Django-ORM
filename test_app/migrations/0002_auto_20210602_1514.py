# Generated by Django 3.0.5 on 2021-06-02 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book_author', to='test_app.Author'),
        ),
    ]
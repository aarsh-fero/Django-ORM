# Generated by Django 3.0.5 on 2021-06-02 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveSmallIntegerField()),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books_added', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'default_related_name': 'books',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(choices=[('Ahmedabad', 'Ahmedabad'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Kolkata', 'Kolkata'), ('Chennai', 'Chennai'), ('Banglore', 'Banglore'), ('Pune', 'Pune'), ('Hyderabad', 'Hyderabad'), ('Jaipur', 'Jaipur'), ('Jodhpur', 'Jodhpur')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(choices=[('Ahmedabad', 'Ahmedabad'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Kolkata', 'Kolkata'), ('Chennai', 'Chennai'), ('Banglore', 'Banglore'), ('Pune', 'Pune'), ('Hyderabad', 'Hyderabad'), ('Jaipur', 'Jaipur'), ('Jodhpur', 'Jodhpur')], max_length=25)),
                ('books', models.ManyToManyField(related_name='stores', to='test_app.Book')),
            ],
            options={
                'default_related_name': 'stores',
            },
        ),
        migrations.CreateModel(
            name='PagesWritten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pages_written', models.IntegerField()),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='author_wrote', to='test_app.Author')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books_written', to='test_app.Book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='book_author', through='test_app.PagesWritten', to='test_app.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='book_genre', to='test_app.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='test_app.Publisher'),
        ),
        migrations.AddField(
            model_name='book',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books_updated', to=settings.AUTH_USER_MODEL),
        ),
    ]

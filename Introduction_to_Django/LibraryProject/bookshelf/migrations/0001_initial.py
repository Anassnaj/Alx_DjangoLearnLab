<<<<<<< HEAD
# Generated by Django 5.1.2 on 2024-10-31 10:10
=======
<<<<<<< HEAD
# Generated by Django 5.0.8 on 2024-08-16 13:38
=======
# Generated by Django 5.1.2 on 2024-11-02 13:05
>>>>>>> origin/master
>>>>>>> 16dee7aeb905a470e30d02d3bea5cea76272bc25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publication_year', models.IntegerField()),
            ],
        ),
    ]

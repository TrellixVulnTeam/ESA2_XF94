# Generated by Django 2.1.4 on 2018-12-14 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belegungen', '0003_studierendenliste'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='lv',
        ),
        migrations.AddField(
            model_name='lehrveranstaltung',
            name='stud',
            field=models.ManyToManyField(to='belegungen.Student'),
        ),
    ]
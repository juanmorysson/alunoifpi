# Generated by Django 2.0.13 on 2020-05-24 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='photo',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]

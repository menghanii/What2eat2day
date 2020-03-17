# Generated by Django 3.0.4 on 2020-03-17 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200317_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image_3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='image_4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='bulletin',
            field=models.CharField(choices=[('2', '신촌 밖'), ('1', '신촌 안')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='menu',
            field=models.CharField(choices=[('cp', '치킨&피자&햄버거'), ('jp', '일식'), ('bo', '분식'), ('ch', '중식'), ('ko', '한식'), ('nh', '야식'), ('et', '기타')], max_length=100),
        ),
    ]

# Generated by Django 3.2.11 on 2023-02-17 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('View', '0009_auto_20230217_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details3_1_1',
            name='Uploaded_by',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='details3_2_2',
            name='Uploaded_by',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='details3_3_1',
            name='Uploaded_by',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='details3_3_2',
            name='Uploaded_by',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='details3_4_3',
            name='Uploaded_by',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='details3_5_1',
            name='Uploaded_by',
            field=models.CharField(default=0, max_length=50),
        ),
    ]

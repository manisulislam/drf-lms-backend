# Generated by Django 4.2.7 on 2024-02-22 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name_plural': '3.Courses'},
        ),
        migrations.AlterModelOptions(
            name='coursecategory',
            options={'verbose_name_plural': '2.Course Category'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name_plural': '4.Students'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name_plural': '1.Teachers'},
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main.coursecategory'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='main.teacher'),
        ),
    ]
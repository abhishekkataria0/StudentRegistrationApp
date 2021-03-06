# Generated by Django 2.0.6 on 2018-08-23 12:29

from django.db import migrations, models
import student.models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0020_auto_20180823_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_form5',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student_form4',
            name='tenth_marksheet',
        ),
        migrations.RemoveField(
            model_name='student_form4',
            name='twelfth_marksheet',
        ),
        migrations.AddField(
            model_name='student_form2',
            name='tenth_marksheet',
            field=models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='student_form3',
            name='twelfth_marksheet',
            field=models.FileField(blank=True, null=True, upload_to=student.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='student_form4',
            name='candidate_photo',
            field=models.ImageField(blank=True, null=True, upload_to=student.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='student_form4',
            name='signature_photo',
            field=models.ImageField(blank=True, null=True, upload_to=student.models.user_directory_path),
        ),
        migrations.AddField(
            model_name='student_form4',
            name='thumb_photo',
            field=models.ImageField(blank=True, null=True, upload_to=student.models.user_directory_path),
        ),
        migrations.DeleteModel(
            name='Student_form5',
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-30 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_createnoteform_delete_note'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CreateNoteForm',
            new_name='CreateNote',
        ),
    ]
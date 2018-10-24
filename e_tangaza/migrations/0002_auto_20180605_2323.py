# Generated by Django 2.0.3 on 2018-06-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_tangaza', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='Category',
            field=models.CharField(choices=[('on_sale', 'on_sale'), ('found', 'found'), ('announcement', 'announcement'), ('event', 'event'), ('lost', 'lost')], default='announcement', help_text='The category of the announcement', max_length=20),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='Icon',
            field=models.FileField(upload_to='announcement-icon'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='Type',
            field=models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('rejected', 'rejected')], default='pending', help_text='The type of the announcement. This is whether it is rejected, approved, or pending', max_length=20),
        ),
    ]
# Generated by Django 3.0.3 on 2020-06-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicines',
            name='Tablet_or_Syrup',
            field=models.CharField(choices=[('Cap', 'Capsule'), ('Syr', 'Syrup'), ('Tab', 'Tablet'), ('Susp', 'Susp'), ('Oint', 'Ointment'), ('Drop', 'Drop'), ('Pow', 'Powder'), ('O', 'Other')], max_length=5),
        ),
    ]

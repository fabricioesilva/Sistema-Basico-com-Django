# Generated by Django 4.2.1 on 2023-05-21 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_customuser_user_since_alter_deleteduser_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremailcheck',
            name='confirmed',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data da confimação'),
        ),
    ]

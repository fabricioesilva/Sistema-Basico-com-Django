# Generated by Django 4.2.1 on 2023-05-20 22:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_delete_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Insira o telefone para contaco com Whatsapp. Ex:(99)999999999.', max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='O telefone para contato precisa         ser incerido com o DDD e os nove dígitos.', regex='\\d{11}$')], verbose_name='Telefone para contato'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_since',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Usuário desde'),
        ),
        migrations.AlterField(
            model_name='deleteduser',
            name='user_since',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Usuário desde'),
        ),
        migrations.AlterField(
            model_name='usermessages',
            name='to_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='receiver', to=settings.AUTH_USER_MODEL, verbose_name='Usuário que recebeu'),
        ),
    ]
# Generated by Django 4.1.3 on 2022-12-13 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=64, null=True)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=64, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('citizenship', models.CharField(blank=True, max_length=64, null=True)),
                ('passport', models.CharField(blank=True, max_length=64, null=True)),
                ('individual_identification_number', models.CharField(blank=True, max_length=64, null=True)),
                ('place_of_birthday', models.CharField(blank=True, max_length=128, null=True)),
                ('place_of_living', models.CharField(blank=True, max_length=128, null=True)),
                ('range', models.CharField(blank=True, max_length=64, null=True)),
                ('military_unit', models.CharField(blank=True, max_length=64, null=True)),
                ('military_from', models.CharField(blank=True, max_length=64, null=True)),
                ('place_where_die', models.CharField(blank=True, max_length=64, null=True)),
                ('data_when_die', models.DateField(blank=True, default=None, null=True)),
                ('status_person', models.CharField(choices=[('ALIVE', 'Alive'), ('CAPTIVITY', 'Captivity'), ('DIE', 'Die'), ('MISSING_PERSON', 'Missing person')], default='DIE', max_length=32)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('post_status', models.CharField(choices=[('DELETED', 'Deleted'), ('PUBLISHED', 'Published'), ('PROCESSING', 'Processing')], default='PROCESSING', max_length=32)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='PersonTypeSocialNetworkChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_from', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=8192)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diap.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonSocialNetwork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=128)),
                ('profile_name', models.CharField(max_length=64, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diap.person')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diap.persontypesocialnetworkchoices')),
            ],
        ),
        migrations.CreateModel(
            name='PersonPlaceWhereHeWas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=128)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diap.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diap.person')),
            ],
        ),
    ]

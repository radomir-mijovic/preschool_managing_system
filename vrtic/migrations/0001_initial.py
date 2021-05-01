# Generated by Django 3.2 on 2021-04-23 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Kids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('city_birthday', models.CharField(blank=True, max_length=100, null=True)),
                ('custom_id', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, choices=[('muski', 'Muski'), ('zenski', 'Zenski')], max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_phone', models.CharField(blank=True, max_length=100, null=True)),
                ('family_size', models.IntegerField(blank=True, null=True)),
                ('living_with', models.CharField(blank=True, choices=[('oba roditelja', 'Oba roditelja'), ('jednim roditeljem', 'Jednim roditeljem'), ('bez roditelja', 'Bez roditelja')], max_length=100, null=True)),
                ('number_of_preschool_kids_in_family', models.IntegerField(blank=True, null=True)),
                ('kid_already_been_in_kindergarten', models.CharField(blank=True, choices=[('da', 'Da'), ('ne', 'Ne')], default=False, max_length=100, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('father_education_level', models.CharField(blank=True, max_length=200, null=True)),
                ('father_company', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mother_education_level', models.CharField(blank=True, max_length=200, null=True)),
                ('mother_company', models.CharField(blank=True, max_length=200, null=True)),
                ('parent_notes', models.CharField(blank=True, max_length=500, null=True)),
                ('program_choice', models.CharField(blank=True, choices=[('primarni program', 'Primarni program'), ('kraci program', 'Kraci program')], max_length=100, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vrtic.group')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('date_of_birth', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=80, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vrtic.group')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_paper_id', models.IntegerField(blank=True, null=True)),
                ('payment_date', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.FloatField(blank=True, null=True)),
                ('need_to_pay', models.FloatField(blank=True, null=True)),
                ('notes', models.CharField(blank=True, max_length=500, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vrtic.kids')),
            ],
            options={
                'ordering': ['bank_paper_id'],
            },
        ),
    ]

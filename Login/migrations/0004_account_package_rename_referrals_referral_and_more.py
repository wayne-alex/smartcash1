# Generated by Django 4.2.3 on 2023-07-16 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_rename_user_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account_balance', models.IntegerField()),
                ('referral_balance', models.IntegerField()),
                ('views_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('package_type', models.CharField(max_length=10)),
                ('due_date', models.DateField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Referrals',
            new_name='Referral',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.RenameField(
            model_name='referral',
            old_name='user2_id',
            new_name='referrer_id',
        ),
        migrations.AddField(
            model_name='deposit',
            name='type',
            field=models.CharField(default='Buy', max_length=10),
        ),
    ]

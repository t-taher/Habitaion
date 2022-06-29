# Generated by Django 3.2.12 on 2022-06-29 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ads', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='type',
            field=models.CharField(choices=[('Apartment', 'Apartment'), ('Villa', 'Villa'), ('Studio', 'Studio'), ('Room', 'Room'), ('Home', 'Home'), ('Hotel', 'Hotel'), ('Apartment', 'Apartment'), ('Office', 'Office'), ('Flat', 'Flat'), ('Palace', 'Palace')], max_length=10),
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ad')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

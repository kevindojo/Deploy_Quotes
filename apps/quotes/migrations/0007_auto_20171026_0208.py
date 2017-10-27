# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-26 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0006_remove_quote_userkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='favorite',
            field=models.ManyToManyField(null=True, related_name='quote_favor', to='quotes.User'),
        ),
        migrations.AddField(
            model_name='quote',
            name='user_upload',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_quote', to='quotes.User'),
        ),
    ]
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Option(models.Model):
	option = models.TextField()

class MenuOption(models.Model):
	image =  models.ImageField(upload_to='static/img')
	name = models.TextField()
	description = models.TextField()
	price = models.FloatField()
	types = models.ForeignKey(Option)


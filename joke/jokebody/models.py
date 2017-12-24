# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class JokeType(models.Model):
    type = models.CharField(max_length=30)

    class Meta:
        db_table = "pre_wuxin_service_joketype"


class JokeBody(models.Model):
    content=models.TextField()
    title=models.CharField(max_length=30)
    dateandtime =models.DateField()
    type=models.ForeignKey(JokeType,db_column="typeid")

    class Meta:
        db_table = "pre_wuxin_service_joke"

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=32,default='title')
    content = models.TextField(null=True)
    feedback = models.TextField(null=True)

    def __unicode__(self):
        return self.title


class VisitRecord(models.Model):
    user_id = models.CharField(max_length=64,default='0')
    bkj_id = models.CharField(max_length=64,default='0')
    time_stamp = models.CharField(max_length=64,default='0')
    is_crawler = models.CharField(max_length=32,default='0')
    visit_freq = models.CharField(max_length=64,default='0')
    visit_times = models.IntegerField(null=True)
    reverse_deta = models.CharField(max_length=64,default='0')  # 1/(a2-a1)
    serially = models.IntegerField(null=True)
    update_stamp = models.TimeField(null=True)
    def __unicode__(self):
        return self.user_id

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from ml.preprocess import features
from numpy import *

import jc.models as models
from jc.baoer.baoer import baoer
from ml.preprocess.modeling import modeling as modeling
from ml.preprocess.data_clean import data_clean
from ml.preprocess.mining import mining
from ml.preprocess.data_flow import data_flow
from ml.preprocess.mysql_process_unit import mysql_process_unit


# Create your views here.


def index(request):

    cf1 = [];cf2 = [];bf1 = [];bf2 = [];output = []
    ret = {'cf1': cf1, 'cf2': cf2, 'bf1': bf1, 'bf2': bf2}
    return render(request, 'jc/index.html', {'ret': ret})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'jc/article_page.html', {'article': article})


def edited_page(request, edited_id):
    return render(request, 'jc/edited_page.html')


def add_visit_record(request, user_id, bkj_id, time_stamp):
    md = modeling(['id', 'time_stamp'], 'jc_visitrecord',
                  'where user_id = ' + user_id ,' order by time_stamp desc')
    _, resaults = md.getDataSet()
    if len(resaults) != 0:
        models.VisitRecord.objects.create(user_id=user_id,
                                          bkj_id=bkj_id,
                                          time_stamp=time_stamp,
                                          reverse_deta=1000 / abs(float(time_stamp) - float(resaults[0].time_stamp)))
    else:
        models.VisitRecord.objects.create(user_id=user_id,
                                          bkj_id=bkj_id,
                                          time_stamp=time_stamp,
                                          reverse_deta=0)

    return render(request, 'jc/add_visit_record.html')


def show_visit_record(request):
    records = models.VisitRecord.objects.all()
    return render(request, 'jc/show_visit_record.html', {'records': records})

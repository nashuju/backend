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
import datetime
import enchant
from ao.EN2CHS import EN2CHS
import ao.baiduTranslateApi as bdt
from django.http import HttpResponse
import json
from django.core import serializers
import ao.record_rules as rr


# Create your views here.


def index(request):
    cf1 = [];
    cf2 = [];
    bf1 = [];
    bf2 = [];
    output = []
    ret = {'cf1': cf1, 'cf2': cf2, 'bf1': bf1, 'bf2': bf2}
    return render(request, 'jc/index.html', {'ret': ret})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'jc/article_page.html', {'article': article})


def edited_page(request, edited_id):
    return render(request, 'jc/edited_page.html')


def add_visit_record(request, user_id, content):
    time_stamp = datetime.datetime.now()
    #if " " not in content:
        # r = EN2CHS(content)
    word, add_content = rr.RecordRules(content).en_zh()
    if add_content != "":
        content = word
    w, r, tp = bdt.all2ZH(content)
    if w != None:
        records = models.VisitRecord.objects.filter(bkj_id=w)
        if records.__len__() != 0:
            models.VisitRecord.objects.filter(bkj_id=w).update(
                visit_freq=str(int(records[0].visit_freq) + 1),
                time_stamp=time_stamp,
                reverse_deta=records[0].reverse_deta if add_content in records[0].reverse_deta else records[0].reverse_deta+add_content
            )
        elif tp != "unknown2zh" and r != content and r != "" and records.__len__() == 0:
            models.VisitRecord.objects.create(user_id=user_id,
                                              bkj_id=w,
                                              time_stamp=time_stamp,
                                              reverse_deta=r if add_content in r else r+add_content,
                                              is_crawler=tp
                                              )
    return render(request, 'jc/add_visit_record.html')


def show_visit_record(request, user_id):
    records = models.VisitRecord.objects.filter(user_id=user_id).order_by('-time_stamp')[:20]
    return render(request, 'jc/show_visit_record.html', {'records': records, 'first': records[0]})


def mz(request, user_id):
    records = models.VisitRecord.objects.filter(user_id=user_id).order_by('-time_stamp')
    return render(request, 'jc/mz.html', {'records': records, 'first': records[0]})


def record_json(request, user_id):
    records = models.VisitRecord.objects.filter(user_id=user_id).order_by('-time_stamp')[:10]
    data = serializers.serialize("json", records)
    return HttpResponse(json.dumps({'records': json.loads(data)[0]}), content_type="application/json")

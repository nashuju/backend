from django.conf.urls import url
from django.contrib import admin
import jc.views as views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_page,name='article_page'),
    url(r'^edited_page/(?P<edited_id>[0-9]+)$', views.edited_page,name='edited_page'),
#   url(r'^visit/(?P<user_id>[0-9]+)/(?P<bkj_id>[0-9]+)$', views.add_visit_record,name='add_visit_record'),
    url(r'^visit/(?P<user_id>[\s\S]*)/(?P<content>[\s\S]*)$', views.add_visit_record,name='add_visit_record'),
    url(r'^show/(?P<user_id>[\s\S]*)$', views.show_visit_record,name='show_visit_record'),
    url(r'^show_json/(?P<user_id>[\s\S]*)$', views.record_json,name='record_json'),
    url(r'^mz/(?P<user_id>[\s\S]*)$', views.mz,name='mz'),

]


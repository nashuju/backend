# -*- coding: utf-8 -*-

from ml.preprocess.mining import mining
from ml.preprocess.modeling import modeling
from ml.preprocess.data_clean import data_clean
from ml.preprocess.mining import mining
from ml.preprocess.data_flow import data_flow
from ml.preprocess.mysql_process_unit import mysql_process_unit
from django.db import connection
import jc.models as models
import json
import csv
import codecs
import datetime
import time
import sys
from django.conf import settings
from django.core.cache import cache

reload(sys)
sys.setdefaultencoding('utf8')


class baoer(mining):
    bkj_id = 0

    frq = 0
    bkj_serially = {}
    ret = {}
    t_f = []
    t_b = []
    ret2csv = []

    def __init__(self):
        self.frq = 0
        self.bkj_serially = {}
        self.ret = {}
        self.t_b = []
        self.t_f = []


    #read cache user id
    def read_from_cache(self, key):
        value = cache.get(key)
        if value == None:
            data = None
        else:
            data = json.loads(value)
        return data

    #write cache user id
    def write_to_cache(self, key,value):
        cache.set(key, json.dumps(value), settings.NEVER_REDIS_TIMEOUT)

    def delete_old_data(self,days):
        now_time = datetime.datetime.now()
        yes_time = now_time + datetime.timedelta(days)
        days_before = str(time.mktime(yes_time.timetuple()))[:-2] + "000"
        with connection.cursor() as cursor:
            cursor.execute('delete from jc_visitrecord where time_stamp < ' + days_before)
            row = cursor.fetchone()
        return row

    def find_serially(self, data_flow):

        if data_flow.is_row_num_change:

            if data_flow.latest_row[0] in self.ret:
                self.ret[data_flow.latest_row[0]][4] += 1
                try:
                    self.ret[data_flow.latest_row[0]][3] = float(data_flow.latest_row[3]) + float(
                        self.ret[data_flow.latest_row[0]][3])
                except:
                    #print (self.ret[data_flow.latest_row[0]])
                    pass
                if abs(int(self.ret[data_flow.latest_row[0]][1]) - int(
                        self.bkj_serially[data_flow.latest_row[0]][0])) == 1:
                    self.bkj_serially[data_flow.latest_row[0]][1] += 300
                elif int(self.ret[data_flow.latest_row[0]][1]) - int(
                        self.bkj_serially[data_flow.latest_row[0]][0])==0:
                    self.bkj_serially[data_flow.latest_row[0]][1] += 30
                self.bkj_serially[data_flow.latest_row[0]][0] = data_flow.latest_row[1]


            else:
                data_flow.latest_row.append(1)
                self.ret[data_flow.latest_row[0]] = data_flow.latest_row
                self.bkj_serially[data_flow.latest_row[0]] = [data_flow.latest_row[1]]
                self.bkj_serially[data_flow.latest_row[0]].append(0)

        return data_flow

    def output2csv(self, name, table, tableName=None):
        with codecs.open(name, "w+", "utf_8_sig") as csvfile:
            cfile = csv.writer(csvfile, dialect="excel")
            if tableName != None:
                cfile.writerow(tableName)
            for row in table:
                cfile.writerow(row)

    def run(self):

        now_time = datetime.datetime.now()
        today = datetime.datetime.today()
        today_zero = datetime.datetime(today.year,today.month,today.day,0,0,0)
        yes_time = now_time + datetime.timedelta(days=-7)
        before_n_days = str(time.mktime(yes_time.timetuple()))[:-2] + "000"
        yestoday_str = str(time.mktime((today_zero+ datetime.timedelta(days=-1)).timetuple()) )[:-2] + "000"
        the_day_before_yestoday = str(time.mktime((today_zero+ datetime.timedelta(days=-2)).timetuple()))[:-2] + "000"

        md = modeling(['id', 'user_id', 'bkj_id', 'time_stamp', 'reverse_deta'],
                      "jc_visitrecord", "where id !=0 and time_stamp > " + before_n_days,
                      " ORDER BY time_stamp desc limit 10000")
        bkj_md = modeling(['id', 'bkj_id', 'count(bkj_id) as num'],
                      "jc_visitrecord", "where id !=0 and time_stamp > "
                          + the_day_before_yestoday
                          +" and time_stamp < "
                          + yestoday_str,
                      " GROUP BY bkj_id ORDER BY count(bkj_id) desc limit 20")
        bkj_ids,_ = bkj_md.getDataSet(['bkj_id','num'])
        userId_md = modeling(['id', 'user_id', 'count(user_id) as num'],
                      "jc_visitrecord", "where id !=0 and time_stamp > "
                          + the_day_before_yestoday
                          +" and time_stamp < "
                          + yestoday_str,
                      " GROUP BY user_id ORDER BY count(user_id) desc limit 20")
        user_ids,_ = userId_md.getDataSet(['user_id','num'])
        high_frq = modeling(["id", "user_id",
                             "bkj_id",
                             "sum(round(reverse_deta)) as freq",
                             "FROM_UNIXTIME(time_stamp/1000,'%%Y-%%m-%%d %%H:%%i:%%s') as ftime "],

                            "jc_visitrecord", "where id !=0 "
                                              "and FROM_UNIXTIME(time_stamp/1000,'%%H:%%i:%%s') > '00:00:00' "
                                              "and FROM_UNIXTIME(time_stamp/1000,'%%H:%%i:%%s') < '23:59:59' "
                                              "AND time_stamp >" + before_n_days,

                            " GROUP BY user_id  ORDER BY sum(round(reverse_deta)) desc limit 20"
                            )
        high_visit = modeling(["id", "user_id",
                               "bkj_id",
                               "count(id) as numberoftimes",
                               "sum(round(reverse_deta)) as freq",
                               "FROM_UNIXTIME(time_stamp/1000,'%%Y-%%m-%%d %%H:%%i:%%s') as ftime "],

                              "jc_visitrecord", "where id !=0 "
                                                "and FROM_UNIXTIME(time_stamp/1000,'%%H:%%i:%%s') > '00:00:00' "
                                                "and FROM_UNIXTIME(time_stamp/1000,'%%H:%%i:%%s') < '23:59:59' "
                                                "AND time_stamp >" + before_n_days,

                              " GROUP BY user_id  ORDER BY count(id)  desc limit 20"
                              )

        # mpu = mysql_process_unit(md)
        # mpu.run()
        # data = mpu.get_data_set()               # 添加结束判断标准

        dc = data_clean()
        md.set_fieldPreProcess_func(dc.removeIdField)  # 数据预处理
        md.set_mining_func(self.find_serially)  # 数据特征处理
        md.getDataSet()  # 执行数据分析

        for x in self.ret.keys():
            try:
                self.t_f.append([float(list(self.ret[x])[4]), float(list(self.ret[x])[3])])
                self.t_b.append([float(list(self.bkj_serially[x])[1]), float(list(self.ret[x])[3])])
                self.ret2csv.append(self.ret[x])
            except:
                #print (self.ret[x])
                pass

        # freqSet =  self.read_from_cache("freqSet")
        # visitSet =  self.read_from_cache("visitSet")
        # if freqSet != None:pass
        # else:
        freqSet, result = high_frq.getDataSet(["user_id", "bkj_id", "freq", "ftime"])

        # if visitSet != None:pass
        # else:
        visitSet, visit_resault = high_visit.getDataSet(["user_id", "bkj_id", "numberoftimes", "ftime"])
        self.write_to_cache("freqSet",freqSet)
        self.write_to_cache("visitSet",visitSet)
        pass



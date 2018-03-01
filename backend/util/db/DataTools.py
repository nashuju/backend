# -*- coding: utf-8 -*-
from src.db.DB import DB
import pandas as pd
class DataTools:

    db = None
    def __init__(self):
        try:
            self.db = DB("mysql","10.20.2.26", "root", "123456", "modeling")
        except:
            self.db = DB("mysql","localhost", "root", "123456", "modeling")

    def get_tablename(self,share_num):
        table = "000001"
        table_frame = self.get_data_frame_from_sql("\
                      select table_name from information_schema.tables where table_schema='modeling'\
                      ")
        for t in table_frame['table_name']:
            if share_num >= t : table = t;continue;
            else: break
        return table

    def get_fixed_share(self,share_num):
        table = self.get_tablename(share_num)
        sql  = "select a.id as id ,a.date as `date`, a.seqNo as `seqNo` ,a.open*b.weight as `open`, \
                  a.close*b.weight as `close`,a.high*b.weight as `high`,a.low*b.weight as `low`\
                  ,a.volume as volume,a.amount*b.weight as amount from  \
                  ((select * FROM `"+table+"` where `"+table+"`.share_num = '"+share_num+"' )as a ),\
                  (\
                    (SELECT * from `weight` where `weight`.share_num = '"+share_num+"') as b\
                  )\
                  where a.date = b.date and a.share_num = b.share_num"
        return  pd.read_sql(sql,self.db.engine,index_col='id')

    def get_data_frame_from_sql(self,sql):
        return pd.read_sql(sql,self.db.engine)

# demo
# from src.db.File import File
# dt = DataTools()
# f = File("../../data")
# for file_name in f.get_file_names_without_suffix_in_current_dir():
#     if file_name != '300516':continue
#     dt.get_fixed_share(file_name).to_csv("../../result/"+file_name+".csv")
#     print (file_name)


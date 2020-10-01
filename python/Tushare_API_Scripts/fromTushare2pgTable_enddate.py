#!/usr/bin/python
# -*- coding: utf-8 -*-
# Time    : 2020-09-06 
# Author  : zzg
# Describe: from Tushare get api datas then create and insert into a pg table
# change  :

import sys
ApiName = sys.argv[1]
Indate = sys.argv[2]

def fromTushare2pgTable(api_name, dt):
    import pandas as pd
    import tushare as ts
    from sqlalchemy import create_engine

    pro = ts.pro_api('d4f88683d4244be4c66d0e3d39324b6e519f4e2807a8b01894480159')
    engine = create_engine('postgresql://postgres:ican00@127.0.0.1:5432/stockam')
    
    data = pro.query(api_name, end_date=dt)
    pd.io.sql.to_sql(data, api_name, engine,index= False, schema='ods',if_exists='append')

fromTushare2pgTable(ApiName, Indate)
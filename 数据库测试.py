import pymysql
import pandas as pd
conn = pymysql.connect(host='172.16.5.160',port=3306,user='root',passwd='hxn1234')
数据 = pd.read_sql('select * from mysql.user',con=conn)
数据.to_excel('哇哦~.xlsx')
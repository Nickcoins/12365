import pandas as pd
from pymysql import connect

conn = connect(host='wardxu19858585.asuscomm.com', port=33066, user='guest', password='123456', database='test', charset='utf8')
sql ="""select *
     from `12365` as t
     inner join id1 on id1.id=t.抱怨分类
     inner join id2 on id2.id=t.抱怨细节
     where 车企 regexp '上汽大众|斯柯达'
         and id1.name='变速器'
         and t.`抱怨日期`>= '2020/1/1' AND t.`抱怨日期`<= '2020/6/1'"""
d = pd.read_sql(sql, con=conn)
gearbox_list = pd.read_excel(r"/Users/wardxu/Documents/GitHub/12365/变速箱匹配.xlsx")

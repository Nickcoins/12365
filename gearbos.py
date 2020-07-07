import pandas as pd
from pymysql import connect

def Gearbox(show_date):

    conn = connect(host='wardxu19858585.asuscomm.com', port=33066, user='guest', password='123456', database='test', charset='utf8')
    sql ="""select t.抱怨编号, t.车型, t.车辆配置, t.抱怨内容, t.抱怨日期, t.url, id2.name
         from `12365` as t
         inner join id1 on id1.id=t.抱怨分类
         inner join id2 on id2.id=t.抱怨细节
         where 车企 regexp '上汽大众|斯柯达'
             and id1.name='变速器'
             and t.`抱怨日期`>= '%s' AND t.`抱怨日期`<= '%s'""" %(str(show_date[0]), str(show_date[1]))
    d = pd.read_sql(sql, con=conn)
    gearbox_list = pd.read_excel(r"/Users/wardxu/Documents/GitHub/12365/变速箱匹配.xlsx")

    d['车辆配置'] = d['车辆配置'].str.replace(' ', '')
    gearbox_list['车辆配置'] = gearbox_list['车辆配置'].str.replace(' ', '')
    # print(d)
    # print(gearbox_list)
    a = pd.merge(d, gearbox_list, on=['车型', '车辆配置'], how='left')
    a['抱怨日期'] = pd.to_datetime(a['抱怨日期'])
    a['month'] = a['抱怨日期'].dt.to_period('M')

    # a = a.set_index('抱怨日期')
    # # print(a['变速箱型号'].resample('M').count().to_period('M'))
    # a = a.to_period('M')
    pd.set_option('display.max_columns', None)
    # print(a)
    #
    c = pd.pivot_table(a[['month', '变速箱型号']], index=['month'], columns=['变速箱型号'], aggfunc=len, fill_value=0)

    gear_list = a['变速箱型号'].drop_duplicates(keep='last')

    c.index = c.index.to_series().astype(str)#格式化index （period），以便后续保存

    for i in gear_list:
        temp = a[a.变速箱型号 == i]
        # print(temp.groupby('name')['抱怨编号'].count().sort_values(ascending=False))

    return c


show_date = ['2020/1/1', '2020/7/1']

Gearbox(show_date)
print(Gearbox(show_date))
# print(list(Gearbox(show_date))[1])
print(Gearbox(show_date).index)
# for i in range(Gearbox(show_date).shape[0]):
#     for j in range(Gearbox(show_date).shape[1]):
#         print(Gearbox(show_date).iloc[i, j])

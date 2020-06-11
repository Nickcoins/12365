import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import random
import pymysql
import json



class Get_data(object):

    def __init__(self):
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
            "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
            "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
            "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
            "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
            "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
            "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
            "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
            "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
            "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
            "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
            "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
            "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
            "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"]
        self.rurl = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
        self.headers = {'User-Agent': random.choice(self.user_agent_list)}
        self.conn = pymysql.connect(host="192.168.50.244", port=33066, user="root", password="198585", database="test")
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def get_table(self, page):
        time.sleep(random.randint(1, 3))
        datatable = pd.DataFrame()
        url = self.rurl + str(page) + '.shtml'
        r = requests.get(url, headers=self.headers)
        r.encoding = 'utf-8'
        content = r.text
        soup = BeautifulSoup(content, "html.parser")
        trs = soup.find_all('tr')
        url_lists = []
        for tr in trs[1:]:
            list_ = []
            for td in tr:
                list_.append(td.text)
            a = tr.find("a")
            a = a.get('href')
            url_list = self.get_detail(a)
            url_lists.append(url_list)
            list_.append(a)
            ulist = self.change(list_)
            datatable = pd.concat([datatable, ulist], ignore_index=True, sort=False)
            datatable['b'] = datatable['a'].str[0]
            datatable['c'] = datatable['a'].str[1:4]  # a列按照字符数拆分成b和c列
            datatable = datatable.dropna(subset=['b'])  # 过滤b列的空值
        print(page)
        r.close()
        return datatable, url_lists

    def get_detail(self, url):
        time.sleep(random.randint(1, 3))
        r = requests.get(url, headers=self.headers)
        r.encoding = 'gb18030'
        content = r.text
        soup = BeautifulSoup(content, "html.parser")
        div = soup.find('div', class_="tsnr")
        detail = div.find_all('p')
        num = len(detail)
        detail = detail[num - 1]
        sql_data = [url, detail.text]
        r.close()
        return sql_data


    def get_id(self):
        local_time = time.strftime("%Y%m%d")
        jsurl = 'http://www.12365auto.com/js/cTypeInfo.js?version=' + str(local_time)
        js_content = requests.get(jsurl, headers=self.headers)
        jd = js_content.text.strip('var cTypeInfo =')  # 删除开头的var内容，并转换成文本
        js = json.loads(jd)  # 转换成json格式
        return js

    def save_SQL_detail(self, list_):
        try:
            for i in range(len(list_)):
                u = list_[i]
                sql = """INSERT IGNORE INTO `detail`(url, text) values (%s, %s)"""
                data = [str(u[0]), str(u[1])]
                self.cursor.execute(sql, data)
            self.conn.commit()
            print("urlok")
        except:
            self.conn.rollback()
            print("urlno")


    def save_SQL_table(self, table):
        data_list = table.values  # dataframe类型转换list类型
        try:
            for i in range(len(data_list)):
                u = data_list[i]
                sql = "INSERT IGNORE INTO `12365` (抱怨编号, 车企, 车型, 车辆配置, 抱怨内容, 抱怨分类, 抱怨细节,抱怨日期, 处理状态, url) VALUES ('%s','%s','%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" \
                      % (str(u[0]), str(u[1]), str(u[2]), str(u[3]), str(u[4]), str(u[9]), str(u[10]), str(u[5]),
                         str(u[6]), str(u[7]))
                self.cursor.execute(sql)
            self.conn.commit()
            print("12365ok")
        except:
            self.conn.rollback()
            print("12365no")


    def save_SQL_id1(self, list_):
        try:
            for i in range(len(list_)):
                u = list_[i]
                sql = "INSERT IGNORE INTO `id1` (`id`, `name`) VALUES ('%s','%s')" \
                      % (str(u[1]), str(u[0]))
                self.cursor.execute(sql)
            self.conn.commit()
            print("id1_ok")
        except:
            self.conn.rollback()
            print("id1_no")

    def save_SQL_id2(self, list_):
        try:
            for i in range(len(list_)):
                u = list_[i]
                sql = "INSERT IGNORE INTO `id2` (`id`, `name`) VALUES ('%s','%s')" \
                      % (str(u[0]), str(u[1]))
                self.cursor.execute(sql)
            self.conn.commit()
            print("id2_ok")
        except:
            self.conn.rollback()
            print("id2_no")


    def change(self, ulist):
        df = pd.DataFrame(ulist)  # 转换dataframe格式
        df = df.T  # 行列转置
        a = df[5].str.split(',', expand=True)  # 用'，'分列，并扩展列
        a = a.stack()  # 逆透视
        a = a.reset_index(level=1, drop=True)  # 重置index，使用原来index
        a.name = 'a'  # 重命名列
        df_new = df.drop([5], axis=1).join(a)  # 用index合并原dataframe与a，删除原第5列
        return df_new

    def run(self):
        for i in range(1, 50):
            table, url_text = self.get_table(i)
            self.save_SQL_table(table)
            self.save_SQL_detail(url_text)

        id_1 = []
        id_2 = []
        js = self.get_id()
        for i in range(len(js)):
            a = (js[i]['name'], js[i]['value'])
            id_1.append(a)
            for j in range(len(js[i]['items'])):
                b = (js[i]['items'][j]['id'], js[i]['items'][j]['title'])
                id_2.append(b)
        self.save_SQL_id1(id_1)
        self.save_SQL_id2(id_2)


def main():
    get_data = Get_data()
    get_data.run()


if __name__ == '__main__':
    main()









from peewee import *
from datetime import datetime

# 连接数据库
db = MySQLDatabase('cnki', host='localhost', user='root', password='123456',port=3308)

# 定义模型类
class Paper(Model):
    title = TextField()
    authorname = TextField()
    institute = TextField()
    date = TextField()
    source = TextField()
    databasename = TextField()
    keywords = TextField()
    abstract = TextField()
    url = TextField()
    class Meta:
        database = db
        table_name = 'papers'

def save_paper(title, authorname, institute, date, source, databasename, keywords, abstract, url):
    Paper.create(title=title, authorname=authorname, institute=institute, date=date, source=source, databasename=databasename, keywords=keywords, abstract=abstract, url=url)
    print("存储数据")

# 存入数据库
# sql = f"insert into cnki values('{count}','{title}','{authors}','{institute}','{date}','{source}','{database}','{keywords}','{abstract}','{url}')"
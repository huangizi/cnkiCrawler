import time
from datetime import datetime
from selenium import webdriver
from peewee import *
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

# 自动安装最新版的 ChromeDriver
chromedriver_autoinstaller.install()


# webdriver.Chrome('D://Code//env//chromedriver_win32//chromedriver')
# driver = webdriver.Chrome('D://Code//env//chromedriver_win32//chromedriver')


# 连接数据库
db = MySQLDatabase('cnki', host='localhost', user='root', password='123456',port=3308)

# 定义模型类
class Paper(Model):
    title = TextField()
    author = TextField()
    abstract = TextField()
    link = TextField()
    created_at = DateTimeField(default=datetime.now)

    class Meta:
        database = db
        table_name = 'papers'

class CnkiSpider:
    def __init__(self):
        # 初始化 ChromeDriver
        self.driver = webdriver.Chrome('D://Code//env//chromedriver_win32//chromedriver')

    def __del__(self):
        # 关闭 ChromeDriver
        self.driver.quit()

    def run(self, keyword):
        # 打开知网主页
        self.driver.get('https://search.cnki.com.cn/')

        # 等待页面加载完成
        time.sleep(3)

        # 查找搜索表单并填写关键词
        input_box = self.driver.find_element('id','textSearchKey')
        input_box.clear()
        input_box.send_keys(keyword)

        # 点击搜索按钮
        search_button = self.driver.find_element('id','search')
        search_button.click()

        # 等待搜索结果页面加载完成
        time.sleep(3)

        # 提取论文列表中每篇论文的标题、作者、摘要和链接
        paper_list = self.driver.find_elements('class name','list-item')
        for paper in paper_list:
            title = paper.find_element('class name','left').get_attribute('title')
            link = paper.find_element('class name','left').get_attribute('href')
            author = paper.find_element('class name','source').find_elements('tag name','a')[0].text
            abstract = paper.find_element('class name','nr').text

            # 保存到数据库
            Paper.create(title=title, author=author, abstract=abstract, link=link)
        # paper_list = self.driver.find_elements(By.CLASS_NAME, 'list-item')
        # for paper in paper_list:
        #     title = paper.find_element(By.CLASS_NAME, 'left').get_attribute('title')
        #     link = paper.find_element(By.CLASS_NAME, 'left').get_attribute('href')
        #     author = paper.find_element(By.CLASS_NAME, 'source').find_elements(By.TAG_NAME, 'a')[0].text
        #     abstract = paper.find_element(By.CLASS_NAME, 'nr').text


if __name__ == '__main__':
    # 创建表格
    db.connect()
    db.create_tables([Paper])
    #
    # # 启动爬虫
    spider = CnkiSpider()
    spider.run('法律')


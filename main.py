import time
from datetime import datetime
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import crawler


# 设置搜索主题 theme = "人工智能"
# 设置所需篇数 papers_need = 100
def cnkiCrawler(theme="人工智能", papers_need=100):
    # get直接返回，不再等待界面加载完成
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"
    # 设置谷歌驱动器的环境
    options = webdriver.EdgeOptions()
    # 设置chrome不加载图片，提高速度
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    # # 设置不显示窗口
    # options.add_argument('--headless')
    # 创建一个谷歌驱动器
    driver = webdriver.Edge(options=options)
    res_unm = int(crawler.open_page(driver, theme))
    # 判断所需是否大于总篇数
    papers_need = papers_need if (papers_need <= res_unm) else res_unm
    crawler.crawl(driver, papers_need, theme)
    # 关闭浏览器
    driver.close()


if __name__ == '__main__':
    cnkiCrawler()


# # 自动安装最新版的 ChromeDriver
# chromedriver_autoinstaller.install()
#
#
# # webdriver.Chrome('D://Code//env//chromedriver_win32//chromedriver')
# # driver = webdriver.Chrome('D://Code//env//chromedriver_win32//chromedriver')
#
#

# class CnkiSpider:
#     def __init__(self):
#         # 初始化 ChromeDriver
#         self.driver = webdriver.Chrome('D://Code//env//chromedriver_win32//chromedriver')
#
#     def __del__(self):
#         # 关闭 ChromeDriver
#         self.driver.quit()
#
#     def run(self, keyword):
#         # 打开知网主页
#         self.driver.get('https://search.cnki.com.cn/')
#
#         # 等待页面加载完成
#         time.sleep(3)
#
#         # 查找搜索表单并填写关键词
#         input_box = self.driver.find_element('id','textSearchKey')
#         input_box.clear()
#         input_box.send_keys(keyword)
#
#         # 点击搜索按钮
#         search_button = self.driver.find_element('id','search')
#         search_button.click()
#
#         # 等待搜索结果页面加载完成
#         time.sleep(3)
#
#         # 提取论文列表中每篇论文的标题、作者、摘要和链接
#         paper_list = self.driver.find_elements('class name','list-item')
#         for paper in paper_list:
#             # 假设 elem 是您的 WebElement 对象
#             elems = paper.find_elements(By.CLASS_NAME, "left")
#
#             #print(paper.find_element('By.CLASS_NAME', 'left'))
#         #     title = paper.find_element('class name','left').get_attribute('title')
#         #     link = paper.find_element('class name','left').get_attribute('href')
#         #     author = paper.find_element('class name','source').find_elements('tag name','a')[0].text
#         #     abstract = paper.find_element('class name','nr').text
#         #
#         #     # 保存到数据库
#         #     Paper.create(title=title, author=author, abstract=abstract, link=link)
#         # paper_list = self.driver.find_elements(By.CLASS_NAME, 'list-item')
#         # for paper in paper_list:
#         #     title = paper.find_element(By.CLASS_NAME, 'left').get_attribute('title')
#         #     link = paper.find_element(By.CLASS_NAME, 'left').get_attribute('href')
#         #     author = paper.find_element(By.CLASS_NAME, 'source').find_elements(By.TAG_NAME, 'a')[0].text
#         #     abstract = paper.find_element(By.CLASS_NAME, 'nr').text
#
#
# if __name__ == '__main__':
#     # 创建表格
#     db.connect()
#     db.create_tables([Paper])
#     #
#     # # 启动爬虫
#     spider = CnkiSpider()
#     spider.run('法律')
#

# 知网文献数据爬取项目

这个项目旨在通过爬取中国知网的文献数据，为用户提供更方便的文献查询和分析工具。本项目使用 Python 语言和 Selenium 库实现爬虫程序，可以自动化地爬取指定关键字的文献数据，并将数据存储到数据库中，方便后续的分析和查询。

## 环境要求

- Python 3.x
- Selenium 库
- Edge 浏览器
- Microsoft Edge Driver

## 使用说明

1. 安装 Edge 浏览器和 Microsoft Edge Driver，并将驱动程序解压缩到指定目录中。
2. 安装 Python 3.x 和 Selenium 库。
3. 在 `dbConnect.py` 文件中配置数据库连接信息。
4. 运行 `crawler.py` 文件，传入关键字和需要爬取的文献数量，例如：
    
    ```python
    python crawler.py "人工智能" 100
    ```

这将会爬取包含关键字“机器学习”的前 100 篇文献，并将数据存储到数据库中。

## 数据库结构

本项目使用 MySQL 数据库存储文献数据，数据表的结构如下：

| 列名      | 类型         | 说明             |
| --------- | ------------ | ---------------- |
| id        | INT          | 序号，自增长     |
| title     | VARCHAR(255) | 文章标题         |
| authors   | VARCHAR(255) | 作者列表，逗号分隔 |
| institute | VARCHAR(255) | 机构             |
| date      | VARCHAR(20)  | 发表日期         |
| source    | VARCHAR(255) | 发表刊物         |
| database  | VARCHAR(20)  | 数据库           |
| keywords  | VARCHAR(255) | 关键词列表，逗号分隔 |
| abstract  | TEXT         | 摘要             |
| url       | VARCHAR(255) | 文章链接         |

## 项目贡献者

- 资资


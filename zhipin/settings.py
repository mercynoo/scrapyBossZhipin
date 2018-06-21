# -*- coding: utf-8 -*-

# Scrapy settings for zhipin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhipin'

SPIDER_MODULES = ['zhipin.spiders']
NEWSPIDER_MODULE = 'zhipin.spiders'

CONCURRENT = 1
CONCURRENT_ITEMS = 1
CONCURRENT_REQUESTS = 32

MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'zhipin'
MYSQL_USER = 'root'
MYSQL_PASSWD = '123456'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhipin (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"

# 以下为使用 cookie 时添加. 不使用的话在文件 MainLgjob 注释
ROBOTSTXT_OBEY = False  # 不遵守Robot协议
DOWNLOAD_DELAY = 3  # 延迟
COOKIES_ENABLED = True  # 启用 cookie

HEADERS = {
   'Connection': 'keep-alive',
   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}
META = {
   'dont_redirect': True,
   'handle_httpstatus_list': [301, 302]
}

COOKIES = {
    'lastCity': '101210110',
    ' __a': '45175773.1523166494.1523166494.1529476519.17.2.16.17',
    ' __g': '-',
    ' __c': '1529476519',
    ' toUrl': 'https%3A%2F%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%26scity%3D101210100%26industry%3D%26position%3D100306',
    ' __l': 'l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DESaDhXLCJjBGFt5Nk-H6U6_iAvXE6jMSUdA23RMmEb0DerOeteiSftQ7-o2HEt3M%26ck%3D6256.5.87.263.141.418.141.18%26shh%3Dwww.baidu.com%26sht%3Dbaidu%26wd%3D%26eqid%3Dcc9cce870002a8d7000000045b29f598',
    ' JSESSIONID': '""'}


# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhipin.middlewares.ZhipinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhipin.middlewares.ZhipinDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'zhipin.MyPipelines.MyPipeline': 100,
   'zhipin.MyPipelines.DBPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

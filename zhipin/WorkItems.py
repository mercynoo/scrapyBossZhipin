import scrapy

class WorkItem(scrapy.Item):

    # 公司名字
    company = scrapy.Field()
    # 职位名称
    positionName = scrapy.Field()
    # 工作年限
    seniority = scrapy.Field()
    # 薪资范围
    salary = scrapy.Field()
    # 学历要求
    education = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 行业
    industryField = scrapy.Field()
    # 融资情况
    financeStage = scrapy.Field()
    # 公司人数
    amount = scrapy.Field()



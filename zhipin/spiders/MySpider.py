import scrapy
from zhipin.WorkItems import WorkItem
from zhipin import settings

class MySpider(scrapy.Spider):

    #设置name
    name = "MySpider"
    #设定域名
    allowed_domains = ["zhipin.com"]
    #填写爬取地址
    start_urls = ["https://www.zhipin.com/c101210100-p110000/h_101210100/?page=1&ka=page-1"]

    #不使用cookie，注释 Request的 ,headers=self.headers, cookies=self.cookies, meta=self.meta
    meta = settings.META
    cookies = settings.COOKIES
    headers = settings.HEADERS

    def parse(self, response):
        body = response.css(".job-primary")
        for head in body:
            item = WorkItem()
            item["positionName"] = head.css(".job-title::text").extract()[0].strip()
            item["salary"] = head.css(".red::text").extract()[0].strip()
            item['company'] = head.css(".company-text .name a::text").extract_first()

            item['city'] = head.css(".info-primary p::text").extract_first().strip()
            item['seniority'] = head.css(".info-primary p::text").extract()[1].strip()
            item['education'] = head.css(".info-primary p::text").extract()[2].strip()

            item['industryField'] = head.css(".info-company .company-text p::text").extract_first().strip()
            item['financeStage'] = head.css(".info-company .company-text p::text").extract()[1].strip()
            # item['amount'] = head.css(".info-company .company-text p::text").extract()[-1].strip()

            yield item

        # url跟进开始

        # 获取下一页的url信息
        url = response.xpath('//a[@class="next"]/@href').extract()
        if url :
            #将信息组合成下一页的url
            page = 'https://www.zhipin.com/' + url[0]
            #返回url
            yield scrapy.Request(page, callback=self.parse)
        #url跟进结束
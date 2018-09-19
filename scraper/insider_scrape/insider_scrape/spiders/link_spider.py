import scrapy, pickle, time

class LinkSpider(scrapy.Spider):
    name = "links"
    link_ls = []

    def start_requests(self):
        with open('big_cik_list.list', 'rb') as fi:
            cik_list = pickle.load(fi)
        root = 'https://www.sec.gov/Archives/edgar/data/'
        urls = [root + str(i) for i in cik_list]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #temp = response.css('a::attr(href)').extract()
        #temp = ['https://www.sec.gov' + i for i in temp if '/Archives/edgar/data/' in i]

        temp = response.css('tr')
        for i in temp:
            if 'class="img_icon"' in i.extract():
                date_temp = i.css('td::text').extract()[0].split(' ')[0]
                date_timestamp = int(time.mktime(time.strptime(date_temp, '%Y-%m-%d')))
                cutoff = '2018-09-13' #Adjust this
                cutoff_timestamp = int(time.mktime(time.strptime(cutoff, '%Y-%m-%d')))
                temp = i.css('a::attr(href)').extract()[0]
                temp = 'https://www.sec.gov' + temp
                if date_timestamp >= cutoff_timestamp:
                    self.link_ls.append(temp)

    def closed(self, reason):
        with open('link_ls.list', 'wb') as fi:
            pickle.dump(self.link_ls, fi)

class FullSpider(scrapy.Spider):
    name = "full"

    def start_requests(self):
        with open('link_ls.list', 'rb') as fi:
            urls = pickle.load(fi)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")
        filename = 'xml_docs/' + str(page[-3]) + '-' + str(page[-2]) + '-' + str(page[-1])
        if filename.endswith('.xml'):
            with open(filename, 'wb') as f:
                f.write(response.body)

        temp = response.css('a::attr(href)').extract()
        temp = ['https://www.sec.gov' + i for i in temp if i.endswith('.xml')]
        for i in temp:
            if i is not None:
                next_page = response.urljoin(i)
                yield scrapy.Request(next_page, callback=self.parse)

class DocSpider(scrapy.Spider):
    name = "docs"
    doc_links = []

    def start_requests(self):
        with open('link_ls.list', 'rb') as fi:
            urls = pickle.load(fi)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        temp = response.css('a::attr(href)').extract()
        temp = ['https://www.sec.gov' + i for i in temp if i.endswith('.xml')]
        self.doc_links.extend(temp)

    def closed(self, reason):
        with open('doc_links.list', 'wb') as fi:
            pickle.dump(self.doc_links, fi)

class GetDocs(scrapy.Spider):
    name = "getdocs"
    def start_requests(self):
        with open('doc_links.list', 'rb') as fi:
            urls = pickle.load(fi)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")
        filename = 'xml_docs/' + str(page[-3]) + '-' + str(page[-2]) + '-' + str(page[-1])
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

class NewLinkSpider(scrapy.Spider):
    name = "new"

    def start_requests(self):
        with open('SP500_cik_list.list', 'rb') as fi:
            cik_list = pickle.load(fi)
        root = 'https://www.sec.gov/Archives/edgar/data/'
        urls = [root + str(i) for i in cik_list]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")
        filename = 'xml_docs/' + str(page[-3]) + '-' + str(page[-2]) + '-' + str(page[-1])
        self.log(filename)
        if filename.endswith('.xml'):
            with open(filename, 'wb') as f:
                f.write(response.body)

        temp = response.css('a::attr(href)').extract()
        temp = ['https://www.sec.gov' + i for i in temp if '/Archives/edgar/data/' in i]
        for i in temp:
            if i is not None:
                next_page = response.urljoin(i)
                yield scrapy.Request(next_page, callback=self.parse)
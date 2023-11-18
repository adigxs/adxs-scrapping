import math
from cssselect import Selector
import scrapy


class GlotelhoproductspiderSpider(scrapy.Spider):
    name = "glotelhoproductspider"
    allowed_domains = ["glotelho.cm"]
    start_urls = [
'https://glotelho.cm/en/telephones-tablettes.html',
 'https://glotelho.cm/en/apple.html',
 'https://glotelho.cm/en/informatique.html',
 'https://glotelho.cm/en/gaming.html',
 'https://glotelho.cm/en/home-appliance.html',
 'https://glotelho.cm/en/electronics.html',
 'https://glotelho.cm/en/automotive-and-accessories.html',
 'https://glotelho.cm/en/network-and-telecom.html',
 'https://glotelho.cm/en/security.html',
 'https://glotelho.cm/en/home-offices.html',
 'https://glotelho.cm/en/small-appliance.html',
 'https://glotelho.cm/en/fashion.html',
 'https://glotelho.cm/en/sports-universe.html',
 'https://glotelho.cm/en/tools-and-ppe.html',
 'https://glotelho.cm/en/supermarche.html',
 'https://glotelho.cm/en/beauty-and-health.html',
 'https://glotelho.cm/en/health-products-ng4l.html']
    
    # pour avoir la valeur de start_urls executer categ dans le scrapy shell


    def parse(self, response):
        #categ=response.xpath("//a[@class='level-top']/@href").getall()[:-1]
        products=response.css('div.product-item-info')
        sel = Selector(response)
        allink=response.xpath('//*[@id="toolbar-amount"]/span[3]/text()').get()
       
        x=int(allink)
        #nb = response.css("p.store-count").get().split(':')[-1].strip().split(' ')[0]

        print(x)

        i=2

        # product_item= ProductScrapingItem()
        # cat=response.css('ul.verticalmenu-list>li>a::attr(href)').getall()[:-1]
        

        # for i in cat:

        category=''

        for product in products:
                    
            try:
                price_init = float(product.xpath(".//div[2]/div[2]/span[2]/span/span[2]/span/span/span/text()").get().replace(',',''))
            except Exception as e:
                price_init = 0

            try:
                price_red = float(product.xpath(".//div[2]/div[2]/span/span/span[2]/span/span/span/text()").get().replace(',',''))
            except Exception as e:
                price_red = 0
                    
            yield{
                        
                    'site' :  'glotelho',
                    'name' :  product.xpath(".//div[2]/strong/a/text()").get(), # OK
                    'category' :  category, # OK
                    'rating' :  0, # Ok
                
                    'price_init' : price_init,
                    'price_red' : price_red,
                    'url' : product.xpath(".//div[2]/strong/a/@href").get(),

                    'shop':{
                        'store_name' : 'glotelho',
                    'fone_s' : '233507300'
                    },
                    
                    
                    }
                    
                    

        # next_page = response.css('[rel="next"] ::attr(href)').get()

        # if next_page is not None:
        #     next_page_url = next_page
        #     yield response.follow(next_page_url, callback=self.parse)

        for i in range(2,math.ceil(x/50)+1):
           
           next_page_url =response.url.split('?p=')[0]+'?p='+str(i)+'/'
           yield response.follow(next_page_url, callback=self.parse)


        # for i in categ:


        #     next_page_url =i
        #     yield response.follow(next_page_url, callback=self.parse)
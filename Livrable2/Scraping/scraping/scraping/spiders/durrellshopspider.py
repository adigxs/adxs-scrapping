import scrapy
from scrapy.selector import Selector


class DurrellshopspiderSpider(scrapy.Spider):
    name = "durrellshopspider"
    allowed_domains = ["durrellmarket.com"]
    start_urls = ["https://durrellmarket.com/store-listing"]

    

    def parse(self, response):
        sel = Selector(response)
        allink=sel.xpath ('//a [@class="page-numbers"]/@href').getall()[-1:][0].split('/')[-2:][0]
        
        x=int(allink)

        print(x)

        i=2

        for i in range(2,97):

            products=response.css('div.store-wrapper')

            for product in products:
                    
                try:
                    rating = product.xpath(".//div/p/text()").get().split("sur")[0].split(" ")[-2]
                except Exception as e:
                    rating = ''

                try: 
                    street = product.xpath(".//p[1]/span[1]/text()").get().split(',')[0]
                except Exception as e:
                    street = ''

                try:
                    city = product.xpath(".//p[1]/span[2]/text()").get().split(',')[0]
                except Exception as e:
                    city = ''

                try:
                    state = product.xpath(".//p[1]/span[3]/text()").get().split(',')[0]
                except Exception as e:
                    state = ''

                try:
                    country = product.xpath(".//p[1]/span[4]/text()").get().split(',')[0]
                except Exception as e:
                    country = ''

                try:
                    phone = product.xpath(".//p[@class='store-phone']").get().split('> ')[1].split(' ')[0]

                except Exception as e:
                    phone = ''

                yield{
                        
                    'site' :  'durell_market',
                    'name' :  product.xpath(".//h2/a/text()").get(), # OK
                    #'category' :  product.xpath(".//div[@class='wd-product-cats']/a/text()").get(), # OK
                    
                    'rating' :  rating, # Ok
                
                    'street' : street,
                    'city' : city,
                    'state' : state,
                    'country' : country,
                    'phone' : phone,
                
                    }
                    
            

            

            # next_page = response.css('[rel="next"] ::attr(href)').get()

            # if next_page is not None:
            #    next_page_url = next_page
            #    yield response.follow(next_page_url, callback=self.parse)





            next_page = 'https://durrellmarket.com/store-listing/page/'+str(i)+'/'

            print(i)
            print(next_page)

            next_page_url = next_page
            yield response.follow(next_page_url, callback=self.parse)





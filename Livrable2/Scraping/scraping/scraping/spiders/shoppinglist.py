import scrapy


class ShoppinglistSpider(scrapy.Spider):
    name = "shoppinglist"
    allowed_domains = ["shoppinglist.cm"]
    start_urls = ["https://shoppinglist.cm/fr/search/product/?query=&sort_by=&start=0"]

    #?query=&sort_by=&start=0

    def parse(self, response):
        products=response.css('div.ps-product')

        # product_item= ProductScrapingItem()

        # nb est le nombre de produits total sur la pages des produits 
        nb= response.xpath("/html/body/div[7]/div/div/div/form/div/div[2]/div/div[1]/div/div[1]/span/strong[1]/text()").get()

        for product in products:
                
                try:
                    price_init = float(product.xpath(".//div[2]/div/p/del/span/text()").get().replace("\xa0",'').strip().split('FCFA')[0])
                except Exception as e:
                    price_init = 0

                try:
                    price_red = float(product.xpath(".//div[2]/div/p/span/text()").get().replace("\xa0",'').strip().split('FCFA')[0])
                except Exception as e:
                    price_red = 0

                try:
                    rating = float(product.xpath(".//div[2]/div/div/span/text()").get().strip())
                except Exception as e:
                    rating = 0
                
                yield{
                     
                'site' :  'shoppinglist',
                'name' :  product.xpath(".//div[2]/div/a/text()").get().strip(), # OK
                'category' :  product.xpath(".//div[@class='wd-product-cats']/a/text()").get(), # OK
                'rating' : rating , # Ok
                # 'price_init' :  product.xpath(".//span[@class='price']/del/span/bdi/text()").get().replace("\xa0",''),
                # 'price_red' :  product.xpath(".//span[@class='price']/span/bdi/text()").get().replace("\xa0",''),
                # 'image' :  product.xpath(".//div/a/picture/@data-wood-src").get(),

                'price_init' : price_init,
                'price_red' : price_red,

                'url' : "shoppinglist.cm"+product.xpath(".//div[2]/a/@href").get(),

                'shop': {
                'store_name': product.xpath(".//div[2]/a/text()").get().strip(),
                'fone_s': "693154242"
                    },

                }
                

        # next_page = response.css('[rel="next"] ::attr(href)').get()

        for i in range(24,int(nb)+1, 24):
           next_page_url ="https://shoppinglist.cm/fr/search/product/?query=&sort_by=&start="+str(i)
           yield response.follow(next_page_url, callback=self.parse)

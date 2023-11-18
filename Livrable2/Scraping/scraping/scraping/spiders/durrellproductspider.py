import scrapy


class DurrellproductspiderSpider(scrapy.Spider):
    name = "durrellproductspider"
    allowed_domains = ["durrellmarket.com"]
    start_urls = ["https://durrellmarket.com/shop"]


    def parse(self, response):
        products=response.css('div.product-grid-item')

        # product_item= ProductScrapingItem()

        for product in products:
                
            try:
                price_init = product.xpath(".//span[@class='price']/del/span/bdi/text()").get().replace("\xa0",'')
            except Exception as e:
                price_init = ''

            try:
                price_red = product.xpath(".//span[@class='price']/ins/span/bdi/text()").get().replace("\xa0",'')
            except Exception as e:
                price_red = ''

                
            yield{
                     
                'site' :  'durell_market',
                'name' :  product.xpath(".//h3/a/text()").get(), # OK
                'category' :  product.xpath(".//div[@class='wd-product-cats']/a/text()").get(), # OK
                'rating' :  product.xpath(".//div[@class='star-rating']/span/strong/text()").get(), # Ok
                # 'price_init' :  product.xpath(".//span[@class='price']/del/span/bdi/text()").get().replace("\xa0",''),
                # 'price_red' :  product.xpath(".//span[@class='price']/span/bdi/text()").get().replace("\xa0",''),
                # 'image' :  product.xpath(".//div/a/picture/@data-wood-src").get(),

                'price_init' : price_init,
                'price_red' : price_red,

                

                
                'url' : product.xpath(".//div/a/@href").get(),

                'store_name' :  product.xpath("//span[@class='store_name']/a/text()").get(),
                'fone_s' :  product.xpath("//span[@class='listing_phone']/a/text()").get()
                

                }
                

        next_page = response.css('[rel="next"] ::attr(href)').get()

        if next_page is not None:
           next_page_url = next_page
           yield response.follow(next_page_url, callback=self.parse)

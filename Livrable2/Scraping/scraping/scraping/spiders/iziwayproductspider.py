import scrapy

# from scraping.items import WebsiteItem

import csv

# with open('/home/kemal/Documents/Projets/ADXS/Scraping/iziwayproducts.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in reader:
#         variable1 = row[0]
#         variable2 = row[1]
#         variable3 = row[2]



# # Importer les bibliothèques nécessaires
# import requests
# from bs4 import BeautifulSoup

# # Envoyer une requête GET à l'URL de Google
# response = requests.get("https://iziway.cm/collections")

# # Créer un objet BeautifulSoup à partir du contenu de la réponse, en utilisant l'analyseur html.parser
# soup = BeautifulSoup(response.content, "html.parser")

# cat=response.css('div.cat-list-item a::attr(href)')

#
class IziwayproductspiderSpider(scrapy.Spider):
    name = "iziwayproductspider"
    allowed_domains = ["iziway.cm"]
    start_urls = ["https://iziway.cm/collections"]
    


    def parse(self, response):
        products=response.css('div.c-product')

        # product_item= ProductScrapingItem()
        cat=response.xpath('//div [@class="cat-list-item"]/a/@href').getall()
        
        
        for i in cat:

            category=i

            for product in products:
                    
                    try:
                        price_init = product.xpath(".//div[2]/div/span[2]/del/text()").get().replace("\xa0",'').replace(" FCFA",'')
                    except Exception as e:
                        price_init = ''

                    try:
                        price_red = product.xpath(".//div[2]/div/span[1]/text()").get().replace("\xa0",'').replace(" FCFA",'')

                    except Exception as e:
                        price_red = ''

                    
                    yield{
                        
                    'site' :  'iziway',
                    'name' :  product.xpath(".//div[2]/p/a/text()").get(), # OK
                    'category' :  category, # OK
                    'rating' :  '', # Ok
                    # 'price_init' :  product.xpath(".//span[@class='price']/del/span/bdi/text()").get().replace("\xa0",''),
                    # 'price_red' :  product.xpath(".//span[@class='price']/span/bdi/text()").get().replace("\xa0",''),
                    # 'image' :  product.xpath(".//div/a/picture/@data-wood-src").get(),

                    'price_init' : price_init,
                    'price_red' : price_red,

                    

                    
                    'url' : ""+category+product.xpath(".//div[2]/p/a/@href").get(),
                    'store_name' : 'iziway',
                    'fone_s' : '656358251'
                    }
                    

            next_page = response.css('[rel="next"] ::attr(href)').get()

            if next_page is not None:
                next_page_url = next_page
                yield response.follow(next_page_url, callback=self.parse)

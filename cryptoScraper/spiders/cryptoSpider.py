
import imp
import json
import scrapy

class GoodReadsSpider(scrapy.Spider):
    
    
    
   
    #idntity
    name = 'crypto'

    #requests
    def start_requests(self):
        url = 'https://crypto.com/price'

       
       
       
        yield scrapy.Request(url=url, callback=self.parse)
        
    
    #response 

    
    def parse(self, response, **kwargs):

       
       
        
        

        changes=[]
        for crypto in response.selector.xpath("//tr[@class='css-1cxc880']"):
            change = crypto.xpath(".//p[@class='chakra-text css-1okxd']/text()").extract_first()
            changes.append(change)

            if change == None:
                path = ".//p[@class='chakra-text css-dg4gux']/text()"
            else:
                path = ".//p[@class='chakra-text css-1okxd']/text()"     

            yield{
                'cryptoName': crypto.xpath(".//a[@class='chakra-text css-o2rp9n']/text()").extract_first(),
                'cryptoTag': crypto.xpath(".//span[@class='chakra-text css-1jj7b1a']/text()").extract_first(),
                'price': crypto.xpath(".//div[@class='css-b1ilzc']/text()").extract_first(),
                '24H change': crypto.xpath(path).extract_first()
            }
            
           
           
       

       
        # with open('spiders/crypto_info.json' ,'r') as f:
            # data = json.load(f)
        # with open('spiders/crypto_info.json', 'w') as f:         
            # json.dump(data,f, indent=2)

        
        


       
       
       
       






        # next_page = response.selector.xpath("//a[@class='next_page']/@href").extract_first()    
        # 
        # if next_page is not None:
            # next_page_link = response.urljoin(next_page)
            # yield scrapy.Request(url=next_page_link, callback=self.parse)

            
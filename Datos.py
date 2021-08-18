import scrapy
from scrapy.item import Field
from scrapy.item import Item
from scrapy.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.loader.processors import MapCompose
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from bs4 import BeautifulSoup

class Articulo(Item):
     id = Field()
     titulo = Field()
     modelo = Field()
     marca = Field()
     procesador = Field()
     modProce = Field()
     veloProce = Field()
     nucleosProce = Field()
     linea = Field()
     ramDisponible = Field()
     ramMax = Field()
     optane = Field()
     tipoAlmacenamiento = Field()
     almacenamiento = Field()
     almacenamientoAdi = Field()
     SSD = Field()
     tipoTarVideo = Field()
     marcaTarVideo = Field()
     modeTarVideo = Field()
     memoriaTarVideo = Field()
     sisOperativo = Field()
     verSisOperativo = Field()
     precioRef = Field()
     precioOfer = Field()
     precioOferEfec = Field()


class PcFactoryCrawler(CrawlSpider):
     name = 'PcFactory'
     custom_settings = {
         'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
     }
     download_delay = 1
 
     allowed_domains = ['pcfactory.cl']   #Se pueden añadir dominios con comas
 
     start_urls = ['https://www.pcfactory.cl/notebooks?categoria=735&papa=636&pagina=']
 
     rules = (
         Rule(  #Paginacion horizontal
             LinkExtractor(
                 allow=r'/notebooks?categoria=735&papa=636&pagina='
             ), follow=True),
 
         Rule(   #Paginacion vertical
             LinkExtractor(
                 allow=r'-notebook-'
             ), follow=True, callback='parse_items'),
             Rule(   #Paginacion vertical
             LinkExtractor(
                 allow=r'-apple-macbook-'
             ), follow=True, callback='parse_items'),
     )

     def Limpiartext(self, texto):
        nuevotext = texto.replace('™', '').replace('\r', ' ').replace('\t', ' ').replace('á', 'a').replace('é', 'e').replace('í', ' i').replace('ó', 'o').replace('ú', 'u').replace('Á', 'A').replace('É', 'E').replace('Í', 'I').replace('Ó', 'O').replace('Ú','U').replace('®', '').replace('"', ' ').replace('ᵉ', '').strip()
        return nuevotext
 
     def parse_items(self, response):
         item = ItemLoader(Articulo(), response)
         item.add_xpath('id', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[2]/div/div/div[2]/text()')
         item.add_xpath('titulo', '//div[@class="product-single__description"]/div[@class="paragraph color-dark-2"]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('modelo', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[5]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('marca', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[3]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('procesador', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[8]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('modProce', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[10]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('linea', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[9]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('veloProce', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[11]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('nucleosProce', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[2]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('ramDisponible', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[14]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('ramMax', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[15]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('optane', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[17]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('tipoAlmacenamiento', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[19]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('almacenamiento', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[20]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('almacenamientoAdi', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[21]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('SSD', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[22]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('tipoTarVideo', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[28]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('marcaTarVideo', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[29]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('modeTarVideo', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[30]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('memoriaTarVideo', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[31]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('sisOperativo', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[33]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('verSisOperativo', '//*[@id="app"]/div[4]/div/div[6]/div[3]/div/div[34]/div/div/div[2]/text()',MapCompose(self.Limpiartext))
         item.add_xpath('precioRef', '//*[@id="id_ficha_producto"]/div[3]/div[3]/div[3]/div/text()',MapCompose(self.Limpiartext))
         item.add_xpath('precioOfer', '//*[@id="id_ficha_producto"]/div[3]/div[3]/div[2]/div/text()',MapCompose(self.Limpiartext))
         item.add_xpath('precioOferEfec', '//*[@id="id_ficha_producto"]/div[3]/div[3]/div[1]/div/text()',MapCompose(self.Limpiartext))

         yield item.load_item()

from bs4 import BeautifulSoup as bs
import requests as req
import linker
from fake_useragent import UserAgent


class Parser:
    link = str()
    tovar = str()

    def __init__(self, link):
        self.link = link
        self.tovar = link

   def avito():
        link = "https://www.avito.ru/chelyabinsk/bytovaya_tehnika?q=видеокарт.."
        d = {}
        ua = UserAgent()
        parsed = bs(req.get(link, headers={'User-Agent': ua.chrome}).text, "html.parser")
        pars = parsed.find_all("div", class_="iva-item-titleStep-2bjuh")
        prices = parsed.find_all("div", class_="iva-item-priceStep-2qRpg")
        i = 0
        res = pd.DataFrame(columns=('name', 'link', 'price'))
        for p in pars:
            d[p.text] = ["https://www.avito.ru/" + p.find("a").get("href"),prices[i].text.translate({ord(i): None for i in "\0₽"})]
            price1 = prices[i].text.translate({ord(i): None for i in "\0₽"})
            res.loc[i]= [p.text, "https://www.avito.ru/" + p.find("a").get("href"), price1.unicodestring.replace('\xa0','')]
            i += 1
        return res

    def citilink():
        link = "https://www.citilink.ru/search/?text=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D0%B0&menu_id=29"
        d = {}
        ua = UserAgent()
        parsed = bs(req.get(link, headers={'User-Agent': ua.chrome}).text, "html.parser")
        pars = parsed.find_all("div", class_="ProductCardVerticalLayout ProductCardVertical__layout")
        i = 0
        resСiti = pd.DataFrame(columns=('name', 'link', 'price'))
        for p in pars:
            pp = p.find("div", class_="ProductCardVertical__description").find("a", class_="ProductCardVertical__name")
            d[pp.text] = ["https://www.citilink.ru/" + pp.get("href"), p.find_all("span", class_="ProductCardVerticalPrice__price-current_current-price")[0].text.strip()]
            i += 1
            resСiti.loc[i]= [pp.text, "https://www.citilink.ru/" + pp.get("href"), p.find_all("span", class_="ProductCardVerticalPrice__price-current_current-price")[0].text.strip()]
        return resСiti
    
    def dns():
        link = "https://www.dns-shop.ru/search/?q=%D0%B2%D0%B8%D0%B4%D0%B5%D0%BE%D0%BA%D0%B0%D1%80%D1%82%D0%B0&stock=hard"
        d = {}
        ua = UserAgent()
        parsed = bs(req.get(link, headers={'User-Agent': ua.chrome}).text, "html.parser")
        pars = parsed.find_all("div", class_="catalog-product ui-button-widget")
        resDNS = pd.DataFrame(columns=('name', 'link', 'price'))
        i = 0
        for p in pars:
            temp = p.find("a", class_="catalog-product__name ui-link ui-link_black")
            d[temp.text] = ["https://www.dns-shop.ru/" + str(temp.get("href")), ""]
            resDNS.loc[i]= [temp.text, "https://www.dns-shop.ru/" + str(temp.get("href")),p.find("div", class_="product-buy__price")]
        return resDNS
        
        

#%%

pr = Parser
res=pr.avito()

rs = pd.DataFrame(res)
rs

#%%

rs.plot(x= 'name',  y='price', kind='scatter', rot=90)

    def get_resp(self, link):
        ua = UserAgent()
        resp = req.get(link, headers={'User-Agent': ua.chrome})
        return resp.text

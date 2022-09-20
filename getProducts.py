from callURL import getPageString
from bs4 import BeautifulSoup

def getProducts(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id": "productList"}) #아이템 리스트 추출
    lis = ul.findAll("li", {"class":"baby"})

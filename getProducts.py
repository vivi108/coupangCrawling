
from callURL import getPageString
from bs4 import BeautifulSoup

def getProducts(string):
    bsObj = BeautifulSoup(string, "html.parser")
    ul = bsObj.find("ul", {"id": "productList"}) #아이템 리스트 추출
    lis = ul.findAll("li", {"class":"baby-product renew-badge"})
    for item in lis:
        # url
        a = item.find("a", {"class": "baby-product-link"}) #리스트의 클래스명
        url = a.get('href')
        print("url:", url)

        # name
        div_name = item.find("div", {"class": "name"})
        name = div_name.getText()
        print("name:", name)

        # price
        price = item.find("strong", {"class": "price-value"}).getText()
        print("price:", price)

        rate = item.find("em", {"class":"rating"})
        print("rate :", rate)

    print("len(lis)",len(lis))
    return []


url = "https://www.coupang.com/np/categories/178454"

pageString = getPageString(url)
print(getProducts(pageString))
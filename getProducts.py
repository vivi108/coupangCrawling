from callURL import getPageString
from bs4 import BeautifulSoup
import requests
import openpyxl


def getProducts(string):
    bsObj = BeautifulSoup(string, "lxml")
    print(bsObj.prettify())
    ul = bsObj.find("ul", {"id": "productList"})  # 아이템 리스트 추출
    lis = ul.findAll("li", {"class": "baby-product renew-badge"})

    # excel_file = openpyxl.Workbook()
    # excel_sheet = excel_file.active
    # excel_sheet.append(['순번', '상품명', '판매가격'])
    print(lis)
    # for item in lis:
    #     # url
    #     a = item.find("a", {"class": "baby-product-link"}) #리스트의 클래스명
    #     url = a.get('href')
    #     print("url:", url)
    #
    #     # name
    #     div_name = item.find("div", {"class": "name"})
    #     name = div_name.getText()
    #     print("name:", name)
    #
    #     # price
    #     price = item.find("strong", {"class": "price-value"}).getText()
    #     print("price:", price)
    #
    #     rate = item.find("em", {"class":"rating"}).getText()
    #     print("rate :", rate)
    #
    #     #excel_sheet.append([index + 1, name, price, rate])
    #
    # print("len(lis)",len(lis))
    # # excel_file.save('PRODUCT_LIST.xlsx')
    # # excel_file.close()

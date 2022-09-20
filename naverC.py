import openpyxl
import requests
from bs4 import BeautifulSoup
import openpyxl
from pandas import ExcelWriter
from openpyxl.writer.excel import ExcelWriter
import pandas as pd

# 컬럼 값을 지정하여 엑셀시트 생성


excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.append(['순번', '상품명', '판매가격'])

web_site = requests.get("https://search.shopping.naver.com/catalog/31962261621")
bsObj = BeautifulSoup(web_site.text, 'html.parser')

ul = bsObj.find("ul", {"class": "reviewItems_list_review__q726A"})  # 아이템 리스트 추출
lis = ul.findAll("li", {"class": ""})
print(lis)

xls_path = 'PRODUCT_LIST.xlsx'

def save_xls(list_dfs, xls_path):
    writer = ExcelWriter(xls_path)
    for n, df in enumerate(list_dfs):
        df.to_excel(writer, 'sheet%s' % n)
    writer.save()

item_list = []
for index, item in enumerate(lis):
    content = item.find("em", {"class": "reviewItems_title__AwHcz"}).getText()
    # print("내용:", content)

    rate = item.find("span", {"class": "reviewItems_average__0kLWX"}).getText()
    # print("rate :", rate)
    # print("")
    item_list.append([content, rate])


df=pd.DataFrame(item_list)
df.columns =name=['상품명', '판매가격']
print(df)
df.to_csv('sample.csv')
# save_xls(df, xls_path)



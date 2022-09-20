
from callURL import getPageString
from getProducts import getProducts

url = "https://www.coupang.com/np/categories/497135"

pageString = getPageString(url)
print(getProducts(pageString))

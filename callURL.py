
import requests

# Headers 원래 필수 값이 아니다. 하지만 쿠팡의 경우 headers 없이 크롤링 했을때는 결과가 한개도 나오지 않는다.
# 그래서 headers를 위와 같이 설정해주면 된다
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36"}
def getPageString(url):
    data = requests.get(url, headers=headers)
    print(data.content)
    return data.content


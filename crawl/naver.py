import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://finance.naver.com/"

userAgent = UserAgent()
headers = {"user-agent": userAgent.chrome}

with requests.Session() as s:
    r = s.get(url, headers=headers)
    print(r.text)
    print(r.status_code)
    soup = BeautifulSoup(r.text, "lxml")
    # container > div.aside > div > div.aside_area.aside_stock > table : 해외증시
    global_stock = soup.select("div.aside_area.aside_stock > table >tbody > tr th a")
    # print(global_stock)
    for item in global_stock:
        print(item.get_text())

    print("=" * 10)

    # container > div.aside > div > div.aside_area.aside_popular > table : 인기검색
    stock = soup.select("div.aside_area.aside_popular > table >tbody > tr")

    # print(stock)
    for item in stock:
        # 회사명
        company_name = item.select_one("a").string
        # 현재 금액
        current_amount = item.select_one("td").string

        print(company_name, current_amount)

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

ws.title = "도서검색"
# 너비 조정
ws.column_dimensions["B"].width = 30
ws.column_dimensions["C"].width = 100
ws.column_dimensions["D"].width = 20
ws.column_dimensions["E"].width = 20
ws.append(["순위", "isbn", "책제목", "할인가격"])

headers = {
    "X-Naver-Client-Id": "SR_E7i6U8jju7V_SEf0T",
    "X-Naver-Client-Secret": "v4cFJWfFJ1",
}

start, num = 1, 1
for idx in range(3):
    # idx : 0~9
    start_num = start + (idx * 100)
    url = "https://openapi.naver.com/v1/search/book.json"
    params = {"query": "히가시노 게이고", "display": "100", "start": str(start_num)}
    r = requests.get(url, headers=headers, params=params)

    # print(r.url)

    # json() 가져오기
    data = r.json()
    # print(data)
    # print(data["items"])
    for idx, item in enumerate(data["items"], 1):
        print(item)
        ws.append([num, item["isbn"], item["title"], item["discount"]])
        num += 1


# 저장
base_dir = "./crawl/file/"
wb.save(base_dir + "히가시노게이고.xlsx")
wb.close()

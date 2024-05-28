import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from xlsx_write import write_excel_template
from datetime import datetime
from urllib.error import HTTPError

# 파이썬으로 뉴스시가 크롤링 하기


base_url = "https://news.google.com"


def main(keyword):
    url = "https://news.google.com/search?q=" + keyword + "&hl=ko&gl=KR&ceid=KR%3Ako"
    try:

        with requests.Session() as s:

            r = s.get(url)
            soup = BeautifulSoup(r.text, "lxml")

            news_clipping = data_extract(soup=soup)

            for news in news_clipping:
                for k, v in news.items():
                    print(f"{k} : {v}")
                print()
    except HTTPError as e:
        print(e.code)


def data_extract(soup):
    news = []
    news_items = {}

    # yDmH0d > c-wiz:nth-child(31) > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(4) > c-wiz > article
    articles = soup.select("div.UW0SDc article")

    for article in articles:
        # yDmH0d > c-wiz:nth-child(31) > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(4) > c-wiz > article > div.m5k28 > div.B6pJDd > div > a
        link_title = article.select_one("article > div.m5k28 > div.B6pJDd > div > a")

        # 제목 추출
        news_items["title"] = link_title.text.strip()
        # 뉴스기사 링크 추출
        news_items["href"] = base_url + link_title["href"][1:]
        # ./articles/CBMiW2h0dHBzOi8vd3d3LmNhZGdyYXBoaWNzLmNvLmtyL25ld3N2aWV3LnBocD9wYWdlcz1sZWN0dXJlJnN1Yj1sZWN0dXJlMDImY2F0ZWNvZGU9OCZudW09NzQxMDDSAQA?hl=ko&gl=KR&ceid=KR%3Ako
        # https://news.google.com/

        # yDmH0d > c-wiz:nth-child(31) > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(4) > c-wiz > article > div.m5k28 > div.B6pJDd > div > div > div.oovtQ > div > div
        # 작성자
        news_items["writer"] = article.select_one("div.oovtQ > div > div").text.strip()
        # yDmH0d > c-wiz:nth-child(31) > div > main > div.UW0SDc > c-wiz > c-wiz:nth-child(4) > c-wiz > article > div.UOVeFe > time
        # T 기준으로 분리
        # 2024-05-03T07:00:00Z
        report_date_tiem = article.select_one("time")
        if report_date_tiem:
            # split -> [2024-05-03,07:00:00Z]
            report_date_tiem = report_date_tiem["datetime"].split("T")
            news_items["report_date"] = report_date_tiem[0]
            news_items["report_time"] = report_date_tiem[1]
        else:
            news_items["report_date"] = ""
            news_items["report_time"] = ""

        # print(title, href, writer, report_date, report_time)
        news.append(news_items)

        news_items = {}

        # 확인
        # print(news[:3])
    return news


if __name__ == "__main__":
    main("아이폰")

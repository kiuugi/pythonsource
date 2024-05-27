import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from xlsx_write import write_excel_template
from datetime import datetime

# https://www.clien.net/service/board/lecture
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=1
# https://www.clien.net/service/board/lecture?&od=T31&category=0&po=2

userAgent = UserAgent()
headers = {"user-agent": userAgent.chrome}

# 데이터 담을 리스트 생성
# lists = []
lists = list()

with requests.Session() as s:

    for page in range(5):  # 0~4
        url = "https://www.clien.net/service/board/lecture?&od=T31&category=0&po="
        url = url + str(page)
        r = s.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")

        # 행 가져오기
        rows = soup.select("div.list_content > div.list_item.symph_row")

        for row in rows:
            title = row.select_one("div.list_title > a > span.subject_fixed")

            time = row.select_one("div.list_time > span > span")
            print(title.text.strip(), time.text.strip()[:10])

            lists.append([title.text.strip(), time.text.strip()[:10]])

        print()
    # 파일 저장 : clien_240527.xlsx
    today = datetime.now().strftime("%Y%m%d")

    write_excel_template(f"clien_{today}.xlsx", "팁과 강좌", lists)

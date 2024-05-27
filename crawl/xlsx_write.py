# 엑셀 저장 모듈
from openpyxl import Workbook
import os

# listdata = [[],[],[]]

print("현재 위치", os.getcwd())


def write_excel_template(filename, sheetname, listdata):
    wb = Workbook()
    ws = wb.active

    ws.title = sheetname
    # 너비 조정
    ws.column_dimensions["A"].width = 100

    for row in listdata:
        ws.append(row)

    base_dir = "./crawl/file/"
    wb.save(base_dir + filename)
    wb.close()


# 모듈 테스트용
if __name__ == "__main__":
    listdata = [["이름", "나이"], ["홍길동", "25"], ["성춘향", 22]]
    write_excel_template("temp.xlsx", "test", listdata)

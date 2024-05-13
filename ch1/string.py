# %%
# 문자 처리
# 문자, 문자열 구분 안함 - 쌍따옴표, 홑따옴표 허용, 3개
# "Life is too short, You need Python"
# 'Life is too short, You need Python'
# '''Life is too short, You need Python'''
# """Life is too short, You need Python"""

multiline = """
    Life is too short
    You need Python
"""
multiline
# %%
# + : 문자열 결합
str1 = "Python" + " is fun"
str1

# %%
# * : 문자열 반복
"python" * 2
# %%
print("=" * 50)
print("My Program")
print("=" * 50)

# %%
# 문자열 인덱싱과 슬라이싱
# Python is fun
print(str1[3])
print(str1[5])
print(str1[-1])  # 오른쪽에서 인덱싱
# %%
# 슬라이싱 [시작위치:끝 위치] => 끝 위치 포함 안함
str1 = "Life is too short"
print(str1[0:])
print(str1[0:4])
print(str1[4:])
print(str1[4:8])
print(str1[:17])
print(str1[0:-4])
# %%
# len() : 길이
len(str1)
# %%
str2 = "20240510Sunny"
date = str2[0:8]
weather = str2[8:]
# 년월일 출력 : 20240510
print(date)
# 날씨 출력 : Sunny
print(weather)
# %%
# 년월일 출력 : 2024-05-10
year = date[:4]
month = date[4:6]
day = date[6:]
print(year, month, day, sep="-")
# %%
jumin = "901205-3234567"
# 주민등록번호에서 1 or 3 남자, 2 or 4 여자
no = int(jumin[7])

if no == 1 or no == 3:
    print("남자")
else:
    print("여자")


if no % 2 == 1:
    print("남자")
else:
    print("여자")

# %%
str1 = "파이썬프로그래밍"
# ♥
for s in str1:
    print(s + "♥", end="")
# %%
# 사용자로부터 숫자 입력받기 => 54321

num1 = input("숫자 입력")

for i in range(len(num1)):
    for j in range(int(num1[i])):
        print("♥", end="")
    print()

# %%
# 문자열 함수
# 1) count() : 문자열에 포함된 특정 문자열 개수
str1 = "hobby"
print("a 문자열에 포함된 b 개수 %d" % str1.count("b"))

# %%
# 2) find() : 문자열 위치
str1 = "Python is the best choice"
print("a 문자열에 b 위치 %d" % str1.find("b"))
print("a 문자열에 b 위치 {}".format(str1.find("b")))
print(f"a 문자열에 b 위치 {str1.find("b")}")
print("a 문자열에 b 위치 ",str1.find("b"))

# %%
# 3) index() : 문자열 위치
print("a 문자열에 b 위치 %d" % str1.index("b"))
# %%
# find() vs index()
# 존재하지 않는 경우 -1 vs ValueError
# print("a 문자열에 b 위치 %d" % str1.index("K"))
print("a 문자열에 b 위치 %d" % str1.find("K"))

# %%
# 4) startswith / endswith
str2 = "Python Is Easy Programming"
print(str2.startswith("P"))
print(str2.endswith("P"))
# %%
# 5) join()
print(",".join("abcdefg"))

# 리스트나 튜플 문자열로 변경 시 많이 사용됨
list1 = ["a","b","c","d","e"]
print("".join(list1))
# %%
# 6) upper / lower / swapcase / title : 대소문자 변경

a = "abcde"
print("소문자 => 대문자 ", a.upper())

a = "ABCDE"
print("대문자 => 소문자", a.lower())

a = "Python is Easy"
print("대문자 소문자 상호 변환 ", a.swapcase())

a = "python is easy"
print("단어의 제일 앞 글자 대문자 변환 ", a.title())

# %%
# python 대소문자 구별 함

"abc" == "ABC"
# %%
# 7) lstrip/ rstrip / strip : 공백 제거
a = "      hi"
print(a)
print(a.lstrip())

a = "hi      "
print(a)
print(a.rstrip())

a = "       hi      "
print(a)
print(a.strip())
# %%

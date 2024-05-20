# 딕셔너리 == Map
# list 와 같이 많이 쓰이는 자료형
# key, value 형태
# {}
# %%
# 생성
dict1 = {}
dict2 = {"name": "Song", "age": 12}
dict3 = {0: "Hello Python", 1: "Hello Coding"}
dict4 = {"arr": [1, 2, 3, 4, 5]}

# %%
print(dict2)
print(dict3)
print(dict4)

# %%
# 특정 키의 요소 출력
print(dict2["name"])
print(dict3[0])
print(dict4["arr"])

# %%
dict1["addr"]  # KeyError: 'addr'

# %%
dict1.get("addr")  # key값이 없어도 에러가 안남

# %%
# 데이터 추가 - 키와 값의 형태로 추가
dict2["birth"] = "0514"
dict2

# %%
dict3[2] = ["Hello Java", "Hello Oracle"]
dict3

# %%
# dict4 L rank => 튜플 (16, 17, 18)
dict4["rank"] = (16, 17, 18)
dict4

# %%
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}
# {1:3, 2:4, 6:1} 숫자가 몇번 등장하는지
for i in numbers:
    counter[i] = numbers.count(i)
counter

# %%
# 삭제
del dict2["birth"]
dict2

# %%
# 1) keys() : key 리스트만 가져옴
dict2.keys()

# %%
# 2) values() : value 리스트만 가져옴
dict2.values()

# %%
# 3) items() : key, value 쌍으로 가져옴
dict2.items()

# %%
for k in dict2.keys():
    print(k)

# %%
for k, v in dict2.items():
    print(k, v)

# %%
# in : key 값이 있는지 확인
"name" in dict1

# %%
"name" in dict2

# %%
# clear() : key, value 전부 제거
dict2.clear()
dict2

# %%
q1 = {"봄": "딸기", "여름": "토마토", "가을": "사과", "겨울": "귤"}

# 가을에 해당하는 과일 출력
print(q1["가을"])
print(q1.get("가을"))

for k in q1.keys():
    if k == "가을":
        print(q1[k])

# 사과가 포함 되었는지 확인
str = "사과가 포함됨" if "사과" in q1.values() else "사과가 포함되지 않음"
str

# %%

# %%

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

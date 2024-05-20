# set(집합)
# 중복 허용하지 않음
# 순서 없음 : (index) 인덱싱을 할 수 없음
# %%
# 생성
set1 = set()
set2 = set([1, 2, 3, 4])
set3 = set([1, 4, 5, 6, 6])  # 중복값 자동탈락

# %%
print(set2)
print(set3)

# %%
# 리스트나 튜플로 변환 : 인덱싱이 필요하다면
list1 = list(set2)
t1 = tuple(set3)
print(list1)
print(t1)

# %%
set4 = set("abcdefg")
set4

# %%
# dict => set
dict1 = {"no": 1, "name": "hong", "age": 25}
set(dict1)  # 키값만 가져옴

# %%
list1 = [1, 2, 3, 4, 5]
set(list1)

# %%
# 교집합, 합집합, 차집합

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1 & s2)
print(s1.intersection(s2))

print(s1 | s2)
print(s1.union(s2))

print(s2 - s1)
print(s1.difference(s2))

# %%
# 하나 추가 : add()
s1.add(7)
s1

# %%
# update() : 여러개 추가하기
s1.update([9, 10, 11])
s1
# %%
# remove() : 제거하기
s1.remove(2)
s1

# %%

# 튜플 : ()
# 튜플은 요소값을 바꿀 수 없다(sort, remove, insert, pop 같은 함수 없음)
# 가공이 불가능하고 읽는것만 가능함
# 리스트와 유사

# %%
# 생성
t1 = ()
t2 = (1,)  # 1개의 요소만을 가질 때 요소 뒤에 쉼표 반드시 필요함
t3 = (1, 2, 3)
t4 = 1, 2, 3  # 소괄호 생략 가능
t5 = ("a", "b", ("ab", "cd"))

# %%
print(t2)
print(t3)
print(t4)
print(t5)

# %%
del t3[0]  # TypeError: 'tuple' object doesn't support item deletion
# tuple은 삭제 불가능

# %%
t3[0] = 6  # TypeError: 'tuple' object does not support item assignment
# tuple은 수정 불가능

# %%
t3[1]
t3[1:]

# %%
t6 = t1 + t2
t6

# %%
t6 = t3 * 3
t6

# %%
len(t6)

# %%

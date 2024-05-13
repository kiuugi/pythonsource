# 연산자
a, b = 5, 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)  # 1.6666666666666667
print(a // b)  # 몫만
print(a % b)  # 나머지만
print(a**b)  # a의 b 제곱 5의 3제곱

# 복합대입연산자
a += 5
print(a)
a *= 5
print(a)
a %= 5
print(a)

# 동전교환
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
money = 7777

# 500원: 15개, 100원 : 2개, 50원 : 1개, 10원 : 2개, 나머지 돈 : 7원
c500 = money // 500
money %= 500
c100 = money // 100
money %= 100
c50 = money // 50
money %= 50
c10 = money // 10
money %= 10

print("\n동전교환결과")
print(
    "500원: %d 개, 100원 : %d 개, 50원 : %d 개, 10원 : %d 개, 나머지 돈 : %d 원"
    % (c500, c100, c50, c10, money)
)
print(
    "500원: {} 개, 100원 : {} 개, 50원 : {} 개, 10원 : {} 개, 나머지 돈 : {} 원".format(
        c500, c100, c50, c10, money
    )
)
print(
    f"500원: {c500} 개, 100원 : {c100} 개, 50원 : {c50} 개, 10원 : {c10} 개, 나머지 돈 : {money} 원"
)


# 관계연산자
# >, >=, <, <=, ==, !=
a, b = 10, 0
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


# 논리연산자
# and, or, not
a, b, c = 100, 80, 130

print("논리연산자")
print("and : ", a > b and b > c)
print("or : ", a > b or b > c)
print("not : ", not b > c)
print("not : ", not False)
print("not : ", not True)

# 삼항연산자는 없음
# 참일때 if 조건 else 거짓일때
str = "안녕하세요" if True else "반갑습니다."
print(str)

# %%
if True:
    print("True")

# %%
a = 200
# a가 100 보다 크고 200보다 작거나 같은지 확인
if a > 100 and a <= 200:
    print("a는 100 보다 크고 200보다 작거나 같다")

# %%
if 100 < a <= 200:
    print("a는 100 보다 크고 200보다 작거나 같다")

# %%
# 세 개의 숫자 중 가장 큰 수 출력
a, b, c = 12, 6, 18

max = a
if max < b:
    max = b
if max < c:
    max = c

print("a,b,c 중 가장 큰 수는 {}".format(max))
# %%
if True:
    print("True")
else:
    print("False")

# %%
score, grade = 90, "A"
# score가 90이상이고 grade가 A => 합격
if score >= 90 and grade == "A":
    print("합격")
else:
    print("불합격")

# %%
# 숫자를 입력 받은 후 짝/홀 출력

num1 = int(input("숫자 입력"))
if num1 % 2 == 0:
    print("짝수")
else:
    print("홀수")

# %%
# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50 보다 작다")

# %%
# 다중 if ==> switch(X)
# elseif(X) ==> elif
num = 90
if num >= 90:
    print("A")
elif num >= 80:
    print("B")
elif num >= 70:
    print("C")
elif num >= 60:
    print("D")
else:
    print("F")

# %%
# age, height 입력받은 후
# age 가 20이상이고 height 170 이상 : A 지망 지원 가능 출력
# age 가 20이상이고 height 160 이상 : B 지망 지원 가능 출력
# age 가 20이상이고 height 160 미만 : 지원불가 출력
# age 가 20미만 : 20세 이상 지원 가능

age = int(input("나이 입력"))
height = int(input("키 입력"))

if age >= 20:
    if height >= 170:
        print("A 지망 지원 가능")
    elif height >= 160:
        print("B 지망 지원 가능")
    else:
        print("지원불가")
else:
    print("20세 이상 지원 가능")


# %%
# 점수 입력 받은 후
# 81 ~ 100 : A학점
# 61 ~ 80 : B학점
# 41 ~ 60 : C학점
# 21 ~ 40 : D학점
# 0 ~ 20 : E학점

jumsu = int(input("점수 입력"))
if jumsu > 80:
    print("A학점")
elif jumsu > 60:
    print("B학점")
elif jumsu > 40:
    print("C학점")
elif jumsu > 20:
    print("D학점")
else:
    print("E학점")

# %%
# 두 개의 숫자 입력받기, 연산자(+,-,*,/,//,**,%) 입력받기
# 연산 후 결과 출력 (출력예시 5 + 3 = 8)
num1 = int(input("첫번째 숫자 입력"))
op = input("+,-,*,/,//,**,% 중 하나의 연산자 입력")
num2 = int(input("두번째 숫자 입력"))

result = None
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
elif op == "//":
    result = num1 // num2
elif op == "**":
    result = num1**num2
elif op == "%":
    result = num1 % num2

print("{} {} {} = {}".format(num1, op, num2, result))

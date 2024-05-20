PI = 3.141592


class Test:
    def solv(self, r):
        return PI * (r**2)

    def sum1(self, a, b):
        return a + b


# 실행하는 당사자(__name__)가 main 일때만 실행
if __name__ == "__main__":
    print(PI)
    a = Test()
    print(a.solv(2))
    print(a.sum1(2, 4))

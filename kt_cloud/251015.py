# * 찍기 input() 함수를 활용
star = int(input("숫자를 입력하세요 : "))
for i in range(star+1):
    print("*" * i)

# * 역으로 찍기 input() 함수를 활용
star = int(input("숫자를 입력하세요 : "))
for i in range(star, 0, -1):
    print("*" * i)

for i in range(star+1):
    print("*" * (star - i))
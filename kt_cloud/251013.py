import re

# # # 1부터 100까지 for문으로 출력
for i in range(1, 101):
    print(i)

# # #1부터 1000까지 3의 배수 합 구하기
sum = 0
i = 1

while i <= 1000:
    if i % 3 == 0:
        sum += i
    i = i + 1

print(sum)

# # #for문을 활용하여 a list 평균 점수 구하기
a = [10, 50, 70, 20, 0, 100, 80]
sum = 0
avg = 0
for i in a:
    sum += i

avg = sum / len(a)
print(int(avg))

# #홀수에만 2를 곱하여 sum에 더하는 코드
number = [0, 1, 2, 3, 4, 5]
sum = 0

for i in number:
    if i % 2 == 1:
        sum += (number[i] * 2)

print(sum)

# b.txt 파일 생성하여 "ABCD"내용 쓰기
f = open('b.txt', 'w')
f.write("ABCD")
f.close()
# b.txt 파일 파이썬 내에서 출력
p = open("b.txt", "r")
print(p.readline())
p.close()
# 같은내용
with open('b.txt', 'w') as f:
    f.write("ABCD")
with open('b.txt', 'r') as f:
    print(f.readline())

# a,b,c,d,e 변수의 값이각각이메일인지판단해서출력하기
a = "kim535@naver.com"
b = "nani@google.co.kr"
c = "@@.com"
d = "aa@@com."
e = "kimt53@naver"

p = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
print(p.match(a))
print(p.match(b))
print(p.match(c))
print(p.match(d))
print(p.match(e))

email_list = [a, b, c, d, e]

for i in email_list:
    if "@@" in i:
        print(i, "이메일 X")
    elif "." not in i:
        print(i, "이메일 X")
    elif i.count(".") > 2:
        print(i, "이메일 X")
    else:
        print(i, "이메일 O")

# 주민등록번호 형태 확인
a = "910313-1952534"
b = "010525-3923432"
c = "020515-4923432"
d = "910828-3929291"
e = "921102-4929291"

total_list = [a, b, c, d, e]

for i in total_list:
    if i[0] == "9" and (i[7] == "1" or i[7] == "2"):
        print(i, "주민등록 번호가 맞습니다")
    elif i[0] == "0" and (i[7] == "3" or i[7] == "4"):
        print(i, "주민등록 번호가 맞습니다")
    else:
        print(i, "주민등록 번호가 아닙니다")
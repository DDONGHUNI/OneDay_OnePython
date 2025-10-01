# 함수
def add(a, b):
    print("%d+%d=%d" % (a, b, a+b))

add(3, 5)

# *을 붙이면 tuple 형태로 생성
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(add_many(1, 2, 3))

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)

# 지역변수
a = 1
def local_global(a):
    a = a + 1
    return a

a = local_global(a)
print(a)

# 함수 연습문제 1 1->n까지 각 수자 더하기
n = int(input())
def c_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

answer = c_sum(n)
print(answer)

# 연습문제 2 점수별로 등급 판별 함수
n = int(input())
def c_grade(n):
    if n >= 100:
        return 'S'
    elif n < 100 or n >= 80:
        return 'A'
    elif n < 80 or n >= 60:
        return 'B'
    else:
        return 'C'

answer = c_grade(n)
print(answer)
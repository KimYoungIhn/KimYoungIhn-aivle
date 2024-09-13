# 흐름제어 !!!
# 1.Bool 연산자¶
# bool 연산자
# 주어진 조건을 평가하여 참 또는 거짓의 결과를 반환하는 연산자
# 결과 : True / False
# 비교 연산자(조건문)
# == 같은가?
# != 같지 않은가?
# 논리 연산자
# and : 양쪽이 둘 다 참일 때만 참.
# or : 둘 중 하나만 참 이어도 참.
# not : 논리 값의 반대.

# 'a' 와 'A' 가 같은가?
print(('a' == 'A'))

# 'a' 와 'A' 가 같지 않은가?
print(('a' != 'A'))

# 'a' 와 'A' 가 같거나, 10과 10.0 이 같은지 비교
print(('a' == 'A') or (10 == 10.0))

# 20과 20.0이 같고, '123'이 '일이삼'과 같은지 비교
print((20 == 20.0) and ('123' == '일이삼'))


# 2.조건제어(if문)
# (1) if
# if 조건문1 :
# ____코드1

# 조건문1이 True이면,
# 코드1 실행(아니면, 그냥 넘어 감.)

score = 89
if (score >= 90):
    print('pass')
    
# (2) if ~ else
# if 조건문1 :
# ____코드1
# else :
# ____코드2

# 조건문1이 True이면,
# 코드1 실행,
# 아니면, 코드2 실행

score = 99
if (score >= 90):
    print('pass')
else :
    print('fail')
    
    
#  (3) if ~ elif ~ else
# if 조건문1 :
# ____코드1
# elif 조건문2 :
# ____코드2
# else :
# ____코드3

# 조건문1이 True이면,
# 코드1 실행
# 아니면, 또 조건문2가 True이면,
# 코드2 실행
# 아니면, 코드3 실행   

score = 50
if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
else :
    print('C')
    

# 3.반복제어
# (1) for loop
# 문법
# for 변수 in range() :
# ____코드

# 실행 절차
# ① 변수 in range() : 데이터 목록(여기서는 range()의 결과)으로 부터 값을 하나씩 꺼내서 변수 i에 담아
# ② 코드를 실행하고
# ③ ①~②반복 (데이터 목록의 다음 값을 변수에 담고 코드실행)
# 반복문 종료 조건
# 데이터 목록 첫번째 값부터, 마지막까지 반복한 후에 종료
# 반복문 안에서 break 구문을 만나면 종료

for i in range(5) :
    print(i)
    
    
for i in [0,1,2,3,4] :
    print(i)
    
# 1부터 100까지 자연수를 모두 더하기
total = 0
for i in range(1, 101) :
    # 여기 들어갈 코드는?
    total += i

print(total)


r = [1,2,3]
m = []
for i in range(1, 101) :
     m.appand(i) 
print(m)

# 코드를 n 번 반복시킬때
import random

n = 10
for i in range(n) :
    rdnum = random.randint(0, 100)  # 0~100 사이 정수 중 랜덤으로 추출
    print(rdnum)
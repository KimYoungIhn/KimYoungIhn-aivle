# 리스트 구조 
# 리스트 생성하기
list_a = [ 1, 2, 3, 4, 5 ]
list_b = ['a','b','c','d','e']
list_c = [1,'a',2,'b']

# 전체 조회
print(list_a)
print(list_b)
print(list_c)

#range 함수
range(1, 12, 2)
list(range(1, 12, 2))

# 리스트안에 리스트
list_d = [1, 2, 3]
list_e = [list_d, 4, 5]
print(list_e)

# 리스트 조회 
# index 는 0에서 부터 시작
a = [23, 3, 16, 45, 11]
print(a[0], a[3])
print(a[-1], a[-3])

#인덱스 범위 조회(슬라이싱)
a = [23, 3, 16, 45, 11]

print(a[0:3])
# 또는
print(a[:3])
print(a[:])

# 리스트 수정
    #값 추가
a = [23, 3, 16, 45, 11]
a = a + [99]
print(a)
a = a + [15]
print(a)
a.append(5)
print(a)

    #값 수정
a = [23, 3, 16, 45, 11]
a[2] = 34
print(a)
    
    #값 삭제
a = [23, 3, 16, 45, 11]
print(len(a))
del a[2]
print(a)
print(a[2])
print(len(a))
    #특정 값 찾아서 삭제
a = [23, 3, 16, 45, 11]
a.remove(45)
print(a)
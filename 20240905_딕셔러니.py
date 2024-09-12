#딕셔러니 생성
# (1) 생성
# 중괄호 {} 안에 , key : value 형태로 선언합니다.
# Value : 다양한 형태의 변수
# Key : Value 변수의 이름

dict_a = { 'v1' : 32,
           'l1' : [1, 2, 3],
           'd1' : {'a' : 1, 'b' : 2} }
print(dict_a)


# 딕셔너리 정보 조회
# .keys() : 딕셔너리의 key 만 조회
# .values() : 딕셔너리의 값 만 조회
# .items() : key와 값을 쌍(tuple)으로 조회

dict_a.keys()
dict_a.values()
dict_a.items()

# 조회
dict_a = { 'v1': 32, 'l1': [1,2,3], 'd1': {'a':1, 'b':2}}

print( dict_a['v1'])
print('=' * 30)

print( dict_a['l1'])
print( dict_a['l1'][:2])
print('=' * 30)

print( dict_a['d1'])
print( dict_a['d1']['a'])
print( 3 + (dict_a['d1']['b']))

# 수정
dict_a = { 'v1': 32, 'l1': [1,2,3], 'd1': {'a':1, 'b':2}}
# 추가
dict_a['v2'] = 500
print(dict_a)

# 수정
dict_a['v2'] = 300
print(dict_a)

# 삭제
del dict_a['v2']
print(dict_a)

# 수정
dict_a['v2'] = 300
print(dict_a)

# 삭제
del dict_a['v2']
print(dict_a)
# 실수 -> 정수
fl = 2.5
fl_to_int = int(fl)
print(fl_to_int)

# 문자 -> 정수
string = '3.141592'
string_to_int = int(float(string))
print(string_to_int)

print(5**3)

print('c' in 'cat')

print('c' not in 'cat')
 
print(str(5) in '50')

a=''
print(bool(a))

print(bool(None))

# 단일 주석
''' 여러줄 주석 '''

lang = "python"

# -> p
print(lang[0])

# -> h
print(lang[-3])

# -> ython
print(lang[1:6])

# -> pyth
print(lang[0:4])

# -> th
print(lang[2:4])

snack = '''꿀꽈배기는
너무 
맛있어요'''

print(snack)

letter = "my name is park hyeon beom"

print(letter.lower())

print(letter.upper())

print(letter.capitalize())

print(letter.swapcase())

print(letter.split()) 

print(letter.count("is"))

s = '나도고등학교'

print(s.startswith('나도'))

print(s.endswith('고등학교'))

print(s.find('고등'))

print(s.center(12,'*'))

print(snack,letter)

java = "자바"

python = "파이썬"

print("개발 언어에는 {}, {} 등이 있다".format(java,python))

print("개발 언어에는 {1}, {0} 등이 있다".format(java,python))

print(f'개발 언어에는 {java}, {python} 등이 있다')

print("하지만 \'나만 당할 순 없지\' 라는 생각에 \"엄청 쉽지\" 라고 했다.")

print("하지만 \n\'나만 당할 순 없지\' 라는 생각에 \n\"엄청 쉽지\" 라고 했다.")

my_list = ['몽쉘', '초코파이', '오예스']

print(len(my_list))

print('몽쉘' in my_list)

print(my_list[1])
my_list[1] = "신상 초코파이"
print(my_list[1])

my_list.append('맛동산')
print(my_list)

my_list.remove('맛동산')
print(my_list)

list1 = ["오예스" , "초코파이"]
list2 = ["맛동산", "포스틱"]
list1.extend(list2)
print(list1)

tuple1 = ('A', "B", "c")
tuple2 = ("가","나","다")
print(len(tuple1+tuple2))

numbers = (1,2,3,4,5,6,7,8,9,10)

(test1, test2, test3, *others) = numbers

print(test1)
print(test2)
print(test3)
print(others)
print(len(others))

set1 = {"제육덮밥", "돈까스", "국밥"}
set2 = {"잔치국수", "햄버거", "제육덮밥"}

# 공통 -> intersection -> 교집합

# 모두 -> union -> 합집합

# A만 좋아하는거 -> difference -> 차집합

# add -> 추가

# remove -> 값 삭제

# clear -> 전체 삭제 -> 값 전체 삭제 -> 세트 자체는 존재

# del -> 세트 삭제 

''' 딕셔너리 -> Key - Value -> ex = {'key1':value1, 'key2':value2}
 -> ex = {
    'key1' : "value1",
    'key2' : value2
    }'''

# 딕셔너리에 저장된 값에 접근하기 위해서는 Key를 사용 -> ex.get('key1')

# 딕셔너리에 값 추가 및 수정 -> ex['key3'] = value3

# 딕셔너리의 여러 값 동시 수정 -> ex.update({'key1' : A, 'key2' : B, 'key3' : C })

# 딕셔너리의 key 조회
ex = {
    'key1' : "value1",
    'key2' : "value2"
    }

ex['key3'] = "value3"
print(ex)

ex.update({'key1' : "A", 'key2' : "B", 'key3' : "C" })

print(ex)

# Key 조회
print(ex.keys())

# Value 조회
print(ex.values())

# Key:Value 조회
print(ex.items())

print(ex.setdefault("key4"))

print(ex)


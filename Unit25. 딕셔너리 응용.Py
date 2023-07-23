# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# x.setdefault('e')
# print(x)
# y = {'a1' : 10, 'b2' : 20, 'c2' : 30, 'd2' : 40}
# y.setdefault('e2', 50)
# print(y)

# setdefaulf(key, value) 메소드를 사용해서 딕셔너리에 키:값 을 추가할 수 있습니다.
# 이 때, 값 없이 키만 넣으면 값이 None인 키가 추가됩니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# x.update(a = 90)
# print(x)
# x.update(e = 150)
# print(x)
# x.update(a = 900, f = 250)
# print(x)

# update(key = value) 메소드를 사용해서 키에 저장된 값을 변경할 수 있습니다.
# 이 때, 딕셔너리에 존재하지 않는 키를 입력하면 새로운 키:값으로 저장됩니다.
# update(key1 = value1, key2 = value2)와 같이 복수의 키와 값을 입력하거나 변경할수도 있습니다.

# x = {1 : 'one', 2 : 'two', 3 : 'three'}
# x.update({1 : 'ONE', 4 : 'FOUR'})
# print(x)
# x.update([[2, 'TWO'], [3, 'THREE']])
# print(x)
# x.update(((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five')))
# print(x)

# 키가 문자열일때만 update(key = value)와 같이 사용할 수 있습니다.
# 키가 숫자열일 경우에는 다음과 같은 방법으로 변경하거나 추가할 수 있습니다.
# update(딕셔너리) → update({key1 : value1, key2 : value2})
# update(리스트) → update([[key1, value1], [key1, value2]])
# update(튜플) → update(((key1, value1), (key2, value2)))

# x = {1 : 'one', 2 : 'two', 3 : 'three'}
# x.update(zip([1, 2, 3], ['One', 'Two', 'Three']))
# print(x)

# zip 함수를 사용해서 표현하면 좀더 간결하게 표현이 가능합니다.
# zip([key1, key2], [value1, value2]) 또는 zip((key1, key2), (value1, value2))

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# print(x.pop('a'))
# print(x)
# print(x.pop('z', 0))
# print(x.pop('z'))

# pop을 이용해서 키:값을 삭제해주며 그 값을 반환할 수 있습니다.
# 없는 키를 넣으면 오류가 나며, pop(없는 key, 기본값)을 넣어주면 기본값을 반환합니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# del x['c']
# print(x)

# del 변수[key] 키워드를 사용하여 키:값을 삭제할 수 있습니다.
# 없는 키를 넣으면 오류가 납니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# print(x.popitem())
# print(x)

# popitem 메소드를 사용하면 마지막 키:값을 삭제하고 키:값을 튜플로 반환합니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# x.clear()
# print(x)

# clear 메소드로 딕셔너리에 모든 것을 삭제하고 빈 딕셔너리로 변경시켜 줄 수 있습니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# print(x.get('a'))
# print(x)
# print(x.get('z', 0))
# print(x)
# print(x.get('z'))
# print(x)

# get(key) 메소드를 사용하면 키값을 반환해 준다.
# 존재하지 않는 키를 넣어주면 None을 반환하고 get(없는 키, 기본값)으로 입력해주면 기본값을 반환한다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# print(x.items())
# print(x.keys())
# print(x.values())

# item 메소드를 사용하면 딕셔너리의 키값을 [(key1, value1), ........ (keyn, valuen)]으로 반환해준다.
# key 메소드를 사용하면 [key1, ..... keyn]으로 반환해준다.
# values 메소드를 사용하면 [value1, ..... valuen]으로 반환해준다.

# keys1 = ['a', 'b', 'c', 'd']
# x = dict.fromkeys(keys1)
# print(x)
# keys2 = ['e', 'f', 'g', 'h']
# y = dict.fromkeys(keys2, 100)
# print(y)

# dict.fromkeys(list, 기본값) 메소드를 사용하면 list의 요소를 키로하고 기본값을 값에 넣어서 딕셔너리를 생성한다.
# 기본값을 입력하지 않으면 None을 기본값으로 갖는다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}

# for i in x:
#     print(i, end=' ')

# 딕셔너리를 for문에 넣어서 변수1개만을 할당하게 하면 키가 할당되어 나옵니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}

# for i, j in x.items():
#     print(i, j, end=' ')
# print()
# for k in x.keys():
#     print(k, end=' ')
# print()
# for l in x.values():
#     print(l, end=' ')

# items 메소드를 사용하면 키와 값으로 이뤄진 튜플이 요소로 되어 있는 리스트가 생성됩니다.
# key(= i), value(= j)에 할당되도록 for문을 구성하면 키값이 모두 꺼내져 나옵니다.
# keys 메소드를 사용하면 키를 요소로하는 리스트가 생성됩니다.
# key(= k)에 할당되도록 for문을 구성하면 키가 모두 꺼내져 나옵니다.
# values 메소드를 사용하면 값을 요소로 하는 리스트가 생성됩니다.
# value(= l)에 항당되도록 for문을 구성하면 값이 모두 꺼내져 나옵니다.

# keys = ['a', 'b', 'c', 'd']
# x = {key : value for key, value in dict.fromkeys(keys).items()}
# print(x)
# y = dict.fromkeys(keys)
# print(y)

# for문을 이용해서 딕셔너리를 만들 수 있다.
# 사실 dict.fromkey(keys)에서 딕셔너리가 완성된 상태이기 때문에 복잡해지기만 하는 형식이다.
# 활용할 경우가 있으니 눈도장찍자

# a = {key : 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()}
# print(a)
# b = {value : 0 for value in {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}.values()}
# print(b)
# c = {value : key for key, value in {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}.items()}
# print(c)

# a는 키만 추출해서 딕셔너리를 만드는 코드인데 사실 dict.fromkey(['a', 'b', 'c', 'd'])에서 이미 딕셔너리가 완성된 상태이다.
# b는 딕셔너리 값을 키로하는 딕셔너리를 만들어준다.
# c는 딕셔너리 키값을 서로 반전해서 키가 값이되고 값이 키가되도록 해준다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}

# for key, value in x.items():
#     if value == 20:
#         del x[key]
# print(x)

# 딕셔너리를 이용해 for문을 작동하는 도중에 if문을 사용해서 key를 삭제하면 오류가 발생합니다.
# 특정 key를 삭제하고 싶은 경우 표현식을 사용해야 합니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}

# x1 = {key:value for key, value in x.items() if value != 20}
# print(x1)

# terrestrial_planet = {
#     'Mercury': {
#         'mean_radius': 2439.7,
#         'mass': 3.3022E+23,
#         'orbital_period': 87.969
#     },
#     'Venus': {
#         'mean_radius': 6051.8,
#         'mass': 4.8676E+24,
#         'orbital_period': 224.70069,
#     },
#     'Earth': {
#         'mean_radius': 6371.0,
#         'mass': 5.97219E+24,
#         'orbital_period': 365.25641,
#     },
#     'Mars': {
#         'mean_radius': 3389.5,
#         'mass': 6.4185E+23,
#         'orbital_period': 686.9600,
#     }
# }
 
# print(terrestrial_planet['Venus']['mean_radius']) # key1 = 금성, keyA = 행성의 반지름 을 불러온 값을 출력합니다.

# 딕셔너리 = {key1 : {keyA : value1}, key2 : {keyB : value2}, key3 : {keyC : value3}}과 같이 중첩해서 사용할 수 있습니다.
# 위 딕셔너리는 태양계의 지구형 행성의 반지름, 질량, 공전주기를 키와 값으로 하는 딕셔너리 입니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# y = x
# print(x == y)
# print(x is y)
# y['a'] = 99
# print(x)
# print(y)

# 딕셔너리의 할당과 복사는 리스트와 크게 다르지 않습니다.
# y에 x를 할당하면 똑같은 리스트가 2개의 변수에 할당될 뿐입니다.

# x = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
# y = x.copy()
# print(x == y)
# print(x is y)

# copy 메소드를 사용해 주면 복사된 새로운 리스트가 y에 할당됩니다.

# xx = {'a' : {'a1' : 10, 'a2' : 100}, 'b' : {'b1' : 20, 'b2' : 200}, 'c' : {'c1' : 30, 'c2' : 300}, 'd' : {'d1' : 40, 'd2' : 400}}

# yy = xx.copy()
# print(xx == yy)
# print(xx is yy)
# yy['b']['b2'] = 2000
# print(xx)
# print(yy)

# 딕셔너리 xx를 copy 메소드를 사용해서 딕셔너리 yy를 만들어 줬고 xx == yy지만 xx is yy라고 결과도 나왔다.
# 하지만 yy['b']['b2'] = 2000의 실행결과 xx의 똑같은 값도 변경되었다.
# 다차원 리스트처럼 중첩 딕셔너리도 copy 메소드가 아닌 copy모듈에서 deepcopy 메소드를 써줘요 온전하게 복사된다.

# xx = {'a' : {'a1' : 10, 'a2' : 100}, 'b' : {'b1' : 20, 'b2' : 200}, 'c' : {'c1' : 30, 'c2' : 300}, 'd' : {'d1' : 40, 'd2' : 400}}

# import copy
# yy = copy.deepcopy(xx)
# yy['b']['b2'] = 2000
# print(xx)
# print(yy)

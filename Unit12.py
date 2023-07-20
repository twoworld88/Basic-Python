# lux = {'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
# print('lux : ', lux)

# 딕셔너리는 {}안에 key : value를 사용하여 생성합니다.
# key와 value사이에 :대신 =를 넣거나 key:value간 ,를 빼먹는 오류가 자주 발생하니 유의해야합니다.

# lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
# print('lux : ', lux)

# key가 중복으로 사용되면 가장 뒤의 값만 사용합니다.
# 가장 뒤의 key를 제외한 값은 저장되지 않습니다.
# key에는 문자열, 정수, 실수, 불을 사용가능하나 리스트와 딕셔너리는 사용이 불가합니다.
# value에는 문자열, 정수, 실수 불, 리스트, 딕셔너리 모두 사용이 가능합니다.

# x = {}
# y = dict()

# 위와 같이 {}나 dict함수를 사용해 빈 딕셔너리를 만들 수 있으나 보통 {}만을 사용합니다.

# lux = dict(health = 490, mana = 334, melee = 550, armor = 18.72)
# print('lux : ', lux)

# dict함수를 사용할 경우 '나 "를 사용하지 않아도 자동으로 문자열로 변형되어 적용됩니다.

# lux = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
# print('lux : ', lux)

# dict 함수 안에 zip함수를 넣어서 딕셔너리를 생성하는 방법도 있습니다.

# lux = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
# print('lux : ', lux)

# dict 함수 안에 튜플로 key와 value를 묶어서 표현해 생성하는 방법도 있습니다.

# lux = dict({'health' : 490, 'mana' : 334, 'melee' : 550, 'armor' : 18.72})
# print('lux : ', lux)

# dict 함수 안에 {}로 딕셔너리를 넣어서 생성도 가능합니다.

# lux = {'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
# print(lux['health'])
# lux['health'] = 2400
# print(lux)
# lux['mana regen'] = 3.8
# print(lux)
# print('health' in lux)

# 키에 새로운 값을 할당하면 값이 변합니다.
# 새로운 키를 만들고 값을 할당하여 추가할 수 있습니다.
# 딕셔너리 내 키가 존재하는지 연산자를 활용하여 확인 가능합니다.

# lux = {'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}
# print(len(lux))
# print(len({'health' : 490, 'health' : 800, 'mana' : 334, 'melee' : 550, 'armor' : 18.72}))

# 딕셔너리를 변수에 할당하여 len함수를 사용하여 키의 개수를 확인할 수 있습니다.
# 또한, len에 딕셔너리를 바로 넣어서 키의 개수도 확인 가능합니다.
# 단, 유효한 키의 개수만 확인됩니다. 중복되는 키는 마지막 키만 카운트합니다.


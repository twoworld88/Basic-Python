# fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry', 'grape', 'orange'}

# print(fruits)

# 세트는 {}안에 ,로 구분하는 자료형입니다.
# 세트의 요소는 순서가 없습니다.
# 때문에 매번 다른 순서로 반환됩니다.
# 또한 요소가 중복해서 들어갈 수 없습니다.
# 순서가 없기 때문에 인덱스로 특정 요소를 출력할 수 없습니다.

# fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}

# print('orange' in fruits)
# print('peach' in fruits)
# print('peach' not in fruits)
# print('orange' not in fruits)

# 값 in 세트, 값 not in 세트로 세트내부에 값이 존재하는지 않하는지 확인할 수 있습니다.

# a = set('apple')
# b = set(range(5))
# print(a)
# print(b)

# set(반복가능한객체) 함수를 이용해서 세트를 만들 수 있습니다.
# 반복가능한객체는 추후 강의에 나오니 눈도장만 찍어둡니다.
# 빈 세트는 변수 = set()과 같이 아무것도 넣지 않으면 됩니다.
# 변수 = {}와 같이 만들면 빈 딕셔너리가 생성됩니다.
# 세트안에는 세트를 넣을 수 없습니다.

# a = frozenset(range(8))
# print(a)

# frozenset 함수를 사용하면 튜플처럼 값을 변경하는 함수, 메소드를 사용할 수 없는 세트를 만들어 줍니다.

# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}

# print(a | b)
# print(set.union(a, b))

# print(a & b)
# print(set.intersection(a, b))

# print(a - b)
# print(set.difference(a, b))

# print(a ^ b)
# print(set.symmetric_difference(a, b))

# 연산자 | 그리고 union(a, b) 메소드는 세트의 합집합을 구합니다.
# 연산자 & 그리고 intersection(a, b) 메소드는 세트의 교집합을 구합니다.
# 연산자 - 그리고 difference(a, b) 메소드는 세트의 차집합을 구합니다.
# 연산자 ^ 그리고 symmetric_difference(a, b) 메소드는 세트의 대칭차집합을 구합니다.

# a = {1, 2, 3, 4}
# a |= {5}
# print(a)
# b = {1, 2, 3, 4}
# b.update({5})
# print(b)

# |= 연산자와 update(세트)는 현재 세트에 다른 세트의 합집합을 현재 세트변수에 다시 할당합니다.

# a = {1, 2, 3, 4}
# a &= {0, 1, 2, 3, 4, 5}
# print(a)
# b = {1, 2, 3, 4}
# b.intersection_update({0, 1, 2, 3, 4, 5})
# print(b)

# &= 연산자와 intersection_update(세트)는 현재 세트에 다른 세트의 교집합을 현재 세트변수에 다시 할당합니다.

# a = {1, 2, 3, 4}
# a -= {2, 3}
# print(a)
# b = {1, 2, 3, 4}
# b.difference_update({2, 3})
# print(b)

# -= 연산자와 difference_update(세트)는 현재 세트에 다른 세트의 차집합을 현재 세트변수에 다시 할당합니다.

# a = {1, 2, 3, 4}
# a ^= {3, 4, 5, 6, 7}
# print(a)
# b = {1, 2, 3, 4}
# b.symmetric_difference_update({3, 4, 5, 6, 7})
# print(b)

# ^= 연산자와 symmetric_difference_update(세트)는 현재 세트에 다른 세트의 대칭차집합을 현재 세트변수에 다시 할당합니다.

# a = {1, 2, 3, 4}
# b = {1, 2, 3, 4, 5, 6, 7}

# print(a <= b)
# print(a.issubset(b))

# print(a >= b)
# print(a.issuperset(b))

# a가 b의 부분집합인지 확인하는 방법은 <= 또는 < 연산식과 issubset(b) 메소드를 사용하는 방법이 있습니다.
# b가 a의 상위집합인지 확인하는 방법은 >= 또는 > 연산식과 issuperset(b) 메소드를 사용하는 방법이 있습니다.

# a = {1, 2, 3, 4}
# b = {4, 2, 1, 3}

# print(a == b)
# print(a != b)

# 세트는 요소에게 순서가 없으므로 값만 같은 요소들이 들어 있으면 같습니다.

# a = {1, 3, 4, 6, 9}
# b = {2, 5, 7, 8}
# c = {1, 4, 7, 8}

# print(a.isdisjoint(b))
# print(a.isdisjoint(c))

# isdisjoint 메소드를 이용하면 서로 교집합이 있는지 확인 할 수 있습니다.
# 교집합이 없으면 True, 있으면 False를 반환합니다.

# a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# a.add(5)
# print(a)

# a.remove(3)
# print(a)

# a.discard(2)
# print(a)

# a.discard(6)
# print(a)

# a.pop()
# print(a)

# print(len(a))

# a.clear()
# print(a)

# add(추가할 요소) 메소드를 이용하면 세트에 요소를 추가할 수 있습니다.
# remove(제거할 요소) 메소드를 이용하면 세트에 요소를 제거할 수 있습니다.
# discard(제거할 요소) 메소드를 이용하면 세트에 제거할 요소가 존재하면 삭제하고 없으면 그냥 넘어갑니다.
# pop 메소드를 이용하면 임의의 요소를 제거하면서 그 요소를 반환합니다.(단, 숫자로된 세트는 순서대로 작은것부터 제거됩니다.)
# len(세트) 함수를 이용하면 세트의 길이를 구할 수 있습니다.
# clear 메소드를 이용하면 모든 요소를 삭제하고 빈 세트로 변경해 줍니다.

# a = {1, 2, 3, 4}
# b = a
# print(a == b)
# print(a is b)
# c = a.copy()
# print(a == c)
# print(a is c)

# 세트도 온전히 새로운 리스트를 복사해서 새로운 변수에 할당하려면 copy 메소드를 사용해야만 합니다.

# a = {1, 2, 3, 4}
# for i in a:
#     print(i)
# b = {'a', 'b', 'c', 'd'}
# for j in b:
#     print(j)

# for문으로 세트의 요소를 꺼내와서 반환할 수 있습니다.
# 세트에는 순서가 없으므로 항상 다른 순서로 꺼내옵니다. 단, 숫자는 순서대로 꺼내옵니다.

# a = {i for i in 'apple'}
# print(a)
# b = {j for j in range(10)}
# print(b)

# 세트도 리스트처럼 표현식을 사용할 수 있습니다.

# a = {i for i in 'apple' if i != 'l'}
# print(a)

# if 문을 사용해서 조건을 지정할 수 있습니다.

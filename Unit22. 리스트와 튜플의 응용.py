# 리스트에 요소를 추가하는 메소드는 총 3가지입니다.
# append : 요소를 하나 추가한다.
# extend : 리스트를 연결하여 확장한다.
# insert : 특정 인덱스에 요소를 추가한다.

# a = [10, 20, 30]
# print(a)
# print(len(a))

# a.append(500)
# print(a)
# print(len(a))

# append 메소드를 사용하면 리스트 내에 요소가 추가된 리스트로 변경되는 효과를 줍니다.

# a.append([600, 700])
# print(a)
# print(len(a))

# append 메소드를 사용해 리스트안에 리스트를 추가할 수도 있으며, 이 리스트는 하나의 element로 취급됩니다.

# a = [10, 20, 30]
# a.extend([500, 600])
# print(a)
# print(len(a))

# extend 메소드를 사용해 리스트에 다른 리스트를 연결하여 하나의 리스트로 만들어 줄 수 있습니다.
# 이 때는 리스트가 서로 합쳐졌으므로 합쳐지는 리스트의 element 하나하나가 element로 취급됩니다.

# a = [10, 20, 30]
# a.insert(2, 500)
# print(a)
# print(len(a))

# insert(a, b) 메소드를 사용하면 원하는 인덱스 a에 b라는 element를 추가해 줍니다.

# a = [10, 20, 30]
# a.insert(len(a), 500)
# print(a)
# print(len(a))

# a.insert(len(a), [600,700])
# print(a)
# print(len(a))

# len(a)는 마지막 인덱스보다 1이 크기때문에 a.append(500)과 같은 효과를 얻습니다.
# insert도 append처럼 리스트 내에 리스트를 추가할 수 있습니다.

# a = [10, 20, 30]
# a[1:1] = [500, 600]
# print(a)
# print(len(a))

# 슬라이스를 이용하면 특정인덱스에 여러개의 요소를 추가할 수 있습니다.
# 이때 a[1:1]과 같이 슬라이스의 시작과 끝을 동일하게 원하는 인덱스로 넣으면 슬라이스하지 않고 여러개를 인설트하는 효과를 얻습니다.

# a = [10, 20, 30, 40, 50, 60]

# print(a.pop()) # a의 가장 마지막 인덱스(60)를 리스트에서 삭제한 뒤 반환해줍니다.
# print(a)
# print(len(a))

# del a[2] # a의 2번째 인덱스(20)를 삭제시킵니다.
# print(a)
# print(len(a))

# a.pop(2) # a의 2번째 인덱스(40)을 리스트에서 삭제한 뒤 반환해줍니다.
# 반환되는 값은 print()함수를 사용해야 출력됩니다. 이하 print로 덮어진 메소드나 함수는 모두 print()함수를 사용해야만 출력되는 것들 입니다.
# print(a)
# print(len(a))

# a = [10, 20, 30, 40, 50, 60]
# a.remove(20)
# print(a)
# print(len(a))

# remove 메소드를 사용하면 특정 '값'을 지정해서 삭제할 수 있습니다.
# del키워드는 del a[b]와 같이 특정 '인덱스' b를 지정해서 삭제합니다.
# '값'을 지정하는가 '인덱스'를 지정하는가의 차이가 있습니다.

# a = [10, 20, 30, 40, 50, 60]
# print(a.index(10))

# a.index(b) 메소드는 특정값 b의 인덱스를 반환해줍니다.

# a = [20, 10, 20, 30, 40, 20, 50, 60, 20]
# print(a.count(20))

# a.count(b) 메소드는 특정값 b가 리스트 내에 몇개 있는지 그 개수를 반환해줍니다.

# a = [10, 20, 30, 40, 50, 60]
# a.reverse()
# print(a)

# reverse 메소드는 리스트를 뒤집어진 리스트로 변경시켜 줍니다.

# a = [20, 10, 20, 30, 40, 20, 50, 60, 20]
# a.sort()
# print(a)

# sort 메소드는 리스트를 정렬된 리스트로 변경시켜 줍니다.

# a = [30, 20, 40, 10]
# print(sorted(a))
# print(a)

# sorted 함수는 새로운 리스트를 생성하여 반환합니다.
# 때문에 다시 a를 출력하면 원래 a가 출력됩니다.

# a = [30, 20, 40, 10]
# a.clear()
# print(a)

# clear 메소드는 리스트 내 모든 요소가 삭제된 리스트로 변경시켜 줍니다.

# a = [10, 20, 30]
# a[len(a):] = [40]
# print(a)
# a[len(a):] = [50, 60]
# print(a)

# a[len(a):] = [b]는 a의 마지막 인덱스 뒤에 [b]의 요소가 추가된 리스트로 변경시켜 줍니다.
# 즉 a.append(b)와 동일한 효과를 얻습니다만 b의 요소의 개수를 모두 추가해주기 때문에 복수추가가 가능하다는 장점이 있습니다.

# a = [0, 0, 0, 0, 0]
# b = a
# print(b is a)

# 위 와 같이 했을 경우 a와 같은 리스트 b가 생성될거라 생각하지만 실제로는 리스트는 하나 뿐입니다.
# 하나의 [0, 0, 0, 0, 0]이라는 리스트가 두 개의 변수에 동시에 할당되어 있을 뿐입니다.
# 때문에 b is a 는 True를 반환합니다.

# b[2] = 99
# print(a)
# print(b)

# 변수 a, b에 할당된 리스트는 동일한 개체이기 때문에 변수 b에 할당된 리스트에 요소를 추가하면 a에 할당된 리스트에도 똑같이 추가됩니다.
# 여기서 다시 한 번 a, b에는 동일한 리스트가 할당되어 있음을 알 수 있습니다.

# a = [0, 0, 0, 0, 0]
# b = a.copy()
# print(a)
# print(b)
# print(b is a)
# print(b == a)

# copy 메소드를 사용하면 b에 a에 할당된 것과 같은 리스트를 할당하는 것이 아니라 a와 같은 리스트를 복사하여 할당합니다.
# 이제 a에 할당된 리스트와 b에 할당된 리스트는 동일한 모양이지만 서로 다른 객체가 할당되어 있습니다.
# 때문에 a is b는 False를 반환합니다.
# 하지만 같은 값을 갖고 있기 때문에 a == b는 Ture를 반환합니다.

# b[2] = 99
# print(a)
# print(b)

# 변수 a, b에 할당된 리스트는 동일한 개체가 아니기 때문에 변수 b에 할당된 리스트에 요소를 추가해도 a에 할당된 리스트는 영향을 받지 않습니다.
# 여기서 다시 한 번 a, b에는 동일한 모양이지만 서로 다른 객체인 리스트가 할당되어 있음을 알 수 있습니다.

# for 변수 in 리스트:
#     반복할 코드

# a = [38, 21, 53, 62, 19]
# for i in a:
#     print(i)

# for문에 리스트를 지정해서 실행해주면 리스트 안 요소를 앞에서부터 하나식 꺼내 i에 할당합니다.

# for i in [38, 21, 53, 62, 19]:
#     print(i)

# 이렇게 for문에 리스트를 직접 넣어줘도 똑같은 결과를 반환합니다.

# a = [38, 21, 53, 62, 19]

# for index, value in enumerate(a):
#     print(index, value)

# enumerate함수를 사용하면 인덱스와 값을 동시에 반환할 수 있습니다.

# a = [38, 21, 53, 62, 19]

# for index, value in enumerate(a):
#     print(index + 1, value)

# 인덱스에 +1을 해주면 인덱스를 1부터 시작하도록 반환할 수 있습니다.

# a = [38, 21, 53, 62, 19]

# for index, value in enumerate(a, start = 1):
#     print(index, value)

# Python에서는 enumerate함수 값 뒤에 , start = 1을 지정해주면 인덱스가 1부터 시작하도록 할 수도 있습니다.

# a = [38, 21, 53, 62, 19]

# for index, value in enumerate(a, start = 2):
#     print(index, value)

# 물론 start = n으로 지정하면 인덱스가 n부터 시작됩니다.

# a = [38, 21, 53, 62, 19]

# for i in range(len(a)):
#     print(a[i])

# len(a) a의 길이 즉 요소 개수를 반환합니다.
# range(len(a))는 range(5)가 됩니다.
# range(5) = 0, 1, 2, 3, 4 이므로 순서대로 i에 할당합니다.
# a[i]를 통해 인덱스인 i에 0~4가 들어가 반환되므로 결과적으로 아래 코드와 동일한 결과가 나옵니다.
# for i in a:
#     print(i)

# a = [38, 21, 53, 62, 19]
# i = 0
# while i < len(a):
#     print(a[i])
#     i += 1

# i는 인덱스를 표시하므로 최초값을 0으로 설정해줍니다.
# while문에서 인덱스에 들어갈 i는 a의 요소 수보다 1이 작아야 하니 i < len(a)를 while 조건식으로 지정해줍니다.
# a의 인덱스를 반환하여 출력하도록 한 후 변경식은 1씩 증가하도록 지정하면 아래 for문과 동일한 결과를 얻습니다.
# for i in a:
#     print(i)

# a = [38, 21, 53, 62, 19]
# smallest = a[0]
# for i in a:
#     if i < smallest:
#         smallest = i
# print(smallest)

# a의 인덱스 0의 값을 smallest에 할당해 줍니다.
# for문으로 a의 요소를 꺼내어 i에 할당합니다.
# 할당된 smallest보다 작으면 그 i를 smallest에 할당되도록 합니다.
# for문이 작동한 뒤 smallest의 할당되어 있는 값은 리스트 a의 요소 중 최소값입니다.

# a = [38, 21, 53, 62, 19]
# largest = a[0]
# for i in a:
#     if i > largest:
#         largest = i
# print(largest)

# 동일한 구조의 코드에 연산자 <를 >로 변경만 해주면 최대값을 얻을 수 있습니다.

# a = [38, 21, 53, 62, 19]
# a.sort()
# print(a[0])
# a.sort(reverse = True)
# print(a[0])
# print(min(a))
# print(max(a))

# sort 메소드를 이용하는 방법과 min, max함수를 이용하면 더욱 간단히 최소, 최대값을 구할 수 있습니다.

# a = [10, 20, 30, 40, 50]
# x = 0
# for i in a:
#     x += i
# print(x)
# print(sum(a))

# x에 a에서 깨내온 i를 더해주기를 반복하는 for문을 통해 a요소의 합계를 구할 수 있습니다.
# sum 함수를 사용하면 간단하게 구할 수 있습니다.

# a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [i for i in range(10)]
# c = list(i for i in range(10))
# print(a == b == c)

# Python은 리스트안에 식, for문, if문을 지정하여 리스트를 생성할 수 있습니다.
# 이를 리스트 컴프리헨션(list comprehension)이라고 합니다.

# a = [i+5 for i in range(10)] # 0~9를 꺼내서 각각 요소에 5를 더한 값을 요소로 갖는 리스트를 생성합니다.
# print(a)
# b = [i*2 for i in range(10)] # 0~9를 꺼내서 각각 요소에 2를 곱한 값을 요소로 갖는 리스트를 생성합니다.
# print(b)

# a = [i for i in range(10) if i % 2 == 0]
# print(a)

# 0~9를 꺼낸 다음 2로 나눠서 나머지가 0인 값을 요소로 갖는 리스트를 생성
# 이처럼 for문과 if문을 동시에 사용할 수 있다.

# a = [i+5 for i in range(10) if i % 2 == 0]
# print(a)

# 식, for문, if문 모두 사용할 수 있다.
# for문에서 range값을 0~9까지 하나씩 꺼내와서 if문으로 판단하고 True값을 반환하여 +5를 시킨 값을 요소로 갖는 리스트를 생성합니다.

# a = [i * j for i in range(2, 10) 
#            for j in range(1, 10)] # 가독성을 위해서 줄을 바꿔서 써줬다.
# print(a)

# 여러개의 for문과 if을 사용할 수 도 있습니다.

# a = [1.2, 2.5, 3.7, 4.6]
# for i in range(len(a)):
#     a[i] = int(a[i])
# print(a)

# a와 같이 실수로 구성된 요소를 갖고 있는 리스트의 요소를 정수화 시키려면 위와 같이 해야합니다.
# 이를 map함수를 사용하면 더욱 간단하게 표현 할 수 있습니다.

# a = [1.2, 2.5, 3.7, 4.6]
# a = list(map(int, a))
# print(a)

# map(함수, 리스트)와 같이 사용하면 리스트의 요소를 하나씩 꺼내서 '함수'의 함수를 적용시켜서 반환해줍니다.
# 이 반환값을 list함수로 리스트화하면 위의 복잡한 for문과 동일한 결과 값을 반환합니다.
# map은 리스트 뿐만 아니라 반복가능한 개체를 넣을 수 있습니다.(튜플 , range 등등)

# a = 38, 21, 53, 62, 19, 53

# print(a.index(62))

# print(a.count(53))

# for i in a:
#     print(i, end=' ')

# print()

# b = tuple(i for i in range(10) if i % 2 == 0)
# print(b)

# c = 1.2, 2.5, 3.7, 4.2, 5.5
# c = tuple(map(int, c))
# print(c)

# print(min(a))
# print(max(a))
# print(sum(a))

# 리스트와 같이 거의 비슷하게 활용이 가능합니다.
# 단, 리스트와 튜플의 차이점 2가지는 []냐 ()냐 그리고 값을 변경할 수 있는냐 없느냐 입니다.
# 때문에 pop, insert, 슬라이스 등이 불가합니다.
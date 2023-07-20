# a = []
# b = list()
# print(a)
# print(b)
# 리스트를 생성하는 방법으로는 변수에 직접 []를 할당하거나 list함수를 사용하는 방법이 있다.

# a = list(range(0, 10))
# b = [range(0,10)]
# print(a)
# print(b)
# range함수와 list함수를 융합해 리스트를 만들 수 있다.
# 하지만 직접 []를 사용하여 만들 경우 range함수를 b와 같이 안에 넣어도 리스트화 되지 않는다.
# range(x, y)에서 x는 element에 포함되지만 y는 포함되지 않고 y-1까지만 포함된다.

# c=list(range(-4, 10, 2))
# d=list(range(10, 0, -1))
# print(c)
# print(d)
# range함수에 3번째 값은 증감폭을 이야기하며, 아무것도 넣지 않을 경우엔 기본 증가폭 1이 적용된다.
# 증감폭을 양수로 넣으면 늘어나고 음수로 넣으면 줄어든다.

# a = (38, 21, 53, 62, 19)
# b = 38, 21, 53, 62, 19
# c = (38,)
# d = 38,
# print(a)
# print(b)
# print(c)
# print(d)
# 튜플 자료형은 변수에 ()로 감싼 값을 할당하거나 ,로 구분된 값을 할당하였을 경우 생성된다.
# 한의 값을 갖고 있는 튜플은 ()에 1개의 값 뒤에 쉼표 또는 1개의 값 뒤에 쉼표로 변수에 할당하여 생성한다.

# a = tuple(range(10))
# print(a)
# b = tuple(range(-4, 10, 2))
# print(b)
# 리스트와 같은 특징을 갖지만 튜플은 한 번 지정한 값을 변경할 수 없다.

# a = list(range(0,8,2))
# print(a)
# b = tuple(a)
# print(b)
# c = list(b)
# print(c)
# tuple함수와 list함수를 이용해서 리스트를 튜플로 다시 튜플을 리스트로 변경할 수 있다.

# a, b, c = [1, 2, 3]
# d, e, f = (4, 5, 6)
# print(a, b, c)
# print(d, e, f)
# x = a, b, c
# y = d, e, f
# print(x)
# print(y)
# 여러개의 변수에 리스트 또는 튜플의 요소를 할당하는 것을 리스트 언패킹, 튜플 언패킹이라고 합니다.
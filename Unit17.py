# i = 0                       # 초기식
# while i < 100:              # while 조건식
#     print('Hello, world!')  # 반복할 코드
#     i += 1                  # 변화식

# while문은 초기식부터 시작해서 while 조건식을 판단합니다.
# 초기식을 while 조건식에 넣고 변화식을 실행 후 다시 while 조건식으로 돌아가며 거짓이 나오면 반복이 종료됩니다.
# 변화식을 넣지 않을 경우 무한 루프에 걸리므로 주의해야 합니다.

# i = 100
# while i > 0:
#     print('Hello, world!')
#     i -= 1

# while문은 초기식에서 커지며 반복도 가능하지만 작아지며 반복하는 것도 가능합니다.

# count = int(input('반복할 횟수를 입력하세요 : '))

# i = 0
# while i < count:
#     print('Hello, world!', i)
#     i += 1

# input을 변수에 주고 이를 while 조건식에 넣어서 원하는 수만큼 반복하게 만드는 코드를 작성할 수 있습니다.

# import random

# print(random.randint(1, 6))

# import로 random 모듈을 불러와서 random모듈의 randint함수를 사용하면 원하는 범위내 숫자 중 랜덤값을 출력할 수 있습니다.

# import random

# i = 0
# while i != 3:
#     i = random.randint(1, 6)
#     print(i)

# i가 3이 아니라면 참이기 때문에 3이 나올때까지 while문이 반복됩니다.
# i는 randint함수가 출력해주는 1과 6사이의 정수가 할당되며, i가 3이 아니면 print()함수가 출력합니다.
# i가 3이 나오면 3이 출력되고 while함수에 3이 들어가면서 종료됩니다.

# import random

# a = [1, 2, 3, 4, 5, 6]

# i = 0
# while i != 3:
#     i = random.choice(a)
#     print(i)

# random모듈의 choice 함수를 이용해서 리스트, 튜플, range함수, 문자열을 이용해 위 코드와 똑같은 결과의 코드를 만들 수 있습니다.

# while True:
#     print('Hello, world!')

# 조건식 없이 트루인 값을 while에 넣으면 코드가 무한 반복되는 무한 루프가 완성됩니다.

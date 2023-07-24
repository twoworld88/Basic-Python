# def hello():
#     print('Hello, world!')
#     hello()
# hello()

# hello()함수는 함수 내부에서 다시 자신을 호출하는 모양을 하고 있습니다.
# 이런 함수의 방식을 재귀호출 이라고 합니다.
# 재귀호출의 중복은 1,000까지로 제한되어 있기에 이 함수를 그대로 실행하면 1000번 반복되다가 오류가 발생합니다.

# def hello(count):
#     if count == 0:
#         return
#     print('Hello, world!', count)

#     count -= 1
#     hello(count)

# hello(5)

# 이번 hello 함수는 내부에서 인수가 0이면 return으로 빠져나오도록 되어 있습니다.
# 0이 아닐경우 'Hello, world!'와 현재 인수를 출력하고
# 그 다음 인수를 -1해주고 다시 재귀호출을 통해 hello함수를 호출해서 반복합니다.
# hello가 0이면 바로 빠져 나오므로 5~1까지 인수와 'Hello, world!'를 출력하고 종료됩니다.
# 이처럼 재귀호출을 사용할 때는 종료 조건을 사용해줘야 합니다.

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))

# factorial(5)로 인수 5가 factorial 함수에 할당되면 n == 1이 아니므로 5 * factorial(4)를 반환합니다.
# factorial(4)를 구하기 위해 인수 4가 factorial 함수에 할당되면 역시 n == 1이 아니므로 4 * factorial(3)를 반환합니다.
# factorial(3)을 구하기 위해 인수 3이 factorial 함수에 할당되면 역시 n == 1이 아니므로 3 * factorial(2)를 반환합니다.
# factorial(2)를 구하기 위해 인수 2가 factorial 함수에 할당되면 역시 n == 1이 아니므로 2 * factorial(1)를 반환합니다.
# factorial(1)을 구하기 위해 인수 1이 factorial 함수에 할당되면 n == 1이므로 1을 반환합니다.
# 이제 역으로 factorial(2)는 2를 반환, factorial(3)은 6을 반환, factorial(4)는 24를 반환, factorial(5)은 120을 반환하며 종료됩니다.

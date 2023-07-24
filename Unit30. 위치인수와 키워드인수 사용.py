# print(10, 20, 30)
# def print_numbers(a, b, c):
#     print(a)
#     print(b)
#     print(c)

# print_numbers(10, 20, 30)

# 위 첫 줄과 같이 함수에 순서대로 인수를 넣어주는 방식을 위치인수라고 합니다.
# 이렇게 위치인수를 넣어준 print 함수는 인수를 한줄로 출력합니다.
# 위와 같이 함수를 선언해 두면 이 함수를 이용한 3개 변수가 할당된 함수는 각 변수에 할당된 값을 한줄씩 출력하게 만들 수 있습니다.

# def print_numbers(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# x = [10, 20, 30]

# print_numbers(*x)
# print_numbers(*[1, 2, 3])
# print_numbers(*(100, 200, 300))

# 위치 인수가 리스트나 튜플로 주어지는 경우가 있습니다.
# 이런 경우에 함수(*리스트), 함수(*튜플), 함수(*range())와 같이 리스트나 튜플, rnage앞에 *을 붙여주면 리스트나 튜플, range를 풀고 인수를 할당합니다.
# 이런 스킬을 언패킹이라고 합니다.

# def print_numbers(*args):
#     for arg in args:
#         print(arg)
# print_numbers(10)
# print_numbers(10, 20, 30, 40)
# print_numbers(*range(10))
# print_numbers(*[1, 2, 3, 4])
# print_numbers(*(100, 200, 300, 400))

# def 함수명(*변수): 와 같이 작성하면 변수에 할당되는 인수의 개수가 변해도 함수에 적용됩니다.
# 이렇게 변수에 여러 인수를 원하는 만큼 할당할 수 있도록 한 것을 가변인수라 합니다.
# 단, 언패킹이 필요한 인수(range, 리스트, 튜플 등)에는 앞에 *을 붙여줘야 합니다.

# def print_n(arg, *args):
#     print(arg)
#     print(args)
# print_n(1)
# print_n(1, 10, 20)
# print_n(*[1, 2, 3])
# print_n(*range(5))

# 고정인수와 가변인수를 같이 사용할 수 있습니다.
# 단, 고정인수는 무조건 가변인수보다 먼저 와야합니다.
# 고정인수와 가변인수를 동시에 넣을 경우 언패킹된 요소들이 고정인수에 먼저 할당되고 나머지가 가변인수에 할당됩니다.

# def personal_info(name, age, address):
#     print('이름 : ', name)
#     print('나이 : ', age)
#     print('주소 : ', address)
# personal_info('홍길동', 30, '서울특별시 용산구 이촌동')

# 첫번째 인수부터 순서와 용도를 기억하고 그 순서대로 이름, 나이, 주소를 넣어줘야합니다.
# 순서와 용도를 항상 기억하기에는 불편함 감이 있습니다.
# 파이썬에는 이런 불편함을 개선하기 위한 기능이 있습니다.

# def personal_info(name, age, address):
#     print('이름 : ', name)
#     print('나이 : ', age)
#     print('주소 : ', address)
# personal_info(name='홍길동', age=30, address='서울특별시 용산구 이촌동')
# personal_info(age=30, name='홍길동', address='서울특별시 용산구 이촌동')
# personal_info(address='서울특별시 용산구 이촌동', name='홍길동', age=30)

# 이렇게 키워드=값 으로 인수를 주면 순서상관없이 맞는 키워드에 값이 할당되어 반환됩니다.
# 참고로 sep='' 또는 end='' 가 바로 이런 키워드 인수입니다.

# def personal_info(name, age, address):
#     print('이름 : ', name)
#     print('나이 : ', age)
#     print('주소 : ', address)

# x = {'name' : '홍길동', 'age' : 30, 'address': '서울특별시 용산구 이촌동'}
# personal_info(**x)
# personal_info(**{'name' : '왕눈이', 'age' : 30, 'address': '서울특별시 서초구 반포동'})

# 이런 키워드 함수는 딕셔너리를 언패킹할 때 사용됩니다.
# 딕셔너리를 언패킹 하기 위해서 함수(**딕셔너리)와 같이 **을 앞에 붙여줘야 합니다.
# *을 한 번 사용하면 키만 언패킹되어 사용가능해 집니다.

# def personal_info(**kwargs):
#     for kw, arg in kwargs.items():
#         print(kw, ':', arg, sep='')
# personal_info(name = '홍길동')
# personal_info(name = '홍길동', age = 30, address= '서울특별시 용산구 이촌동')

# x = {'name' : '홍길동'}
# y = {'name' : '왕눈이', 'age' : 30, 'address': '서울특별시 서초구 반포동'}
# personal_info(**x)
# personal_info(**y)

# 위 와 같이 키워드가변인수를 만들 수 있습니다.
# 키워드가변인수를 갖고 있는 함수에는 키워드인수를 직접넣어도 되고 **딕셔너리로 넣어줘도 됩니다.

# def personal_info(**kwargs):
#     if 'name' in kwargs:
#         print('이름 : ', kwargs['name'])
#     if 'age' in kwargs:
#         print('나이 : ', kwargs['age'])
#     if 'address' in kwargs:
#         print('주소 : ', kwargs['address'])

# x = {'name' : '피카츄', 'age' : 30, 'height' : 88, 'job' : '한전직원', 'address' : '서울특별시 강남구 도곡동'}
# personal_info(**x)

# 이렇게 보통 키워드가변인수를 사용할 때는 함수내부에 딕셔너리 내 해당 키가 있는지 확인하고 실행하도록 만듭니다.
# 위치인수, 가변인수, 키워드가변인수를 같이 사용할때는 앞 순서와 같이 사용해야만 사용이 가능합니다.

# def personal_info(name, age, address = '비공개'):
#     print('이름 : ', name)
#     print('나이 : ', age)
#     print('주소 : ', address)

# personal_info('홍길동', 30)
# personal_info('왕눈이', 30, '서울특별시 서초구 반포동')

# 매개변수에 초기값을 지정해놓으면 변수값을 넣지 않았을 경우 그 초기값을 반환합니다.
# 대표적인 예가 print함수의 sep입니다. sep의 초기값은 ' '로 지정되어 있습니다.
# 고정값을 갖지만 가끔 예외적으로 값을 지정해야 할 때 사용합니다.
# 초기값이 지정된 변수는 초기값이 없는 변수 앞에 위치할 수 없습니다.

# a = 'Hello, world!'.replace('world', 'Python')
# print(a)
# b = 'Hello, world!'
# print(b.replace('world', 'Python'))
# print(b)
# c = b.replace('world', 'Python')
# print(b)
# print(c)

# replace 메소드를 사용하면 문자열 내 특정문자열을 지정해서 빠꿔줄 수 있습니다.
# replace 메소드는 문자열을 바꿔줄 뿐 결과를 저장하지 않습니다.
# 결과를 유지하고 싶다면 새로운 변수에 할당해주면 됩니다.

a = 'apple'
table = str.maketrans('aeiou', '12345')
print(a.translate(table))

# str.maketrans 함수를 이용해서 table이란 변수는 'aeiou'를 '12345'로 바꿔주도록 지정합니다.
# 여기서 'aeiou'→'12345'는 'a'→'1', 'e'→'2', 'i'→'3', 'o'→'4', 'u'→'5'로 변환된다는 뜻입니다.
# translate 메소드를 사용하여 지정된 테이블 변수를 실행해주면 글자가 치환되어 반환됩니다.

# a = 'apple pear grape pineapple orange'
# print(a.split())
# b = 'monkey, pig, bear, wolf, lion, tiger'
# print(b.split(', '))

# split 메소드를 사용하면 문자열을 분리해서 리스트에 저장해줍니다.
# 기본적으로 공란을 기준으로 분리합니다.
# split(값)처럼 값을 입력하면 기준을 값을 기준으로 분리해줄 수 있습니다.

a = 'apple pear grape pineapple orange'
b = a.split()
print(b)
c = ' '.join(b)
print(c)
# d = '-'.join(b)
# print(d)

# '구분자'.join(리스트)를 이용하면 서로 다른 문자열로 구성된 리스트의 요소를 합쳐서 하나의 문자열로 반환합니다.

# a = 'python'
# b = a.upper()
# print(b)
# c = b.lower()
# print(c)

# upper 메소드는 문자열을 대문자로, lower 메소드는 문자열을 소문자로 반환합니다.

# a = '   Python   '
# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())

# lstrip 메소드는 왼쪽공백을 없에주고 rstrip 메소드는 오른쪽 공백을 없에줍니다.
# strip 메소드는 모든 공백을 없에줍니다.

# a = '..,.,. Python .,.,.,'
# print(a.strip('.,'))
# print(a.lstrip('.,'))
# print(a.rstrip('.,'))

# strip('.,')와 같이 넣어줘서 .이나 콤마를 제거 할 수 있습니다.
# 이 때 공백까지 제거하려면 공백을 추가해줘야 합니다.

# a = '..,.,. Python .,.,.,'
# print(a.strip('., '))
# print(a.lstrip('., '))
# print(a.rstrip('., '))

# a = 'python'
# print(a.center(10))
# print(a.ljust(10))
# print(a.rjust(10))

# 문자열을 정렬할때는 center, ljust, rjust 메소드를 사용해 줍니다.
# center(정렬공간길이)와 같이 사용하면 정렬공간길이 내 문자열의 인덱스가 중앙에 오도록 정렬합니다.
# ljust(정렬공간길이)와 같이 사용하면 정렬공간길이 내 문자열의 인덱스가 왼쪽으로 오도록 정렬합니다.
# rjust(정렬공간길이)와 같이 사용하면 정렬공간길이 내 문자열의 인덱스가 오른쪽으로 오도록 정렬합니다.

# a = 'python'
# b = a.rjust(10).upper()
# print(b)

# 정렬공간길이 10에 python을 오른쪽으로 정렬하고 대문자로 변환하게 됩니다.
# 문자열 메소드는 이처럼 연결해서 호출할 수 있는 메소드 체이닝 이라는 기술을 사용할 수 있습니다.

# a = 'python'
# b = a.zfill(8)
# print(b)

# 파이썬에서는 남는 공간에 0을 채워줘야 하는 경우가 발생합니다. 
# 이럴 경우엔 zfill 메소드를 사용해주면 됩니다.
# zfill(채워줄 공간)으로 사용했을 때 채워줄 공간보다 적용하는 문자열이 길거나 같으면 아무것도 채우지 않습니다.

# a = 'apple pineapple'
# b = a.find('l')
# c = a.find('z')
# d = a.rfind('l')
# print(b)
# print(c)
# print(d)

# find(찾는 문자열) 메소드는 문자열 내에 문자열을 찾아줍니다.
# 찾는 문자열이 없을 경우 -1을 반환하며, 있을 경우 그 인덱스를 반환합니다.
# find는 동일한 문자열이 있을 경우 왼쪽에서 가장 먼저 있었던 문자의 인덱스를 반환합니다.
# rfind는 동일한 문자열이 있을 경우 오른쪽에서 가장 먼저 있었던 문자의 인덱스를 반환합니다.
# index, rindex 메소드도 동일한 find, rfind와 동일한 기능을 합니다.
# 단, index, rindex는 찾는 문자열이 없을 경우 에러를 발생시킵니다.

# a = 'apple pineapple'
# print(a.count('p'))

# count(찾는 문자열) 메소드는 문자열 내에서 찾는 문자열이 몇 개 존재하는지 그 개수를 반환해줍니다.

# a = 'I am %s' % 'james'
# print(a)

# b = 'jane'
# c = 'I am %s' % b
# print(c)

# d = 'I am %d years old.' % 20
# print(d)

# 문자열에 %s를 넣고 문자열 종료 후 뒤에 % 문자열 을 넣어주면 %s 자리에 문자열이 대입되어 들어갑니다.
# 이 때 %s의 s는 string의 s입니다.
# 문자열에 %d를 넣고 문자열 종료 후 뒤에 % 숫자 를 넣어주면 %d 자리에 숫자가 대입되어 들어갑니다.
# 이 때 %d의 d는 decimal integer의 d입니다.

# a = 2.3
# print('%f' % a)
# print('%.2f' % a)
# print('%.3f' % a)

# %f를 문자열로 작성한 후 그 뒤에 % 숫자를 넣어주면 소수점으로 표현해줍니다. %f는 기본 소수점뒤 6자리까지 표기합니다.
# %.자릿수f를 입력할 경우 소수점 뒤 자릿수를 지정할 수 있습니다.

# a = '%10s' % 'python'
# print(a)
# b = '%-10s' % 'python'
# print(b)

# %정렬공간길이s 를 문자열로 작성한 후 뒤에 % 문자열을 넣어주면 정렬공간길이에서 오른쪽으로 정렬된 문자열을 반환합니다.
# %-정렬공간길이s 를 문자열로 작성한 후 뒤에 % 문자열을 넣어주면 정렬공간길이에서 왼쪽으로 정렬된 문자열을 반환합니다.
# %d 와 %f도 %뒤에 정렬공간길이를 넣어주면 정렬합니다.

# a = 'Today is %d %s.' % (3, 'April')
# print(a)

# 하나의 문자열에 여러개를 넣을 수도 있습니다.
# 이런 경우 문자열 종료 후 % 뒤에 ()를 넣고 문자열 내 %# 개수만큼 값을 넣어줘야만 합니다.

# a, b, c = input().split()
# d = 'my name is {} {}. i am {} years old.'.format(a, b, c)
# print(d)

# format(a, b, c) 메소드를 사용하면 문자열 내 {}에 순서대로 a b c를 넣어준다.
# 만약 {인덱스}을 지정할 경우 순번대로 입력됩니다.

# a, b, c = input().split()
# d = 'my name is {0} {2}. i am {1} years old.'.format(a, b, c)
# print(d)

# {0} = a, {1} = b, {2} = c

# a = 'my name is {name} {firstname}. i am {old} years old.'.format(name = 'sehwan', firstname = 'lee', old = 36)
# print(a)

# 인덱스 대신 포맷에 이름을 지정해서 넣어줄수도 있다.

# name = 'sehwan'
# firstname = 'lee'
# old = '36'
# a = f'my name is {name} {firstname}. i am {old} years old.'
# print(a)

# 변수를 직접 넣어주는 방법도 있습니다. 문자열 앞에 f를 붙여주고 {}안에 변수를 입력해주면 그대로 값을 반환합니다.

# a = '{0:<10}'.format('Python')
# b = '{0:>10}'.format('Python')
# c = '{0:<10} {1:>10}'.format('Python', 'world!')
# print(a)
# print(b)
# print(c)

# {}안에 인덱스:<정렬공간길이를 넣어주면 공간길이 내에서 왼쪽으로 정렬로 반환합니다.
# {}안에 인덱스:>정렬공간길이를 넣어주면 공간길이 내에서 오른쪽으로 정렬로 반환합니다.

# a = '%03d' % 1
# print(a)
# b = '{0:03d}'.format(35)
# print(b)
# c = '%08.2f' % 3.6
# print(c)
# d = '{0:08.2f}'.format(150.37)
# print(d)

# %03d 는 % 뒤 정수를 3자리로 표현해라. 단, 왼쪽 빈공간은 0으로 채워라. 라는 코드입니다.
# {0:03d}는 포맷에 인덱스 0의 정수를 3자리로 표현해라. 단, 왼쪽 빈공간은 0으로 채워라. 라는 코드입니다.
# %08.2f는 % 뒤 실수를 소숫점 뒤 2자리까지 표현된 8자리로 표현해라. 단, 왼쪽 빈공간은 0으로 채워라. 라는 코드입니다.
# {0:08.2f}는 포맷에 인덱스 0의 실수를 소숫점 뒤 2자리까지 표현된 8자리로 표현해라. 단, 왼쪽 빈공간은 0으로 채워라. 라는 코드입니다.
# 복합해서 사용할 경우 {인덱스:채우는숫자정렬방법정렬공간길이.소숫점자릿수자료형}순으로 입력합니다.

# a = '{0:,}원입니다.'.format(1778600)
# print(a)

# {인덱스:,}를 입력해서 숫자에 3자리마다 ,를 찍어줄 수 있습니다.
# {인덱스:정렬방향정렬공간길이,}로 정렬방향 및 정렬공간을 지정하고 3자리마다 ,를 찍어서 표기할수도 있습니다.
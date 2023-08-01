# import re

# print(re.match('Hello', 'Hello, world!'))

# 정규표현식은 일정한 규칙을 가진 문자열을 표현하는 방법입니다.
# 특정 문자를 검색해서 특징이나 규칙을 찾아서 추출하거나 바꿀때 사용합니다.
# 또는, 문자열이 정해진 규칙에 부합하는지를 판단해줍니다.
# re모듈에 포함된 기능을 사용해서 구현합니다.
# 위 코드는 'Hello, world!'라는 문자열에 'Hello'문자열과 동일한 문자열이 있는지를 찾아주는 match메소드를 사용한 것입니다.

# import re

# print(re.search('^Hello', 'Hello, world!'))
# print(re.search('Hello$', 'Hello, world!'))
# print(re.search('^world!', 'Hello, world!'))
# print(re.search('world!$', 'Hello, world!'))

# search 메소드를 사용하면 해당 문자열이 멘앞에 있는지 멘뒤에 있는지 확인해줍니다.
# 멘 앞에 있는지 볼 때는 찾는 문자열 앞에 ^를 붙이고 멘 뒤에 있는지 볼 때는 뒤에 $를 붙여줍니다.
# search는 멘 앞 또는 멘 뒤에 있는지만 판단합니다.

# match는 찾는 문자열이 처음부터 일치하는 문자열이 있는지만 판단할 수 있습니다.
# search는 찾는 문자열이 어디든 존재하는지를 판단할 수 있습니다.

# import re

# print(re.match('Hello|world|Hi', 'Hello, skill!'))

# 여러개의 문자열을 사이사이 |를 넣어서 찾아야하는 문자열에 넣어주면 그 중 하나라도 있는지 판단해준다.

# import re

# print(re.match('[0-9]*', '12234'))
# print(re.match('[0-9]+', '1284827'))

# match 메소드를 사용할때 찾아야하는 문자열에 [0-9]를 넣어주고 그 뒤에 *을 붙이면 0개 이상이 있으면 그 위치와 개수를 반환하고 +를 붙이면 1개 이상이 있으면 그 위치와 개수를 반환합니다.

# import re

# print(re.match('a*b', 'b'))
# print(re.match('a+b', 'b'))
# print(re.match('a*b', 'aab'))
# print(re.match('a*b', 'aab'))

# 뒤에 *를 붙여주면 0개 이상을 경우에도 반환값이 있는 것을 볼 수 있습니다.

# import re

# print(re.match('abc?d', 'abd'))
# print(re.match('ab[0-9]?c', 'ab3c'))
# print(re.match('ab.d', 'abxd'))
# print(re.match('abc?d', 'abccd'))
# print(re.match('ab[0-9]?c', 'ab34c'))
# print(re.match('ab.d', 'abxyzd'))

# 뒤에 ?를 붙이면 앞의 문자나 범위가 0개 또는 1개인지 판단하고, .을 붙이면 그 위치에 문자나 숫자가 1개 있는지 판단합니다.
# 복수의 문자나 범위를 판단하지 못합니다.

# import re

# print(re.match('h{3}', 'hhhello'))
# print(re.match('(hello){3}', 'hellohellohelloworld'))

# 문자나 (문자열)뒤에 {n}을 붙여주면 판단할 문자열에 문자나 (문자열)이 n개 존재하는지 확인할 수 있습니다.

# import re

# print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-4356-2948'))
# print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '0507-4356-2948'))
# print(re.match('[0-9]{3}-[0-9]{4}-[0-9]{4}', '010-356-2948'))

# 숫자 범위 뒤에 {n}을 붙여서 휴대폰 번호가 맞는지 아닌지 판단하도록 할 수 있습니다.
# 하지만 이렇게 하면 가운제 번호가 3자리인 휴대폰 번호는 판단할 수 없습니다. 

# import re

# print(re.match('[0-9]{3}-[0-9]{3,4}-[0-9]{4}', '010-4356-2948'))
# print(re.match('[0-9]{3}-[0-9]{3,4}-[0-9]{4}', '0507-4356-2948'))
# print(re.match('[0-9]{3}-[0-9]{3,4}-[0-9]{4}', '011-356-2948'))

# 위 코드에서 처럼 뒤에 {n}이 아니라 {n, m}과 같이 붙여주면 n개 ~ m개가 있는지를 검색해 줍니다.
# 가운데 번호가 3자리인 휴대폰번호까지 판단해 줄 수 있게됩니다.

# import re

# print(re.match('[a-zA-Z0-9]+', 'Hello1234'))
# print(re.match('[A-Z0-9]+', 'hello'))

# [0-9], [a-z], [A-Z]로 문자열도 범위로 지정할 수 있으며, 하나의 []에 같이 넣어주면 같이 들어간 계열을 모두 판단합니다.
# 한글은 [가-힣]을 넣어주면 됩니다.

# import re

# print(re.match('[^A-Z]+', 'Hello'))
# print(re.match('[^A-Z]+', 'hello'))

# 특정 문자열 범위가 포함되어 있는지 판단해주려면 범위 앞에 ^를 붙여줍니다.
# 특정 문자열이나 범위로 시작하는지도 앞에 ^를 붙였는데 시작하는지는 ^[x]와 같이 대괄호 밖 앞에 붙여주고 search메소드를 사용합니다.
# 특정 문자열이나 범위로 끝나는지를 확인할 때는 [x]+$과 같이 대괄호 밖 +나 *의 뒤에 붙여주고 search메소드를 사용합니다.

# import re

# print(re.search('\*+', '1 ** 2'))
# print(re.search('[$()a-zA-Z0-9]+', '#(document)'))
# print(re.match('\d+', '1234'))
# print(re.match('\D+', 'Hello'))
# print(re.match('\w+', 'Hello_1234'))
# print(re.match('\W+', '(:;,.)'))

# 특수문자가 사용됐는지를 확인하려면 찾을 특수문자앞에 \를 붙여주고 search메소드를 써주면 됩니다.
# []안에 특수문자를 넣으면 \를 사용할 필요가 없으나 혹시 오류가 나는 경우 앞에 붙여줍니다.
# \d, \D, \w, \W를 match메소드의 사용하면 아래와 같은 뜻으로 사용됩니다.
# \d는 [0-9]과 같은 뜻으로 쓰입니다.
# \D는 [0-9]를 제외한 모든 문자열을 말합니다.
# \w는 [a-zA-Z0-9_] 소문자, 대문자, 숫자에 _를 포함한 문자열을 뜻합니다.
# \W는 소문자, 대문자, 숫자, _를 제외한 모든 문자열을 뜻합니다.

# import re

# print(re.match('[a-zA-Z0-9 ]+', 'Hello 1234'))
# print(re.match('[a-zA-Z0-9\s]+', 'Hello 1234'))

# 공백을 포함하는 판단하기 위해서는 ' ' 또는 \s 를 사용합니다.
# \s는 [ \t\n\r\f\v]와 같습니다.
# \S는 [\t\n\r\f\v]와 같습니다. 공백을 제외하고 탭, 새 줄, 캐리지 리턴, 폼피드, 수직 탭을 포함합니다.

# import re

# p = re.compile('[0-9]+')

# print(p.match('1234'))
# print(p.search('hello'))

# 변수 = re.compile('패턴') 과 같이 작성하면 원하는 패턴을 변수에 저장할 수 있습니다.
# 패턴이 저장된 변수.match('판단할 문자열') 또는 패턴이 저장된 변수.search('판단할 문자열')과 같이 작성하여 사용할 수 있습니다.

# import re

# m = re.match('([0-9]+) ([0-9]+)', '10 295')

# print(m.group(1))
# print(m.group(2))
# print(m.group())
# print(m.group(0))
# print(m.groups())

# n = re.match('([a-zA-Z]+) ([0-9]+) ([a-zA-Z0-9]+)', 'Hello 2349 naVer003')

# print(n.group(1))
# print(n.group(2))
# print(n.group(3))
# print(n.group(0))
# print(n.groups())

# 정규표현식을 만들때 조건에 ()와 공백으로 구분해주면 그룹이 형성됩니다.
# 정규표현식을 변수에 할당하고 변수에 group메소드를 사용해주면 해당 그룹별로 반환할 수 있습니다.
# groups 메소드를 사용하면 그룹별 값을 하나의 튜플로 반환합니다.


# import re

# m = re.match('(?P<func>[a-zA-Z_][a-zA-Z0-9_]+)\((?P<arg>\w+)\)', 'print(1234)') # \( \)는 print(1234)에서 괄호를 표현식에 넣어주기 위해서 앞에 \를 붙여줍니다.

# print(m.group('func'))    # 그룹 이름으로 매칭된 문자열 출력
# print(m.group('arg'))     # 그룹 이름으로 매칭된 문자열 출력

# ?P<그룹이름>을 그룹의 ()안 멘 앞에 넣어주면 그룹명을 지정할 수 있습니다.

# import re 

# print(re.findall('[0-9]+', '1 2 Fizz 4 Buzz Fizz 8 9'))

# findall메소드를 사용하면 해당 조건에 맞다고 판단된 문자열을 ' '로 구분하여 요소로하는 리스트로 반환해줍니다.

# import re

# print(re.sub('apple|orange', 'fruit', 'apple box orange tree'))
# print(re,sub('[0-9]+', 'n', '1 2 Fizz 4 Buzz Fizz 7 8'))

# re.sub('패턴', '새롭게 바뀌어 들어갈 문자열', '대상 문자열', '바꿀횟수')와 같이 작성해주면 대상 문자열에서 패턴에 맞는 문자열을 추출해서 새롭게 바뀌어 들어갈 문자열로 치환해줍니다. 문자열 구분은 ' '로 합니다. 

# import re

# def multiple10(m):
#     n = int(m.group())
#     return str(n * 10)

# print(re.sub('[0-9]+', multiple10, '1 2 Fizz 4 Buzz Fizz 7 8'))

# sub메소드는 새롭게 바뀌어 들어갈 문자열에 함수를 넣을 수 있습니다.
# 위 코드는 match객체를 변수로 받는 함수를 만들고 객체에 group메소드로 추출하여 int함수로 정수로 변환해 변수에 할당해줍니다.
# n에 10을 곱한 후 str함수로 문자열로 변환해서 return해줍니다.

# import re

# print(re.sub('([a-z]+) ([0-9]+)', '\\2 \\1 \\2 \\1', 'hello 1234'))

# 그룹1 그룹2 조건으르 추출한 후 \\그룹번호 로 바꿔넣어준 코드입니다.
# 그룹1 hello, 그룹2 1234를 \\2 \\1 \\2 \\1 로 순서를 바꿔 2번 반복되게 출력됩니다.

# import re

# print(re.sub('({\s*)"(\w+)":\s*"(\w+)"(\s*})', '<\\2>\\3</\\2>', '{ "name": "james" }'))

# name과 james를 추출해서 <name>james</name>으로 출력하도록 하는 코드입니다. 외계어처럼보이지만 하나씩 풀어서 살펴보겠습니다.
# 그룹1 : {, \s(공백)이 0개 이상 포함된 것
# 그룹2 : 첫 번째 ""안에 a-z, A-Z, 0-9, _에 포함되는 것
# 가운데 :와 ' '은 판단만 되도록 넣어주고 그룹필 하지 않습니다.
# 그룹3 : 두 번째 ""안에 a-z, A-z, 0-9, _에 포함되는 것
# 그룹4 : \s(공백), }가 0개 이상 포함된 것
# 이렇게 그룹을 나눠준 후 바뀌어 바뀌어 들어갈 문자열 부분에 넣어줄 기호와 \\들어갈 그룹번호 를 알맞게 넣어주면 원하는 결과물 <name>james</name>이 나오게 됩니다.


# import re

# print(re.sub('({\s*)"(?P<key>\w+)":\s*"(?P<value>\w+)"(\s*})', '<\\g<key>>\\g<value></\\g<key>>', '{ "name": "james" }'))

# 그룹명을 정했을 때는 바뀌어 들어가는 문자열에 \\들어갈 그룹번호 대신 \\g<그룹명>을 넣어주면 됩니다.
    
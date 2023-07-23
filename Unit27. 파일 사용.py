# file = open('hello.txt', 'w')
# file.write('Hello, world!')
# file.close()

# 파일객체 = opne(파일명, 파일모드)로 파일을 쓰기전용, 읽기전용 등으로 불러올 수 있습이다.
# 파일객체.write('문자열') 메소드로 파일에 문자열을 작성해서 저정할 수 있습니다.
# 파일객체.close() 메소드로 작업을 완료한 파일을 종료합니다.

# f = open('hello.txt', 'r')
# s = f.read()
# print(s)
# f.close()

# 파일객체.read() 메소드로 변수f에 열려서 할당된 'hello.txt'의 내용을 반환하여 변수 s에 할당해줍니다.
# print 함수로 s의 값을 출력합니다.

# with open('hello.txt', 'r') as f:
#     s = f.read()
#     print(s)

# with open(파일명, 파일모드) as 파일객체: 로 파일을 열어 줄 수 있다.
# close() 메소드를 사용하지 않아도 파일이 자동으로 닫힌다.

# with open('hello.txt', 'w') as f:
#     for i in range(3):
#         f.write('Hello, worle! {}\n'.format(i))

# for문을 이용해서 여러줄의 문자열을 파일에 저장할 수 있습니다.
# 이 때, \n으로 줄바꿈을 문자열에 넣어주지 않으면 한줄로 붙어서 출력되니 유의해야합니다.

# l = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
# with open('hello.txt', 'w') as f:
#     f.writelines(l)

# 리스트에 있는 문자열을 파일에 쓰고 저장하고 싶을 경우 writelines(리스트)를 사용해주면 됩니다.

# with open('hello.txt', 'r') as f:
#     l = f.readlines()
#     print(l)

# readlines 메소드를 사용해주면 파일내 문자열을 1줄씩 리스트로 가져올 수 있습니다.

# with open('hello.txt', 'r') as f:
#     l = None
#     while l != '':
#         l = f.readline()
        # print(l.strip('\n'))

# readline은 한 줄씩 파일의 값을 반환해준다.
# 파일의 문자열을 불러올땐 while문을 사용합니다. 왜냐하면 파일에 몇줄의 문자열이 있는지 모르기 때문입니다.
# 빈문자열이 나오면 반복을 멈추도록 조건식에 l != '' 빈문자열은 아니라는 조건을 달아줍니다.
# l을 None으로 초기화 해주지 않으면 내부 자료와 대조하여 실행됨으로 에러가 날 수 있습니다.
# 또한 빈문자열로 설정하면 처음부터 빈문자열이 나오기때문에 작동하지 않습니다.
# 출력에서 strip 메소드로 \n을 하나씩 삭제하지 않으면 이미 문자열에 줄바꿈이 있고 readline으로 한줄씩 불러오며 생긴 \n까지 중복적용됩니다.

# with open('hello.txt', 'r') as f:
#     for l in f:
#         print(l.strip('\n'))

# 파이썬에서는 for문으로 while문보다 간단하게 한줄씩 문자열을 불러서 출력할 수 있습니다.
# for문이 파일객체 f에서 한줄씩 읽어서 l에 할당하고 출력합니다.

# import pickle

# name = 'gildong'
# age = 18
# address = '서울특별시 서초구 반포동'
# scores = {'korean' : 90, 'english' : 95, 'mathematics' : 85, 'science' : 82}

# with open('gildong.p', 'wb') as f:
#     pickle.dump(name, f)
#     pickle.dump(age, f)
#     pickle.dump(address, f)
#     pickle.dump(scores, f)

# pickle 모듈을 사용해 내부에 dump 메소드를 이용하면 객체를 파일에 저장할 수 있게 됩니다.
# *.p라는 확장자를 사용했지만 다른 확장자를 써도 무관합니다.
# wb 파일모드는 바이너리 쓰기 모드입니다. 파일을 바이너리파일로 작성합니다.
# 바이너리 파일은 지금까지 작성한 텍스트 파일과 다르게 사람이 읽을 수 없는 언어입니다.
# 특정 뷰어가 있으면 사람이 읽을 수 있게 변환해줍니다.

# import pickle

# with open('gildong.p', 'rb') as f:
#     name = pickle.load(f)
#     age = pickle.load(f)
#     address = pickle.load(f)
#     scores = pickle.load(f)
#     print(name)
#     print(age)
#     print(address)
#     print(scores)

# pickle 모듈 내부에 있는 load 메소드를 사용해서 저장한 객체를 불러올 수 있습니다.


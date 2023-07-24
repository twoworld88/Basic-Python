# for i in range(5):
#     for j in range(5):
#         print('j:', j, sep='', end='')
#     print('i:', i, '\\n', sep='')

# i가 있는 for문은 새로줄을 만들어주는 반복문
# j가 있는 for문은 가로줄을 만들어주는 반복문
# 으로 활용되어 두가지 for문을 중복사용하여 2차원을 표현할 수 있습니다.
# 이는 이미지, 영상, 좌표계 처리에 주로 사용됩니다.

# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()

# i를 하나 할당할때마다 j가 할당되도록 합니다.
# j는 한번 할당될때마다 *을 하나씩 출력합니다.
# print()로 줄바꿈을 하고 다음 i를 할당하며 코드가 반복됩니다.
# 결과적으로 가로 5 새로 5의 *로 만들어진 사각형이 출력됩니다.

# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print('*', end='')
#     print()

# i를 하나 할당할때마다 j가 할당되도록 합니다.
# j를 할당하는 포문 내부에 if문으로 이미 할당된 i보다 j가 작거나 같을때만 *을 출력합니다.
# print()로 줄바꿈을 하고 다음 i를 할당하며 코드가 반복됩니다.
# 결과적으로 위부터 1개 2개 ..... 5개인 *로 만들어진 직각삼각형이 출력됩니다.

# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# i를 하나 할당할때마다 j가 할당되도록 합니다.
# j를 할당하는 포문에 if문으로 j가 i랑 같을때는 '*'을 다르면 공란을 출력하도록 합니다.
# print()로 줄바꿈을 하고 다음 i를 할당하며 코드가 반복됩니다.
# 결과적으로 *로 그려진 대각선이 만들어 집니다.

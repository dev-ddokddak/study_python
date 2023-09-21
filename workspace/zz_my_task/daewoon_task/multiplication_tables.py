# 대운 왈 1~9단까지 세로로 나열해서 해보셈

# for i in range(9):
#     print(f'{i + 1}단')   
#     for a in range(9):
#         # print('2.for단')
#         result = (i + 1) * (a + 1)
#         print(f'{i + 1} * {a + 1} = {result}')

       


# print(f'{1} * {2} = {2}')






# for i in range(9):
#     print(f'{9-i}단')

#     for a in range(9):
#         result = (9 - i) * (a + 1)
#         print(f'{9-i} * {a+1} = {result}')

#     # print(9-i)

# 1~9단까지 홀수인 것만 출력


for i in range(9):
    # if i % 2 == 0 :
    # if i + 1 % 2 == 0 :  -> 실패출력(나머지가 남지 않아서 else로 감)
    if (i + 1) % 2 == 1 :


        print(f'{i + 1}단')   


        for a in range(9):
            # print('2.for단')
            result = (i + 1) * (a + 1)
            print(f'{i + 1} * {a + 1} = {result}')
    else:
        print('실패')
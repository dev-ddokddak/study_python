if '다' < '나' :
    print('true')
else :
    print('false')

if 'a' < 'c' :
    print('true')
else :
    print('false')

# 영문 알파뱃이나 한글도 제 각각 값이 있다. 순서를 사용할 수 있다.

num1, num2 = input().split(" ")
op = input()
choice1, choice2, choice3, choice4 = op == '+', op == '-', op == '*', op == '/'
if choice1:
    total = int(num1) + int(num2)
    print(total)
elif choice2:
    a = int(num1) - int(num2)
    print(a)
elif choice3:
    b = int(num1) * int(num2)
    print(b)
elif choice4:
    c = int(num1) / int(num2)
    print(c)

# 두 정수의 연산을 수행하는 계산기 모듈 제작
# 연산 수행 시 해당 시간을 기록하고,
# 연산 수행 중 오류 발생 시 오류 사항과 시간을 기록하도록 한다.

# 입력 예
# 두 정수를 입력하세요.
# 연산자를 선택하세요

# 출력 예
# 1 + 3 = 4
# 10 / 0 = ZeroDivisionError
message1, message2 = input("두 정수를 입력하세요: ").split(" ")
message3 = input("연산자를 선택하세요: ")

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        result = int(self.num1) + int(self.num2)
        return result
    
    def minus(self):
        result = int(self.num1) - int(self.num2)
        return result
    
    def mul(self):
        result = int(self.num1) * int(self.num2)
        return result

    def div(self):
        result = int(self.num1) / int(self.num2)
        return result


choice1, choice2, choice3, choice4 = message3 == '+', message3 == '-', message3 == '*', message3 == '/'



print_result = Calculator(message1, message2)
if choice1:
    print(print_result.plus())
elif choice2:
    print(print_result.minus())
elif choice3:
    print(print_result.mul())
elif choice4:
    print(print_result.div())

# 테스트 계산기는 작동 잘하는데 class에 문제가 있는거같음
# 해결완료/ 문제점 : 선언부에 Calculator을 안적어서 오류가 났었음

# num1, num2 = input().split(" ")
# op = input()
# choice1, choice2, choice3, choice4 = op == '+', op == '-', op == '*', op == '/'
# if choice1:
#     total = int(num1) + int(num2)
#     print(total)
# elif choice2:
#     a = int(num1) - int(num2)
#     print(a)
# elif choice3:
#     b = int(num1) * int(num2)
#     print(b)
# elif choice4:
#     c = int(num1) / int(num2)
#     print(c)

file = open('clac_w.txt', 'w', encoding='utf-8')
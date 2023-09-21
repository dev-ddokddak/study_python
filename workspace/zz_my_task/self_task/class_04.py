# message1, message2 = print(input("2개의 정수를 입력하세요.\n예)1 2 \n").split(" "))
# 왜 오류???
# TypeError: cannot unpack non-iterable NoneType object

message1 = int(input("첫번째 정수를 입력하세요."))
message2 = int(input("두번째 정수를 입력하세요."))

# message1 = print(input("첫번째 정수를 입력하세요."))
# message2 = print(input("두번째 정수를 입력하세요."))
# print를 쓰면 안되나봄
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        result = self.num1 + self.num2
        return result
    
    def minus(self):
        result = self.num1 - self.num2
        return result
    
    def mul(self):
        result = self.num1 * self.num2
        return result

    def div(self):
        result = self.num1 / self.num2
        return result
    


print_result = Calculator(message1, message2)
print('더하기', print_result.plus())
print('빼기', print_result.minus())
print('곱하기', print_result.mul())
print('나누기', print_result.div())

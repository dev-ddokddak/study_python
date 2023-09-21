def check(*, key, value): # 키와 벨류값을 받아서 유져에게 리턴
    def set_target():
        for bank in Bank.banks:
            for user in bank:
                if user.__getitem__(key) == value:
                    return user
        return None

    return set_target


class Bank: # 뱅크 클래스
    total_count = 3 # 전체 카운트 = 3
    banks = [[] for i in range(total_count)] 

    def __init__(self, owner: str, account_number: str, phone: str, password: str, money: int): # __init__메소드 ->생성자/ 멤버의 변수를 초기화. __init__의 호출이 끝나면 메모리 주소값이 부여
        self.owner = owner                          # self 객체 자기 자신을 참조하는 변수, self가 아닌 다른 변수명을 사용할 수 있다. 멤버 메소드정의 시 사용.
        self.account_number = account_number
        self.phone = phone
        self.password = password
        self.money = money
        self.object = self

    @classmethod # classmethod해당 메소드의 첫번째 인자에 클래스를 입력하여 정적 메소드로 정의
    def open_account(cls, owner: str, account_number: str, phone: str, password: str, money: int, bank_choice: int): # 
        # 선언
        bank = [
            ShinHan, KookMin, KaKao
            # ShinHan(owner, account_number, phone, password, money),   # 신한 국민 카카오에 대해 각자 선언하는 방식
            # KookMin(owner, account_number, phone, password, money),   # 주석처리 안한것은 나열해놓고 아래의 append~이후에 한번에 선언한다
            # KaKao(owner, account_number, phone, password, money)
        ][bank_choice - 1]
        # 사용 (bank(owner, ...))
        cls.banks[bank_choice - 1].append(bank(owner, account_number, phone, password, money).__dict__)
        return bank


    @staticmethod # 해당 메소드의 특별히 추가되는 인자없이 정적 메소드로 정의
    def check_account_number(account_number: str) -> dict: # 계좌번호를 체크하는 함수
        return check(key='account_number', value=account_number)() # 추출된 값을 키와 벨류로 딕셔너리에 입력

    @staticmethod # 해당 메소드의 특별히 추가되는 인자없이 정적 메소드로 정의
    def check_phone(phone: str) -> dict: # 휴대폰 번호를 체크하는 함수
        return check(key='phone', value=phone)() # 추출된 값을 키와 벨류로 딕셔너리에 입력

    def deposit(self, money: int): # 입금
        self.money += money # 기존 잔액 += 입력한 금액

    def withdraw(self, money: int): # 출금
        self.money -= money # 기존 잔액 -= 입력한 금액

    def show_balance(self) -> int: # 잔액조회 # '-> int'는 int값임을 표시하기위한 주석처리같은것 식에 영향을 주지 않음
        return self.money # self.money로 리턴

    def __str__(self): # __str__메소드 -> 문자열 표현
        return f'{self.owner}, {self.account_number}, {self.phone}, {self.password}, {self.money}'# f스트링으로 문자열 출력


class ShinHan(Bank):# 신한은행
    def deposit(self, money: int):# 출금함수
        money /= 2 # 기존값에서 출금금액을 빼기위한 수식
        super().deposit(int(money))


class KookMin(Bank):
    def withdraw(self, money: int):
        money *= 1.5 # 기존값에서 출금금액을 빼기위한 수식
        super().withdraw(int(money)) # 


class KaKao(Bank):
    def show_balance(self) -> int: # 화살표는 주석이다/ 전체
        self.money /= 2 # 기존값에서 
        return super().show_balance()


if __name__ == '__main__':

    bank_menu = "1. 신한 은행\n" \
                "2. 카카오 뱅크\n" \
                "3. 국민 은행\n" \
                "4. 나가기\n"

    menu = "1. 개설\n" \
           "2. 입금\n" \
           "3. 출금\n" \
           "4. 잔액\n" \
           "5. 은행 선택 메뉴로 돌아가기\n"

    owner_message = "예금주: "
    account_number_message = "계좌번호: "
    phone_message = "핸드폰 번호: "
    password_message = "비밀번호(4자리): "
    money_message = "예치금: "
    deposit_message = "입금액: "
    withdraw_message = "출금액: "
    error_message = "다시 시도해주세요"

    while True:
        bank_choice = int(input(bank_menu))
        if bank_choice == 4:
            break

        while True:
            menu_choice = int(input(menu))
            if menu_choice == 5:
                break

            # 개설
            if menu_choice == 1:
                owner = input(owner_message)
                
                while True:
                    account_number = input(account_number_message)
                    if Bank.check_account_number(account_number) is None:
                        break

                while True:
                    phone = input(phone_message)
                    if Bank.check_phone(phone) is None:
                        break

                while True:
                    password = input(password_message)
                    if password.__len__() == 4:
                        break

                money = int(input(money_message))

                user = None

                # 아래의 분기별 은행 분석을 한 줄로 변경!
                user = Bank.open_account(owner, account_number, phone, password, money, bank_choice)

                # # 신한 은행
                # if bank_choice == 1:
                #     user = ShinHan.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 카카오 뱅크
                # elif bank_choice == 2:
                #     user = KaKao.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # # 국민 은행
                # elif bank_choice == 3:
                #     user = KookMin.open_account(owner, account_number, phone, password, money, bank_choice)
                #
                # print(user, Bank.banks, sep="\n")

            # 입금
            elif menu_choice == 2:
                # 입금은 개설한 은행에서만 가능
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        deposit_money = int(input(deposit_message))
                        # 객체를 가져와서 deposite()실행
                        user.__getitem__("object").deposit(deposit_money)
                else:
                    print(error_message)
            # 출금
            elif menu_choice == 3:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        withdraw_money = int(input(withdraw_message))
                        if user.__getitem__("object").money >= withdraw_money:
                            user.__getitem__("object").withdraw(withdraw_money)
                        else:
                            print("대출을 진행할까요?")
                else:
                    print(error_message)
            # 잔액
            elif menu_choice == 4:
                account_number = input(account_number_message)
                user = Bank.check_account_number(account_number)
                if user is not None:
                    if user.__getitem__("password") == input(password_message):
                        print(f'현재 잔액: {user.__getitem__("object").show_balance()}')

                else:
                    print(error_message)

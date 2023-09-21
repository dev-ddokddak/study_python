class Starbucks:

    total_stars = 0
    stars = 1
    
    

    def __init__(self, menu, price, executives_and_staff_members = False):
        self.menu = menu
        self.price = price
        self.executives_and_staff_members = executives_and_staff_members

    def sell(self, buddy):
        

        if buddy == 'executives_and_staff_members':
            discount_price = self.price - (self.price - (30 % 100))

            price = buddy.money - int(discount_price)
        
        else:
            price = buddy.money - self.price
            

        Starbucks.total_stars += Starbucks.stars


class Buddy:
    def __init__(self, nickname, stars, money, executives_and_staff_members):
        self.nickname = nickname
        self.stars = stars
        self.money = money
        self.executives_and_staff_members = executives_and_staff_members



buddy = Buddy('alex', 2, 30000, 'executives_and_staff_members')
starbucks = Starbucks('아메리카노', 4500)

starbucks.sell(buddy)
print(buddy.money)

# 36번째 줄의 'executives_and_staff_members'가 15번째줄의 if문에서
# 일치할경우 True -> 조건식으로 이어 나가고 싶은데 방법을 못찾겠음
# 고민이 더 필요함
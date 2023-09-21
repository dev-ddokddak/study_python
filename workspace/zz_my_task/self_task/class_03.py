class 집에가고싶어서쓰는_우리집으로가는버스:


    def __init__(self, numbers, color, time = 0):
        self.numbers = numbers
        self.color = color
        self.time = time

    def 어떤버스를타지(self):
        if 집에빨리가자.time == 1:
            print(f'집에가고싶다 {self.color[0]}, {self.numbers[0]}버스를 타자')

        elif 집에중간가자.time == 2:
            print(f'집에가고싶다 {self.color[1]}, {self.numbers[1]}버스를 타자')

        elif 집에늦게가자.time == 3:
            print(f'집에가고싶다 {self.color[2]}, {self.numbers[2]}버스를 타자')
        

집에빨리가자 = 집에가고싶어서쓰는_우리집으로가는버스("463", '빨간', 1)
집에중간가자 = 집에가고싶어서쓰는_우리집으로가는버스("175", '파란', 2)
집에늦게가자 = 집에가고싶어서쓰는_우리집으로가는버스("175", '초록', 3)

집에가고싶어서쓰는_우리집으로가는버스.어떤버스를타지(집에늦게가자)

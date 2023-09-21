class 포켓몬스터:
    def __init__(self, name, damage, health = 10):
        self.name = name
        self.damage = damage
        self.health = health

    def 전광석화(self):
        self.damage += 1
        self.health -= 1
    
    def 몸통박치기(self):
        self.damage += 3
        self.health -= 2

    
picka = 포켓몬스터('피카츄', 10)
mana = 포켓몬스터('망나뇽', 36)


picka.전광석화()
mana.몸통박치기()

print(picka.name, picka.damage, picka.health)
print(mana.name, mana.damage, mana.health)
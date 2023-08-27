# 일반 유닛
class Unit:
    def __init__(
        self,
        name,
        hp,
    ):
        self.name = name
        self.hp = hp


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    # location 은 전달 받은 인자를 받아서 사용
    def attack(self, location):
        print(
            "{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(
                self.name, location, self.damage
            )
        )

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파과되었습니다.".format(self.name))


firebat = AttackUnit("파이어뱃", 50, 16)
firebat.attack("5시")
firebat.damaged(25)
firebat.damaged(25)

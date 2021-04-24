"""
一个回合制游戏，有两个英雄，分别以两个类进行定义。分别是timo和police。每个英雄都有 hp 属性和 power属性，hp 代表血量，power 代表攻击力

每个英雄都有一个 fight 方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个 hp 进行对比，血量剩余多的人获胜

每个英雄都一个speak_lines方法
调用speak_lines方法，不同的角色会打印（讲出）不同的台词
timo : 提莫队长正在待命
police: 见识一下法律的子弹
"""
from First_class_zuoye.Police import police
from First_class_zuoye.Timo import timo


class herof:
    def creat_hero(self,name):
        if name == "timo":
            return timo()
        elif name == "police":
            return police()
        else:
            print("没有这个英雄")

cre_hero = herof()
tim = cre_hero.creat_hero("timo")
pol = cre_hero.creat_hero("police")
tim.fight(pol.hp,pol.power)
tim.speak_lines()
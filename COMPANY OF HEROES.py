import random


class Soldier:
    def __init__(self, id, team):
        self.id = id
        self.team = team

    def follow_hero(self, hero):
        print(f"Солдат {self.id} следует за героем {hero.id}")


class Hero:
    def __init__(self, id, team):
        self.id = id
        self.team = team

    def increase_level(self):
        print(f"Герой {self.id} уровень повышен")


hero1 = Hero(1, "Команда A")
hero2 = Hero(2, "Команда B")

soldiers_team_a = []
soldiers_team_b = []
for i in range(10):
    team = random.choice(["Команда A", "Команда B"])
    if team == "Команда A":
        soldiers_team_a.append(Soldier(i + 1, team))
    else:
        soldiers_team_b.append(Soldier(i + 1, team))

print(f"Количество солдат в команде A: {len(soldiers_team_a)}")
print(f"Количество солдат в команде B: {len(soldiers_team_b)}")

if len(soldiers_team_a) > len(soldiers_team_b):
    hero1.increase_level()
else:
    hero2.increase_level()

soldier_to_follow = random.choice(soldiers_team_a)
soldier_to_follow.follow_hero(hero1)

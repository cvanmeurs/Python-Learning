from dataclasses import dataclass

@dataclass
class Enemy:
    name: str
    maxHealth: int
    health: int
    attackPower: int
    xp: int

rat = Enemy(
    name = "Rat",
    maxHealth = 10,
    health = 10,
    attackPower = 10,
    xp = 10);

print(rat)

rat.health = rat.health - 1;

print(rat)
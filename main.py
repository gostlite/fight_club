class Warriors :
    def __init__(self, name="Warrior", health=0, attackmax=0, blockmax=0):
       self.name = name
       self.health = health
       self.attackmax = attackmax
       self.blockmax = blockmax

    def attack(self):
        attackAmt = self.attackmax * (random.random() + .5)
        return attackAmt

    def block(self):
        blockAmt = self.blockmax * (random.random() + .5)
        return blockAmt

class Battle:
    def startFight(self, warrior1, warrior2):
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game over")
                break

    @staticmethod
    def getAttackResult(warriorA, warriorB):

        warriorAAttack = warriorA.attack()
        warriorBblk = warriorB.block()
        warriorbDamage = math.ceil(warriorAAttack - warriorBblk)
        warriorB.health = warriorB.health - warriorbDamage

        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name,
        warriorbDamage))

        print("{} is down to {} health".format(warriorB.name, warriorB.health,
        warriorB.health))

        if warriorB.health <= 0:
            print("{} has Died and {} is victorious".format(warriorB.name,
            warriorA.name))
            return "Game Over"

        else:
            return "fight Again"

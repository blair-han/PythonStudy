## Class
# Starcraft game 

from random import * 

# base level unit
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} Unit is generated.".format(name))

    def move(self, location):
        print("{} is moving to {} direction. [speed {}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} damaged.".format(self.name, damage))
        self.hp -= damage
        print("{0}: HP is {1}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : destructed.".format(self.name))   

# Combat unit
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
       
    def attack(self, location):
        print("{0} : we are attaking to {1} direction. [Damage {2}]"\
            .format(self.name, location, self.damage))

# Marine
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    # stimpack : increase movement speed and firing rate by 50% at the cost of 10 HP for 11 seconds.
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : stimpack used.(-10 HP)".format(self.name))
        else:
            print("{0} : Lack of HP, can't use stimpack.".format(self.name))

# Tank
class Tank(AttackUnit):
    # Siege_mode : this locks the tank in place, but nearly doubles the tank's range and damage.
    siege_developed = False # Siege mode developed

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.siege_mode = False
    
    def set_siege_mode(self):
        if Tank.set_siege_mode == False:
            return
        
        # Siegemode off -> on
        if self.siege_mode == False:
             print("{0} : Siegemode on.".format(self.name))
             self.damage *= 2
             self.siege_mode = True
        # Siegemode on -> off
        else:
             print("{0} : Siegemode off.".format(self.name))
             self.damage /= 2
             self.siege_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : It is flying to {1} direction. [Speed {2}]".format(name, location, self.flying_speed))

# Air combat unit class
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # land speed : 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        self.fly(self.name, location)

# Wraith - air combat unit, cloaking상대방에게 보이지 않음)
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False # cloaking mode (off)
    
    def cloaking(self):
        if self.clocked == True: # cloaking mode on -> off
            print( "{0} : cloaking mode off.".format(self.name))
            self.clocked = False
        else: # cloaking mode off -> on
            print( "{0} : cloaking mode on.".format(self.name))
            self.clocked = True

def game_start():
    print ("[Alert] New game starts.")

def game_over():
    print("Player : gg") # good game
    print("[Player] left")


# Game Starts
game_start()

# Generate 3 Marine 
m1 = Marine()
m2 = Marine()
m3 = Marine()

# Generate 2 Tank
t1 = Tank()
t2 = Tank()

# Generate 1 Wraith  
w1 = Wraith()

# Manage all unit using a list (append all generaged units )
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# Move all units 
for unit in attack_units:
    unit.move("1 O'clock")

# Develop tank's seize mode.
Tank.seize_developed = True
print("[Alert] Tank siege mode has been developed.")

# Ready to attack ( Marine : stimpack, Tank: siegemode, Wraith : clocking)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_siege_mode()
    elif isinstance(unit, Wraith):
        unit.cloaking()

# All units start attacking
for unit in attack_units:
    unit.attack("1 O'clock")

# All units are damaged
for unit in attack_units:
    unit.damaged(randint(5,21)) # randomly damaged(5 ~ 20)

# End game
game_over()

import random 

# class Enemy(object):
class Enemy: 

    def __init__(self, name = 'Enemy', hit_points = 0, lives = 1): 
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._alive = True
    
    def take_damage(self, damage): 
        remaining_points = self._hit_points - damage
        if remaining_points >= 0: 
            self._hit_points = remaining_points
            print('I took {} points damage and have {} left'.format(damage, self._hit_points))
        else: 
            self._lives -= 1
            if self._lives > 0: 
                print("{0.name} lost a life".format(self))
            else: 
                print("{0.name} is dead".format(self))
                self._alive = False
    
    def __str__(self): 
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.hit_points}".format(self)


class Troll(Enemy): 
    
    def __init__(self, name): 
        # super(Troll, self).__init__(name = name, lives = 1, hit_points=23)
        super().__init__(name = name, lives = 1, hit_points=23)
    
    def grunt(self): 
        print("Me {0.name}. {0.name} stomp you".format(self))

class Vampyre(Enemy): 

    def __init__(self, name):
        super().__init__(name, hit_points = 12, lives = 3)
    
    def dodges(self): 
        if random.randint(1, 3) == 3: 
            print("**** {0.name} dodges ****".format(self))
            return True
        else: 
            return False
    
    def take_damage(self, damage):
        if not self.dodges(): 
            return super().take_damage(damage=damage)


# challenge
# create a new Vampire class that's a subclass of Enemy. 
# Vampyres have 3 lives, and take 12 hitpoints of damage
# You can create  a new Python file for the Vampyre if you like, but I'd 
# suggest adding it to the existing enemy.py file.

# Test your class by creating one or two Vampyre instances and displaying their 
# details. Also inflict some damage to make sure that take_damage method woks ok
# Also make sure that the trolls can also take damage, becase we havent tested that yet.



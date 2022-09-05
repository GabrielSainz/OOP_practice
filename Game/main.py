from turtle import get_poly
from player import Player

tim = Player('Tim')

from enemy import Enemy, Troll

# random_moster = Enemy("Basic enemy", 12, 1)
# print(random_moster)

# random_moster.take_damage(4)
# print(random_moster)

# random_moster.take_damage(8)
# print(random_moster)

# random_moster.take_damage(9)
# print(random_moster)

ugly_troll = Troll("Pug")
print('Ugly troll - {}'.format(ugly_troll))

another_troll = Troll("Ug")
print('Another troll - {}'.format(another_troll))

brother = Troll('Urg')
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# monster = Enemy('Basic enemy')
# monster.grunt()









"""
print(tim.name)
print(tim.lives)
tim.lives -= 1
print(tim.lives)

tim.lives -= 1
print(tim.lives)

tim.lives -= 1
print(tim)

tim.lives -= 1
print(tim)

tim._lives = 9
print(tim)

tim.level = 2
print(tim)

tim.level += 5
print(tim)

tim.level = 3
print(tim)

tim.score = 500
print(tim)



# Exec and eval functions. 
# 1. eval accepts only a single expression, exec can take a code block that has Python 
#   statements: loop, try: except, class and function/method def initions and so on. 
# 2. eval returns the value of the given expression, whereas exec ignores the return value 
#   from its code, and always returns None. 


x = 1

a = eval("x+1")
print(a)

a = exec("x+1")
print(a)

"""
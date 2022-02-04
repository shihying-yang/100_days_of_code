################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")


# # local scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# # print(potion_strength)


# global scope
# player_health = 10


# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()


# print(player_health)


# There is no Block Scope in Python

# if 3 > 2:
#     a_variable = 10

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

# create_enemy()


# Modifying Global Scope

# enemies = 1


# def increase_enemies():
#     # global enemies
#     # # bad practice
#     # enemies += 1     # local variable 'enemies' referenced before assignment without global
#     # better practice
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# Globacl constants
PI = 3.14159

def calc_area(radius):
    return PI * radius ** 2

print(calc_area(10))

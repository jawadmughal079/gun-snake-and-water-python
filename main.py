import random  # this module give you random number
print("Welcome snake water and gun game ")

print("\n\t\tGame rule \n")
print('''\n\nSnake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.\n\n\n''')

def gameFun(comp, you):
    if (comp == you):
        print("match are tied ")
    elif (comp == 's'):
        if (you == "g"):
            print("you are win because comp is snake and you have gun ")
        if (you == "w"):
            print("you are lose because comp is snake and you have water ")
    elif (comp == 'g'):
        if (you == "s"):
            print("you are lose because comp is gun and you have snake ")
        if (you == "w"):
            print("you are win because comp is gun and you have water ")
    elif (comp == 'w'):
        if (you == "s"):
            print("you are win because comp is water and you have snake ")
        if (you == "g"):
            print("you are lose because comp is water and you have gun ")






randomNumber = random.randint(1, 3)
if randomNumber == 1:
    comp = 's'
elif randomNumber == 2:
    comp = 'g'
elif randomNumber == 3:
    comp = 'w'

print("ComputerTURN : press  snake(s) , gun(g) and water(w)          :")
yourTurn = input("Your Turn  : press  snake(s) , gun(g) and water(w) :")



gameFun(comp,yourTurn)
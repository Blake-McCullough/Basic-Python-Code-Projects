from random import randint


def dice_roller(sides):
    result = randint(1,sides)
    print(result)

dice_roller(sides = int(input("How many sides will the dice have?\n")))

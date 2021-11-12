#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com
from random import randint


def dice_roller(sides):
    result = randint(1,sides)
    print(result)

dice_roller(sides = int(input("How many sides will the dice have?\n")))

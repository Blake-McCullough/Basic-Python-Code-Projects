#Made By Blake McCullough
#Discord - Spoiled_Kitten#4911
#Github - https://github.com/Blake-McCullough/
#Email - privblakemccullough@protonmail.com
choice = int(input("Would you like to \n 1- Convert KPH to MPH \n 2- Convert MPH to KPH\n"))

if choice == 1:
    kmh = int(input("Enter km/h: "))
    mph =  0.6214 * kmh
    print("Speed:", kmh, "KM/H =", mph, "MPH")

elif choice == 2:
    mph = int(input("Enter mp/h: "))
    kmh =  1.609344 * mph
    print("Speed:", mph, "MP/H =", kmh, "KM/H")
else:
    print("Your input is invalid")

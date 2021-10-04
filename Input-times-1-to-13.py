num = int(input("please enter a number")) #asks for a number

for number in range(1,13):
    ans = number * num #multiplies entered number for each number in the loop
    print("{0} times {1} is {2}".format(number,num,ans)) #displays results

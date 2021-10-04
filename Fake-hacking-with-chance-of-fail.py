import os 
import sys
import random
import time

succesful = random.randint(5,20)
count = 0
#last line deletion
def delete_last_line():
    "Use this function to delete the last line in the STDOUT"

    #cursor up one line
    sys.stdout.write('\x1b[1A')

    #delete last line
    sys.stdout.write('\x1b[2K')


########## FAKE HACKING PROGRAM ################

while (count < 20):
    print("Hacking.")
    time.sleep(0.1)
    delete_last_line()
    print("Hacking..")
    time.sleep(0.1)
    delete_last_line()
    print("Hacking...")
    time.sleep(0.1)
    delete_last_line()
    count = count + 1
###################SAYS HACK SUCCESSFUL################# 
################## 1/20 chance of fail! ######################

if succesful==2:
    print("Hack failed, try again")

else:
    print("HACK SUCCESSFUL!")



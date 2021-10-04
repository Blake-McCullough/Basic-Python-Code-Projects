import os 
import sys
import time
count = 0
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
print("HACK SUCCESSFUL!")


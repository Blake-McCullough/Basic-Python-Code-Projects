from calendar import monthrange #imports the calender to find the month
print("Made by Blake McCullough") #prints creators name
print("If you want to quit type 'Quit'") #tells user how to quit
#sets variable for loop
i = 0 
#sets loop until user quits
while i < 1: 
    asked_month = input("Put the month's name")#asks user to ener month
    asked_month = asked_month.capitalize() #capitalizes input
    if asked_month != "Quit":
        year = int(input("Enter the year you want"))# asks user to put in a year
    
        if year != 1-9999:
            print("error")
            continue
        
        
    
    #checks if month was January
    if asked_month == "January":
        month = 1
    
        
        
    #checks if month was Febuary
    elif asked_month =="Febuary":
        month = 2
        
        
    #checks if month was March
    elif asked_month =="March":
        month =3
        
        
    #checks if month was April
    elif asked_month =="April":
        month = 4
        
        
    #checks if month was May
    elif asked_month =="May":
        month = 5
        
        
        
    #checks if month was June
    elif asked_month =="June":
        month = 6
        
        
    #checks if month was July
    elif asked_month =="July":
        month = 7
    
        
    #checks if month was August
    elif asked_month =="August":
        month = 8
        
        
    #checks if month was September
    elif asked_month =="September":
        month = 9
        
        
    #checks if month was October
    elif asked_month =="October":
        month = 10
    
        
    #checks if month was November
    elif asked_month =="November":
        month = 11
        
        
    #checks if month was December
    elif asked_month =="December": 
        month = 12
    elif asked_month == "Quit":
        print("Thankyou for using this program")
        i = i+2
    #else:
       #print("Invalid date try again") 
   
    elif asked_month != "Quit":
        num_days = monthrange(year, month)[1] # num_days in the month
        print("The number of days in", asked_month , "is" ,num_days, "for", year) # Prints day and how many are in it

    else:
        continue
    
    
print("test")


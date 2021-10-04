


#displays creators name
print("Currency converter made by Blake McCullough")

#gets the amount that the user wishes to convert from
value = float(input("Choice a value to convert:$"))

#gets user choice for choice of currency to convert to
in_curr = input("Select a currency to convert from, Pick 'BGN','USD','EUR', or 'GBP':")

#gets user choice for choice of currency to convert to
out_curr = input("Select a currency to convert to , Pick 'BGN','USD','EUR', or 'GBP':") 

#conerts input from user to capital letters for dictionary
in_curr=in_curr.upper()
out_curr=out_curr.upper()

#list of available currencys to convert to and from
dict = {'BGN': 1, 'USD': 1.79549, 'EUR': 1.95583, 'GBP': 2.53405}

#defines the code for the currency converter
def currency_converter (value = value,in_curr = in_curr,out_curr = out_curr):
    return((dict[in_curr] / dict[out_curr]) * value)
    
#Rounds the result to 2 decimal places so that the user gets the result in cents    
rounded = round(currency_converter(),2)    

#prints the returned value
print("$",rounded)

print("Thankyou for using my code!")


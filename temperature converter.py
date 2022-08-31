celcius=float(input("enter a number in celcius:"))
farenheit=(9/5)*celcius+32

print('%0,if degree celcius =%0,if degree farenheit'%(celcius,farenheit))
temp=farenheit
if (temp>=114):
   print('it is too hot')
elif (temp<=50):
    print("it is too cool")
else:
    print("the temperature is nice")       

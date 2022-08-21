a = int(input("enter a number: "))
if (a%5 == 0 and a%3 == 0):
    print("fizzbuzz")

elif(a%5 ==0 ):
    print("fizz")  

elif(a%3 == 0 ):
    print("buzz")

else:
    print(a)        
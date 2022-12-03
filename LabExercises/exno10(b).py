'''program to calculate the fuel counsumption of your aeroplane
ask user to enter the quantity of pertol to fill up the tank and the distance covered till the tank goes dry calculate
the fuel counsumption and display it in the format  liters per 100 kilometer. Note the inverse approach of fuel consumptio
calculation distance divided by fuel is the inverse of the europian approach(fuel/diatance) also note that one kilometer is 
0.6214 miles and one liter is 0.2642 gallons  the results should be two decimal place float cost =617.23 enter the no of
liters to fill the tank 20 
enter the distance covered = 150
output = liters/100km
ans:13.33
miles/gallons 
and:17.64


sample 2 
liter :-5
output :
not a valid input 

sample input no 3 
liter = 25 
distance covered = -25
output;
invalid input
 

 for 120 km fuel consumption is 20 lit 
 then 100 km fuel consumption would be 20/150=13.
 the distance is given in km we have to convert it  into miles 150*0.6214 =93.21
 fuel consumption is given in liters we have to convert innto gallons 20*0.2642=5.2484
 then find miles div by gall 93.21/5.287=17.64
'''

liters =int(input("enter the amount of liters"))
distance=int(input("enter the dstance amount : "))

if liters<0 or distance<0:
    print("invalid input")
else:
    
    a=liters/distance
    b=a*100
    c=distance*0.6214
    d=liters*0.2642
    e =c/d
    #conversion
    x=float(b)
    y=float(e)
    '''x=str(b)
    y=str(e)
    z=x[:5]
    q=y[:5]'''
    print(round(x,2))
    print(round(y,y))
   
        
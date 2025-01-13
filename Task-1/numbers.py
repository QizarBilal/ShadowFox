#1. Write a function that takes two arguments, 145 and 'o', and uses the 'format' function to return a formatted string. Print the result. Try to identify the representation used.
def number_formatfunc(number, character):
    value = "{},{}".format(number, character)
    return value
string = number_formatfunc(145, 'o')
print("The Formatted String is :", string)
print("The Representation used is:", type(string).__name__)


#2. In a village, there is a circular pond with a radius of 84 meters. Calculate the area of the pond using the formula: Circle Area = pi*r*
radius=84
pi =3.14
Area_of_circle=pi*radius*radius
print("The Area of circle is:",Area_of_circle)
#Pond has a Water amount of 1.4 litres in a square meter
water_amount=1.4
total_water=int(Area_of_circle*water_amount)
print("The total amount of water contained in the pool is:", total_water)

#3.If you cross a 490 meter long street in 7 mins, calculate your speed in meters per second. Print the answer without any decimal point in it. (speed = distance / time)
distance=490 #meters
time=7 #minutes
#converting minutes into seconds
time=7*60
speed=int(distance/time) #Speed in meters per second
print("The speed in meters per second is:", speed)

#1. Write a program to determine the BMI Category based on the user input
Height=float(input("Enter the height in meters:"))
Weight=float(input("Enter the weight in kilograms:"))
BMI=Weight/(Height*Height)
print("The value of BMI is: ",BMI)
if BMI >=30:
    print("Obesity")
elif BMI >24 and BMI <30:
    print("Overweight")
elif 18.5<=BMI<26:
    print("Normal")
else:
    print("Underweight")
    
    
#2. Write a program to determine which country a city belongs to. Given the list of cities per country
Australia = ["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai","Abu Dhabi","Sharjah","Ajman"]
India = ["Mumbai","Bangalore","Chennai","Delhi"]
city = input("Enter a city name: ")
if city in Australia:
    print(f"{city} is in Australia")
elif city in UAE:
    print(f"{city} is in UAE")
elif city in India:
    print(f"{city} is in India")
else:
    print("City Invalid! Not Found.")
    
#3. Write a program to check if two cities belong to the same country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in Australia:
    country1 = "Australia"
elif city1 in UAE:
    country1 = "UAE"
else:
    country1 = "India"

if city2 in Australia:
    country2 = "Australia"
elif city2 in UAE:
    country2 = "UAE"
else:
    country2 = "India"

if country1 == country2:
    print(f"Both cities are in {country1}")
else:
    print("They don't belong to the same country")


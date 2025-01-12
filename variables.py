#1. Create a variable named pi and store the value 22/7 in it. Now check the data type of this variable.
pi = 22/7
print("The value of pi is=", pi)
pi_type=type(pi)
print("The data type of pi is:", pi_type)



#2. Create a variable called for and assign it a value 4. See what happens and find out the reason behind the bevavior that you see
for = 4
print("The value is":, for)
#The obtained output is an error message, this is because the word "for" is a keyword in Python and cannot be used as a variable name.



#3. Store the principal amount, rate of interest, and time in different variables and then calculate the Simple interest for 3 years. Formula: SI = (P * R * T) / 100  
P=int(input("Enter the principal amount:")) #Principal amount
R= int(input("Enter the rate_of_interest:")) #Rate_of_interest
T=3
Simple_interest=(P*R*T)/100
print(f"The Value of Simple Interest is = {Simple_interest}")
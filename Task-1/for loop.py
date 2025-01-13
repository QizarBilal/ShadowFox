#1. Using a for loop, simulate rolling a sixsided die multiple times (at least 20 times).
import random
minimum_rolls=20
count_of_6=0
count_of_1=0
sixes_in_row=0
array=[]
for i in range(minimum_rolls):
    value=random.randint(1,6)
    if value==6:
        count_of_6+=1
        array.append(value)
    elif value==1:
        count_of_1+=1
        array.append(value)
    elif value==6 and previous_value==6:
        sixes_in_row+=1
    previous_value=value
print("The count of 6's is : ",count_of_6)
print("The count of 1's is : ",count_of_1)
print("The number of times two sixes rolled in a row is: ",sixes_in_row)


#2. Write a program that asks you to perform 10 jumping jacks at a time and after every set, is asks "Are you tired"
jumpingjacks_goal = 100
completed = 0
set_size = 10
while completed < jumpingjacks_goal:
    completed += set_size
    print(f"You completed {completed} jumping jacks.")  
    if completed == jumpingjacks_goal:
        print("Congratulations! You completed the workout.")
        break 
    value = input("Are you tired?: ").lower()  
    if value in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
    else:
        remaining = jumpingjacks_goal - completed
        print(f"{remaining} jumping jacks remaining.\n")

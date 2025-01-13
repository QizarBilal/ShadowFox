#1. Create a list of your friends' names. The list should contain atleast 5 names. Create a list of tuples, each tuple should contain a friend's name and the length of the name
my_friends=["Abdullah", "Ibrahim", "Mohammed", "Ahmed", "Abdur Rahman", "Yousuf"]
tuple=[(name, len(name)) for name in my_friends]
print("The List of tuples is:", tuple)

#2.You and your partner are planning a trip, and you want to track expenses.Create two dictionaries, one for your expenses and one for your partner'sexpenses. Each dictionary should contain at least 5 expense categories and their corresponding amounts.
my_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}
my_partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}
my_total_expense = sum(my_expenses.values())
my_partner_total_expenses = sum(my_partner_expenses.values())
print(f"My total expenses: {my_total_expense}")
print(f"My partner's total expenses: {my_partner_total_expenses}")

if my_total_expense > my_partner_total_expenses:
    print("I've spent more money overall.")
elif my_total_expense < my_partner_total_expenses:
    print("My partner has spent more money overall.")
else:
    print("Both of us spent the same amount.")
print("\nSignificant differences in the expense between me and my partner is:")
for category in my_expenses:
    difference = abs(my_expenses[category] - my_partner_expenses[category])
    if difference >= 100:
        print(f"Category: {category}, Difference: {difference}")

#Daniel Lopez
#8/31/23
#Problem3NumList35.py
#ask the user to enter a number. Append each entered number to a list and add them together. Continue asking for a number until the sum of the list of numbers is greater than 100
numbers = []
total_sum = 0

while total_sum <= 100:
    user_input = int(input("Enter a number: "))
    numbers.append(user_input)
    total_sum = sum(numbers)

print("Numbers:", numbers)
print("Total Sum:", total_sum)

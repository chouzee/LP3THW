# here we define 2 args an will print their values inside
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Get a blaknet.\n")

# pass 2 nums to by calling functions
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# the same but with var values
print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# and call it
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

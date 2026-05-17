#ok guys let's build a hotel, shall we?
print("Hello! welcome to hotel Zenith!")
N = input("What is your name?\n ")
print("Welcome " + N +  ", thank you so much for coming in today!\n")
print("What whould you like to have " + N + "?\n")
M = ("chicken, seafoods and breads.\n")
print("We have " + M )
Order = input()
c = ("chicken\n")
s = ("seafoods\n")
b = ("breads\n")
if Order == "chicken":
  print("\nIn " + c + " we have, Malai chicken, Kadai chicken and Pepper chicken\n")
  print("Which one do you like to have?  " + N)
elif Order == "seafoods":
  print("\nIn " + s + " we have, Fish curry, Fish fry and Fish BBQ\n")
  print("Which one do you like to have?" + N)
elif Order == "breads":
  print("\nIn " + b + " we have, Ginger bread, Garlic bread and Butter bread\n")
print("Which one do you like to have? " + N) 
order2 = input()  

print("Good choice " + N +", we will have your order ready in a moment!")

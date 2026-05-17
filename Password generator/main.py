#Guys lets malke a passworde generetor!
#its not showing any error na
import random

letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

n = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

sc = ('/', '#', '$', '^', '&', '*', '(', ')', '-', '+')

print("Welcome to password generator!\n\n")

print("Length of the password?\n\n")
length = int(input())

#print("Does your password need numbers?")
#answer = (input())

#d = 'letters+sc'
#if answer == "yes":
  #f = 'letters+n+sc'
  #password = "".join(random.sample(f, length))
#else:
  #password = "".join(random.sample(d, length))

print("Does your password requires special characters?")
answer = (input())
if answer == "yes":
  f = "letters+n+sc"
  password = "".join(random.sample(f, length))
else:
  e = 'letters+n'
  password = "".join(random.sample(e, length))

print("Your password is: " + password)

#a = 'letters'
#b = 'n'
#c = 'sc'
#e = 'letters+n'
#global e
#d = 'letters+sc'
#f = 'letters+n+sc'

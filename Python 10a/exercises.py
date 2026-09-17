#exercise 1
welcome = "Welcome to Computer Science!"
print (welcome)
#exercise 2 
name = input("Enter your name: ")
city  = input("Enter your city: ")
print ("Hello " + name + " from " + city + "!")
#exercise 3
print (type(25))
print (type(25.0))
print (type("25"))
print (type(True))
print (type("true"))
#exercise 4
first_number = int(input("tell me the first number: "))
second_number = int(input("tell me the second number: "))
print (first_number + second_number)
#exercise 5
value = 7.89
print(int(value))
print(str(value))
print(round(value))
#exercise 6
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
print("Area: "  , width * height)
print("Perimeter: " , (width + height) * 2)
#exercise 7
temperature = int(input("Enter temperature in celcius so we'll convert it into farenheit: "))
answer = temperature * 9/5 + 32
print(round(answer, 1))
#exercise 8 
mins = int(input("Enter number of minutes so we'll convert it into hours and minutes: "))
print(mins // 60 , "hours", "and" , mins % 60 , "minutes")
#exercise 9
soum = float(input("Whats your salary in soums?: "))
print ("your tax: " , soum*0.12 )
print ("Your salary with tax: " , soum + soum*0.12)
#exercise 10
sco = float(input("Enter score 1: "))
scor = float(input("Enter score 2: "))
score = float(input("Enter score 3: "))
average = (sco + scor + score) / 3
print("Average: " + str(round(average, 2)))
#exercise 11
leonname = input("Enter your full name: ")
print(leonname.upper())
print(leonname.lower())
print(leonname.title())
#exercise 12
nah = input("Enter a sentence: ")
char_count = len(nah)
a_count = nah.lower().count('a')
print("Number of characters: " + str(char_count))
print("Number of letter a: " + str(a_count))
#exercise 13
first_name = input("Enter your first name: ")
surbottanname = input("Enter your surname: ")
first_initial = first_name[0].upper()
last_initial = surbottanname[0].upper()
print("Your initials are: " + first_initial + "." + last_initial + ".")
#exercise 14
f_name = input("Enter your full name: ")
username = f_name.lower().replace(" ", "_")
print("Your username is: " + username)
#exercise 15
email = input("Enter your email address: ").strip()
at_position = email.find("@")
username_part = email[:at_position]
print("Username part: " + username_part)
#exercise 16
word = input("Enter a word: ")
first_three = word[:3]
last_three = word[-3:]
reversed_word = word[::-1]
print("First 3 letters: " + first_three)
print("Last 3 letters: " + last_three)
print("Reversed: " + reversed_word)
#exercise 17
number = int(input("Enter a whole number: "))
if number % 2 == 0:
    print(str(number) + " is even")
else:
    print(str(number) + " is odd")
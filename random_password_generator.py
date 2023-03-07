import random, string
import sys

password = []

print()
print("*************************")
print("Random password generator")
print("*************************")
print()
print("You may decide length of passwords and how many passwords to generate.")
print()
#Prompt to ask the length of the passwords
pass_len = input("Please type in a length of the passwords (3 - 30 only): ")
#Checking numeric
if not pass_len.isnumeric():
    print("Invalid number. Please type in a positive integer.")
    sys.exit()
else:
    #length validation
    if int(pass_len) > 30 or int(pass_len) < 3:
        print("Please type only in 3 - 30 character range.")
        sys.exit()
#Prompt to ask the number of the passwords
num_of_pass = input("Please type in a number of passwords to generate (less than 100,000): ")
#Checking numeric
if not num_of_pass.isnumeric():
    print("Invalid number. Please type in a positive integer.")
    sys.exit()
else:
    #number validation
    if int(num_of_pass) > 100000 or int(num_of_pass) < 1:
        print("Only more than 1 and less than 100,000 passwords can be generated.")
        sys.exit()

# print("Length is: " + pass_len) #Checking the contents of the variables
# print("Number is: " + num_of_pass) #Checking the contents of the variables

#Generating randome password based on the criterias given in the above questions.
symbols = '.!_/`()[]+-=$#&@~'
for i in range(int(num_of_pass)):
    password.append("")
    for j in range(int(pass_len)):
        password[i] += random.choice(string.ascii_letters + string.digits + symbols)

print()

#Outputting password into a text file
f = open('password.txt', 'w', encoding='utf-8', newline='\n')
for i in range(int(num_of_pass)):
    # print(password[i])
    f.write(password[i] + '\n')
f.close

print()
print('Passwords generated. They are output in password.txt.')
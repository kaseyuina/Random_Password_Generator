# Random_Password_Generator
=========================
Random Password Generator
=========================
This program generates random passwords based on user input for length and number of passwords to generate. The passwords will be written to a text file named "password.txt".

[Requirements]
This program requires Python 3 and the following modules:

- random
- string
- sys

[How to Use]
Download or clone the repository to your local machine.
Open a terminal or command prompt and navigate to the directory where the program is located.
Run the program using the following command: python password_generator.py
Follow the prompts to enter the length of the passwords and the number of passwords to generate.
The passwords will be generated and saved to a text file named "password.txt" in the same directory as the program.

[Notes]
The password length must be between 3 and 30 characters.
The number of passwords to generate must be less than 100,000.
The generated passwords will contain a combination of uppercase and lowercase letters, numbers, and symbols.
The symbols used in the passwords are: .!_/()[]+-=$#&@~`.

[Example]
*************************
Random password generator
*************************

You may decide length of passwords and how many passwords to generate.

Please type in a length of the passwords (3 - 30 only): 8
Please type in a number of passwords to generate (less than 100,000): 5

Passwords generated. They are output in password.txt.
The contents of the "password.txt" file:

[Generated password example]
N4v4D}F2
U(4kL]g6
vS6w!yP#
h[6e)C5~
R9@tW+Z#

Author
This program was created by Tsutomu Nakajima.
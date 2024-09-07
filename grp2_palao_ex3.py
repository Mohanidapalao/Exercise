# A program for you calculate the length of a string.

def calculate_length(s):
    return len(s)

string = "Hello, Mohanida!"
print("Length of the string:", calculate_length(string))

# Output Length of the string: 16


#  A program count the number of characters in a string.

def count_characters(s):
    return len(s)

string = "Hello, Barbie!"
print("Number of characters in the string:", count_characters(string))

# Output Number of characters in the string: 14


#  A program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def change_char(s):
    first_char = s[0]
    s = s.replace(first_char, '$')
    s = first_char + s[1:]
    return s

string = "restart"
print("Modified string:", change_char(string))

# Output Modified string: resta$t


#  A program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swap_and_concatenate(m,p):
    new_m = p[:2] + m[2:]
    new_p = m[:2] + p[2:]
    return new_m + ' ' + new_p

string1 = "love"
string2 = "hate"
print("Swapped and concatenated string:", swap_and_concatenate(string1, string2))

# Output Swapped and concatenated string: have lote


# Using + Concatenate Strings in Python using 4 variables concatenate them with spaces

a = "Hello"
b = "everyone"
c = "from"
d = "alabang"
concatenated_string = a + " " + b + " " + c + " " + d
print("Concatenated string:", concatenated_string)

# Output Concatenated string: Hello everyone from alabang


# Using + Concatenate in Python using your name and your age in a paragraph

name = "Mohanida"
age = 23
paragraph = "My name is " + name + " and I am " + str(age) + " years old."
print(paragraph)

# Output My name is Mohanida and I am 23 years old.


# Using + Concatenate Strings in Python get two strings from user input and concatenate them.

string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
concatenated_string = string1 + " " + string2
print("Concatenated string:", concatenated_string)


# Output Concatenated string: Mohanida Palao

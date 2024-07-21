# Write a Python program that prints the first and last three characters of the string s as a single string.
# If the string has less than six characters, print an empty string (blank output).

string = input("Give me a string!")

if len(string) < 6:
    print("")
else:
    print(string[:3] + string[len(string) - 3:])

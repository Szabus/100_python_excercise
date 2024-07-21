# Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
# curr_char and new_char are variables that contain strings with a single character.
# You may assume that new_char will not be an empty string.
# The match must be case-sensitive (do not replace lowercase letters if curr_char is uppercase).
# If no match is found, print the initial string.

string = input("Give me a string!: ")
curr_char = input("Which char do you want to replace?")
new_char = input("what should be the new char?")
new_string = ""

for char in string:
    if char == curr_char:
        new_string += new_char
    else:
        new_string += char
print(new_string)

print(string.replace(curr_char, new_char))

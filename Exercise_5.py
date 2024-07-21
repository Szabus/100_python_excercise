# Write a Python program that prints the string s without the characters located at even indices.
# If the string is empty or only has one character, print it intact.

string = input("Give meg a string!")
newString = ""

counter = len(string)

if len(string) <= 1:
    print(string)
else:
    for counter in range(len(string)):
        if counter % 2 != 0:
            newString += string[counter]
print(newString)

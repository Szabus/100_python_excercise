# Write a Python program that prints the string s without the character at index n.
# If the index n is out of range, print the string s intact.
# If the string s is empty, print the string s intact.

string = input("Give me a string!: ")
index = int(input("Give me a number!: "))
newString = ""

if index > len(string) - 1 or len(string) == 0:
    print(string)
else:
    for numb in range(len(string)):
        if string[index] != string[numb]:
            newString += string[numb]
    print(newString)

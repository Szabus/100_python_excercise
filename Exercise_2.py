# Write a Python program that prints the character at index i in the string s.
# If the index is out of range, the program should print "i" is out of range"
# If the string is empty, the program should print "Empty String"

string = input("Give  me a string!")
i = int(input("Give me a number!"))

if i >= len(string) != 0:
    print("i is out of range")
elif len(string) == 0:
    print("Empty String")
else:
    print("the character: {}".format(string[i]))

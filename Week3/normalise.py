#normalise.py
# Author : Alan Dineen
rawString = input("Please enter a string: ")
normalisedString = rawString.strip().lower()

lengthOfRawString = len(rawString)
lengthOfNormalised = len(normalisedString)

print(f"That string normalised is: {normalisedString}")
print(f"We reduced the input string from {lengthOfRawString} to {lengthOfNormalised} characters")

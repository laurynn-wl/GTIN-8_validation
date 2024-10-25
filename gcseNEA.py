import math

# Input a 7-digit GTIN-8 code
sevendigit = int(input("Enter a 7-digit GTIN-8 code: "))  # Allows the user to enter their code
x = len(str(sevendigit))  # Checks if they entered 7 digits
if x != 7:  # Not equal to 7
    print("Your GTIN-8 code is invalid, please re-run the program.")
    exit()  # Ends the program since the code is invalid
else:
    print()

# Convert the 7-digit code to a list of digits
code_list = [int(digit) for digit in str(sevendigit)]

# Extracting digits from the list
d1, d2, d3, d4, d5, d6, d7 = code_list

# Prepare lists for calculation
list_3 = [d1, d3, d5, d7]
y3 = [3 * i for i in list_3]  # Multiplying every other number by 3
list_1 = [d2, d4, d6]
y1 = [1 * i for i in list_1]  # Multiplying every other number by 1

# Calculate totals
total1 = sum(y3)  # Adding all the numbers in this list together
total2 = sum(y1)  # Adding all the numbers in this list together

final_total = (total1 + total2)  # Total of all the numbers
nearest10 = (int(math.ceil(final_total / 10.0)) * 10)  # Finding the nearest 10 to the final total of the 7 digit GTIN-8 code
eightdigit = (nearest10 - final_total)  # Calculating the 8th digit
print("The 8th digit to your GTIN-8 code is:", eightdigit)  # Printing the 8th digit of the user's GTIN-8

# Input the full 8-digit GTIN-8 code
code = int(input("Enter all 8 digits of the GTIN-8 code: "))

X = len(str(code))  # Checking only 8 digits have been entered
if X != 8:  # Not equal to 8
    print("Your GTIN-8 code is invalid, please re-run the program.")  # Error message
    exit()  # Ends the program since the code is invalid
else:
    print()

# Convert the 8-digit code to a list of digits
code_list2 = [int(digit) for digit in str(code)]

# Extracting digits from the list
D1, D2, D3, D4, D5, D6, D7, D8 = code_list2

# Prepare lists for calculation
listt_3 = [D1, D3, D5, D7]
z3 = [3 * i for i in listt_3]  # Multiplying every other number by 3
listt_1 = [D2, D4, D6]
z1 = [1 * i for i in listt_1]  # Multiplying every other number by 1

# Calculate totals
total3 = sum(z3)  # Adding all the numbers in this list together
total4 = sum(z1)  # Adding all the numbers in this list together

final_total2 = (total3 + total4)  # Total of all the numbers
nearestt10 = (int(math.ceil(final_total2 / 10.0)) * 10)  # Finding the nearest 10 to the final total of the 8 digit GTIN-8 code
eightdigit2 = (nearestt10 - final_total2)  # Calculating the value of the eighth digit

# Validation of the eighth digit
if eightdigit2 != eightdigit:  # Checking if both of the eighth digits produced by this program are equal
    print("The eighth digit of your GTIN-8 is not valid, please re-run the program.")  # Error message
    exit()  # Stopping the program for running as the code is not valid
else:
    print("The eighth digit of your GTIN-8 is valid.")  # Displaying a message to the user stating the code is valid
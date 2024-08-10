# question 1

bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2

print(f"Each person needs to pay: ${share:}")

# question 2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 != 0:
    result = num1 / num2
    print(f"The result is: {result}")
else:
    print("Cannot divide by zero.")

# question 3

word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "{}"
word6 = "so"
word7 = "far?"

sentence = f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}"
print(sentence)

# question 4

word7 = word7.replace("?", "!")

word5 = word5.format("python")

sentence = f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}"
print(sentence)

# question 5 

statement = input("Please enter a statement: ")

length = len(statement)

print(f"The length of the statement is: {length} characters")

# question 6

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operation."

print(f"The result is: {result}")

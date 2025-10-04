# create 3 variables names
num1 = int(input ("enter a number."))
num2 =int(input ("enter a second number."))
symbol = input ("""
1. addition
2. subraction
3. multtiplication
4. division
5.
""")

if symbol == "1":
    answer = num1 + num2
if symbol == "2":
    answer = num1 - num2
if symbol == "3":
        answer = num1 * num2
if symbol == "5":
    answer = num1 / num2
print(answer)
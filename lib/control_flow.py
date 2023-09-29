#!/usr/bin/env python3

def admin_login(username, password):

    if(username.lower() == "admin" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"
    
username = "admin"
password = "12345"

access_result = admin_login(username, password)

def hows_the_weather(temperature):
    # your code here
    response = ""
    if temperature <40:
        response = "brisk"
    elif 40<= temperature <=65:
        response = "a little chilly"
    elif temperature >85:
        response = "too dang hot"
    else:
        response = "perfect"

    return f"It's {response} out there!"
    
temperature = 33

result = hows_the_weather(temperature)
print(result)

temperature = 55

result = hows_the_weather(temperature)
print(result)

temperature = 75

result = hows_the_weather(temperature)
print(result)

temperature = 99

result = hows_the_weather(temperature)
print(result)


result = hows_the_weather(temperature)
print(result)


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    
num = 10
result = fizzbuzz(num)

print(result)
    


def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation!"
    

result = calculator("+", 5, 2)
print(result)

result = calculator("-", 10, 3)
print(result)

result = calculator("*", 12, 4)
print(result)

result = calculator("/", 5, 0)
print(result)

result = calculator("", 5, 2)
print(result)
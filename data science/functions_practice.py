#1: Calculator Function

def calculator(a, b, operation):

    try:
        if operation == "+":
            return a + b

        elif operation == "-":
            return a - b

        elif operation == "*":
            return a * b

        elif operation == "/":
            return a / b

        else:
            return "Invalid Operation"

    except ZeroDivisionError:
        return "0 se divide nahi kar sakte"
print(calculator(10, 5, "+"))


#2: Temperature Converter
def temperature_convert(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit 
print(temperature_convert(25))


#3: Prime Number Check
def is_prime(num):

    if num <= 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True
print(is_prime(7))
print(is_prime(10))

#4:Factorial Function
def factorial(num):

    result = 1

    for i in range(1, num + 1):
        result = result * i

    return result
print(factorial(5))


#5:List Average
def list_average(numbers):
    return sum(numbers) / len(numbers)
nums = [10, 20, 30, 40, 50]

print(list_average(nums))

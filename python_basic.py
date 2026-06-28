#1 Even ya Odd Number
num = 7

if num % 2 == 0:
    print("Even")
else:
    print("Odd")


#2 Largest Number in List
numbers = [10, 20, 5, 40, 15]

print("Maximum:", max(numbers))


#3 String Reverse
text = "Python"

print(text[::-1])


#4 Word Count
sentence = "I love Python programming"

words = sentence.split()
print("Word Count:", len(words))


#5 Sum of Numbers from 1 to 10
total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)


#6 Multiplication Table
num = 5

for i in range(1, 11):
    print(num, "x", i, "=", num * i)


#7 Factorial
num = 5
fact = 1

for i in range(1, num + 1):
    fact *= i


#8 Count Vowels
text = "Hello World"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowels:", count)


#9 Find Largest of Three Numbers
a = 10
b = 25
c = 15

print("Largest:", max(a, b, c))


#10 Check Palindrome
text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
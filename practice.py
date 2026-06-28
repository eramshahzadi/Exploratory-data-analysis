#equal check
age=18
if age == 18:
    print("adult")
else:
    print("not adult")

#not equal
age=18
if age!=18:
    print("u r not adult")
else:
    print("u r adult")

# greater than
makrs=50
if makrs>50:
    print("pass" )
else:
    print("fail")

#less than
makrs=50
if makrs<50:
    print("you fail")
else:
    print("pass")

# greater than and eqaul
marks=50
if makrs>=50:
    print("you pass")
else:
    print("fail")
#less than and equal
marks=50
if marks<=80:
    print("you fail")
else:
    print("pass")
#even or odd
num=3
if num%2==0:
   print("even")
else:
    print("odd")

#positive or nagetive
num=-5
if num>0:
    print("positive")
else:
    print("nagetive")

#if elif else program
num=-1
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("zero")
#length check
name="iram"
print(len(name))
print(name[1])

#boolean values
student=True
if student:
    print("right")
else:
    print("wrong")
#use of in or  operater
name="iram"
if "r" in name:
    print("found")
else:
    print("not found")
#not in operater
text="iram"
if "j" not in text:
    print("not found")
else:
    print("found")

#use of and operater
age=18
student=True
if age>=18 and student:
    print("true")
else:
    print("false")

#use of or operater
age=15
if age>=18 or age>=16 :
    print("true")
else:
    print("false")

#while loop prgram 
#print counting from 1 to 10
i=1
while i<=10:
    print(i)
    i+=1
    
#from 10 to 1
i=10
while i>=1:
    print(i)
    i-=1
    
#even number from 2 to 20 
i=2
while i<=20:
    print(i)
    i+=2
#odd number
i=1
while i<=19:
    print(i)
    i+=2

# password system
password=""
while password!="python1924":
    password=input("enter password=")
print("access granted")

#guess number game
secret=3
guess=0 
while guess!=secret:
    guess=int(input("enter ur guess ="))
print("correct guess")


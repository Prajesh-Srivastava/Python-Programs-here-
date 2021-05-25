def greet(name):   #function definition
    print ("Have a Good day,"+name)
greet(" Prathima..!")      #function called


def mysum(num1,num2):
    return num1+num2
s = mysum(9,8)
print(s)

#Default_arguments
def greet(name="Stranger"):
    print ("Have a Good day,"+name)
greet(" Prathima..!")
greet()


#Recursion

#factorial
def factorial_iter(n):
   product=1
   for i in range(n):
      product=product*(i+1)
   return(product)
f= factorial_iter(9)
print(f)


def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)
s=factorial_recursive(4)
print(s)

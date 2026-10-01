radius = float(input("Enter circle radius? "))
area = 3.14 * (radius ** 2)
print(f"Circle area = {area}")

#ex2
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{int(celsius)} (C) = {fahrenheit} (F)")

#ex3
number = int(input("Enter a number? "))

is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is a NOT prime number")

    #ex4
    number = int(input("Enter a number? "))

sum_divisors = 0
if number > 0:
    for i in range(1, number):
        if number % i == 0:
            sum_divisors += i

if number > 0 and sum_divisors == number:
    print(f"{number} is a perfect number")
else:
    print(f"{number} is a NOT perfect number")


    #ex5
    colors = ["blue", "yellow", "Red", "pink", "brown", "gray"]

user_color = input("What is your favorite color? ")

if user_color in colors:
    print(f"Your colod is at index {colors.index(user_color)} in my list")
else:
    print("Sorry, I could not find your color")


    #ex6
    range1 = list(range(7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print("range1", range1)
print("range2", range2)
print("range3", range3)
print("range4", range4)


 #ex10.11.12
def   get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
def distance(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5
def print_pattern(m, n):
    for i in range(m):
        if i == 0 or i == m - 1:
            print("* " * n)
        else:
            print("*" + " " * (2 * n - 3) + "*")
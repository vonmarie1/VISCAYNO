def z(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i
    return n


x = int(input("Enter an integer >=2:"))

if x <= 1:
    print("Invalid input. Enter a number greater than 2.")
else:
    y = z(x)
    print(f"The smallest factor of {x} other than 1 is: {y}")

# Python - HW3_The Collatz Conjecture - Chia-Yu Chen

def collatz(num):
    if num % 2 == 0:        # Even
        num = num // 2
        print(num)
        return num
        
    elif num % 2 == 1:      # Odd
        num = 3 * num + 1
        print(num)
        return num


# Ask for an user input
print('Enter an integer: ')

        
try:
    number = int(input())
    
    while number != 1:
        number = collatz(number)

except ValueError:
    print('Error: Invalid Value.')
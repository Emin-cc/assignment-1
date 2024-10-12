# Prime Check Function
def is_prime(num):
    if num <= 1:
        return False  
    for i in range(2, num):
        if num % i == 0:
            return False  
    return True  

# Function to find divisor
def find_divisors(num):
    divisors = []
    for i in range(2, num):
        if num % i == 0:
            divisors.append(i)
    return divisors

# User Input
def get_positive_integer():
    while True: 
        user_input = input("Please enter the number to check: ")
        if user_input.isdigit():  
            num = int(user_input)
            if num > 0:
                return num
            else:
                print("Enter a positive number.")
        else:
            print("That is not a positive whole number. Try again.")

# Neighbouring primes
def previous_prime(num):
    for prime_candidate in range(num - 1, 1, -1):
        if is_prime(prime_candidate):
            return prime_candidate
    return None  
def next_prime(num):
    prime_candidate = num + 1
    while True:
        if is_prime(prime_candidate):
            return prime_candidate
        prime_candidate += 1

# Program logic 
def main():
    user_number = get_positive_integer()
    if is_prime(user_number):
        print(f"{user_number} is a prime number.")
    else:
        divisors = find_divisors(user_number)
        print(f"{user_number} is not prime. Its factors are: {divisors}")
    
    prev_prime = previous_prime(user_number)
    if prev_prime is not None:
        print(f"The prime number before {user_number} is {prev_prime}.")
    else:
        print("No prime number before your number.")
    
    next_p = next_prime(user_number)
    print(f"The prime number after {user_number} is {next_p}.")

if __name__ == "__main__":
    main()
    
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_prime_sum(num: int):
    """Find one prime pair that sums to num (num must be even)."""
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i):
            return i, num - i
    return None

# Ask the user for a single number
num = int(input("Enter an even natural number: "))

if num % 2 != 0:
    print("Please enter an even number.")
else:
    pair = find_prime_sum(num)
    if pair:
        print(f"{num} = {pair[0]} + {pair[1]}")
    else:
        print(f"No prime pair found for {num}")


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_up_to_n(n):
    primes = []
    for number in range(2, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes


N = int(input("Введите N"))
print(f"Простые числа от 1 до {N}: {find_primes_up_to_n(N)}")

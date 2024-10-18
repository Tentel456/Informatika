def eratosthene(n):
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


N = int(input("Введите число N:"))
print(f"Простые числа от 1 до {N} (решетом Эратосфена): {eratosthene(N)}")

def only_prime_numbers(numbers):
    primes = []

    for num in numbers:
        if num <= 1:
            continue

        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)

    return primes

entry = input("Ingrese números separados por comas: ")
numbers = [int(x) for x in entry.split(",")]

print(only_prime_numbers(numbers))
    
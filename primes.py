def primes():
    primes = set()
    n = 2
    while True:
        n_isprime = True
        for p in primes:
            if n % p == 0:
                n_isprime = False
                break
        if n_isprime:
            primes.add(n)
            yield n
        n += 1


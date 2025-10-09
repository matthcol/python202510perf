from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import math
import timeit


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True

def calcul_monothread(primes):
    return [is_prime(n) for n in primes]

def calcul_multithread(primes):
    with ThreadPoolExecutor() as pool:
        return list(pool.map(is_prime, primes))
    
def calcul_multiprocess(primes):
    with ProcessPoolExecutor() as pool:
        return list(pool.map(is_prime, primes))
    
if __name__ == "__main__":
    print("Computing")
    print("1 - Monothread")
    r = calcul_monothread(PRIMES)
    print(r)
    print("2 - Multithread")
    r = calcul_multithread(PRIMES)
    print(r)
    print("3 - Multiprocess")
    r = calcul_multithread(PRIMES)
    print(r)
    
    print()
    print("Benchmark")
    n = 7
    t1 = timeit.timeit(lambda: calcul_monothread(PRIMES), number=n)
    t2 = timeit.timeit(lambda: calcul_multithread(PRIMES), number=n)
    t3 = timeit.timeit(lambda: calcul_multiprocess(PRIMES), number=n)
    print(f"1 - Mono thread: {t1 / n:.4f} sec par exécution")
    print(f"2 - Multi threads: {t2 / n:.4f} sec par exécution")
    print(f"3 - Multi processes: {t3 / n:.4f} sec par exécution")
    
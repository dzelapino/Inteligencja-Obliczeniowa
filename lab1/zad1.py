def prime(n):
    if(n < 2):
        return False
    i = 2
    while (i*i <= n):
        if (n % i == 0):
            return False
        i = i + 1
    return True


print(prime(11))


def select_primes(x):
    result = []
    for i in x:
        if prime(i) == True:
            result.append(i)
    return result


print(select_primes([3, 6, 11, 25, 19]))

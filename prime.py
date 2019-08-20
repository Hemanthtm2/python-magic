def primes_check(n):
    primes=[]
    is_prime=True
    for divisor in range(2,n):
        if n%divisor==0:
            is_prime=False
            break
    if is_prime:
        return n
res=primes_check(3)

print(res)

def prime_number(n):
    prime = 0
    count = 0
    num = 2
    while count<n:
        if all(num % item !=0 for item in range(2,num)):
            prime += num
            count += 1
        num += 1
        
    return prime
print(prime_number(10))

# Path: prime.py

def list_prime(n):
    prime = []
    num = 2
    while len(prime)<n:
        if all(num % item !=0 for item in range(2,num)):
            prime.append(num)
        num += 1

    return prime

print(list_prime(10))

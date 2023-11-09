# import json

# data = {
#     "text": "hello world",
#     "nested_dict": {
#         "text": "hello",
#         "numbers": [1, 2, 3, "hello"]
#     },
#     "nested_list": ["apple", "banana", ["cherry", "hello"]],
#     "hello_1": {
#         "test" : ["hello", 56, {"uu": "hello"}]
#     }
# }

# def occ(data,val):
#     count = 0
#     if isinstance(data,dict):
#         for item in data.values():
#             count += occ(item,val)
#     elif isinstance(data,(list,tuple)):
#         for item in data:
#             count += occ(item,val)
#     elif isinstance(data,str):
#         if val in data:
#             count += 1
#     return count

# print(occ(data,'hello'))


# # Path: undata.py

# def first_n_primes(n):
#     primes = []
#     num = 2
#     while len(primes) < n:
#         if all(num % i != 0 for i in range(2, num)):
#             primes.append(num)
#         num += 1
#     return primes

# print(first_n_primes(100))

print(list(5 % i != 0 for i in range(2, 5)))

x = list()
for  i in range(2,5):
    if 5 % i != 0:
        x.append(i)
        
print(x)
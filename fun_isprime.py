import math


# def is_prime(num):
#
#     if num <= 1:
#         return False
#
#     for i in range(2, int(math.sqrt(num) + 1)):
#         if num % i == 0:
#             return False
#     return True

def is_prime_2(num):
    if num <= 1:
        return False

    prime = True
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            prime = False
            break
    return prime


print(is_prime_2(101))

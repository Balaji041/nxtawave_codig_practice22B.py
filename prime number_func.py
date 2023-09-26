def is_prime(number):
    # complete this function
    is_prime=True
    for i in range(2,number):
        if number%i==0:
            is_prime=False
            break
    if is_prime:
        return("Prime Number")
    else:
        return("Not a Prime Number")
number = int(input())
result = is_prime(number)# call is_prime function
print(result)

"""
input:13
output:Prime Number

"""

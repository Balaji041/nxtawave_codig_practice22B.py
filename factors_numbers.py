def factors_of_n(number):
    # complete this function    
    fact=""
    for i in range(1,number+1):
        if number%i==0:
            fact+=str(i)+" "
    return fact

number = int(input())
result =factors_of_n(number) # call the factors_of_n function
print(result)

"""
input:6
output:1 2 3 6
"""

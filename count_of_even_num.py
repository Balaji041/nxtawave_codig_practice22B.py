def get_even_numbers_count(numbers):
    # complete this function
    list_=numbers.split()
    count=0
    for i in list_:
        if int(i)%2==0:
            count+=1
    return count
numbers = input()
result =get_even_numbers_count(numbers) # call the get_even_numbers_count function
print(result)

"""
input:2 3 4 5 6 7 8
output:4
"""

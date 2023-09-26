def shuffle_string(string, indexes_list):
    # complete this function
    stri=""
    indexes_lis=indexes_list.split()
    for i in indexes_lis:
        a=int(i)
        stri+=string[a]
    return stri
        
            
string = input()
indices_list = input()

result = shuffle_string(string,indices_list) # call the shuffle_string function
print(result)

"""
input:
tonyPh
4 3 0 5 1 2
output:Python

"""

def is_prime(n):
    # complete this function
    num=""
    for i in range(1,n+1):
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            num+=str(i)+" "
    return num
            
        

n = int(input())

# call the is_prime function
print(is_prime(n))

"""
input:8
output:2 3 5 7 
"""

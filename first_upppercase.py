def get_first_upper_letter(string):
    # complete this function
    for i in string:
        if i.isupper():
            return i

string = input()
upper_case_character = get_first_upper_letter(string)# call the get_first_upper_letter function
print(upper_case_character)

"""
input:javaScrpT

output:S
"""

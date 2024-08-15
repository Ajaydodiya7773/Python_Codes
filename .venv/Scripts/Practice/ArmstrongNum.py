def Arms_num(num):
    #convert  string into number
    num_str=str(num)
    num_digit=len(num_str)
    sum_of_power=sum(int(digit)**num_digit for digit in num_str)
    return sum_of_power==num
num=int(input("Enter Number"))
if Arms_num(num):
    print("ARMStrong Number")
else:
    print("Not A Armstrong Number")
#Bit manipulation question
xor = 0 # here we initialize the xor variable to 0
nums =[4,1,2,1,2] # here we initialize the nums variable to a list of numbers
for i in nums: # here we iterate through the list of numbers
    print('num, i') # here we print the num and i variables
    xor ^= i # here we perform the xor operation (the bitwise operation) on the i variable
    print(xor) # here we print the xor variable
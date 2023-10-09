
print ("\n Hello. I'm going to check if your array is symmetric or not.")
print (" Please enter your array's sentences one by one as inputs, and when the sentences where finished print 'done' as an input ")
print (" Array's sentences must be number\n")
array = []

while True :
    user_input = input (" Please enter your input :")
    if user_input == "done" :
        break

    else :
        sentence = int (user_input)
        array.append ( sentence )

print ("\n Your array is : ")
print ( array )

for i in range (len(array)//2) :
    if array[i] != array[len(array) - 1 - i] :
        print (" This array is NOT SYMMETRIC ❌ \n")
        break

else :
    print (" This array is SYMMETRIC ✅ \n")
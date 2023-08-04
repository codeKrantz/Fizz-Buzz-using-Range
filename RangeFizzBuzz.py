# range of numbers 1-100
num_range = range(1, 101)

# converting range into a list
num_list = list(num_range)

#CREATING THE FIZZ BUZZ FEATURE
for n in num_list:
    #for fizz buzz
    if n % 3 and n % 7 == 0:

        print("Fizz Buzz")

    # for fizz
    elif n % 3 == 0:

        print("Fizz")

    # for buzz
    elif n % 7 ==0:

        print("Buzz")    

# for the rest of the numbers
    else:
        
        print(n)
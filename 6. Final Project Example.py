
# // Declare a function to check if the numbers
# // are even or odd
def even_numbers(_min, _max):
    for i in range(_min, _max):
        if i % 2 == 0:
            print("Number is Even!")
        else:
            print("Number is odd!")
            
# // Call the function      
even_numbers(0, 100)
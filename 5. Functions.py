# ///////////////
# // Functions //
# ///////////////


# // Create a simple function
def my_function():
    print("my first function!")
    
# // Then call it like so...
my_function()





# // If you want to return a value from the function...
def function_with_return():
    return "a value"

# // Then call the function like so...
my_value = function_with_return()
print(my_value)
# >> Output: "a value"





# // If you want to pass a value to the function...
def function_with_parameters(name):
    print(name)

# // Then call the function like so...
function_with_parameters("Tristan")
# >> Output: "Tristan"

# // If you don't pass the parameters
# // Example:
function_with_parameters()
# // You'll get an error. 





# // Therefore, if you want to have optional parameters...
def function_with_optional_parameters(name = "No Name!"):
    print(name)

# // Use the equals sign...
# // The call it like so...
function_with_optional_parameters(name = "Tristan")
# >> Output: "Tristan"

# // or

function_with_optional_parameters()
# >> Output: "No Name!"
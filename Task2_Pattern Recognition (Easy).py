# Checking when a number repeats itself 
def find_pattern(string):
    n = len(string)
    for i in range(1, n // 2 + 1):
        pattern = string[:i]
        repetitions = n // i
        if pattern * repetitions + string[:n % i] == string:
            return pattern, repetitions
    return None, 0

# Input string
script = input("Enter a string: ")

# Calling the function
pattern, repetitions = find_pattern(script)

if pattern is not None:
    print("Pattern Found:", pattern)
    print("Repetitions:", repetitions)
else:
    print("Pattern Not Found")

# How the code works
'''
first we define the function so that it takes a string 
as an input 
we define a loop inside the function in such a way
that if there is a pattern which is not longer than half the string, 
then pattern Found is printed and
then the no of repititions which is equal to the string's length// value of iteration no
if a pattern is no found then, pattern not found is printed 
'''

import random 

# Define function to define a random range b/w (0 - 100)
def random_range():
    start = random.randint(0,1000)
    end = random.randint(start,1000)
    return start,end

# Define function to classift which color should be printed
def color_classifier(red,green,blue):
    if (red>green and red>blue):
        return "RED"
    elif (green>red and green>blue):
        return "GREEN"
    elif (blue>red and blue>green):
        return "BLUE"
    else:
        return "Not Defined"

# call out the randon_range function to store the value of start and end of range in variables
start,end = random_range()

# Taking value of r,g,b from user within the random range we got 
value_red = int(input(f"Enter value of red (b/w {start} and {end}) "))
value_green = int(input(f"Enter value of red (b/w {start} and {end}) "))
value_blue = int(input(f"Enter value of red (b/w {start} and {end}) "))

# Call out the color)classifier function to determine the color to be printed  
color = color_classifier(value_red,value_green,value_blue)
print(f"The color is {color}")
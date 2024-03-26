
def area_of_a_triangle(height,base):
    area=float(height * base)/2
    return(area)

def volume_of_a_pyramid(length, width, height):
    volume=float(length*width*height)/3
    return(volume)


def calculator():
    calculation_options = ["Area of a triangle", "Volume of a pyramid"]
    #print(calculation_options)
    for (i,item) in enumerate(calculation_options, start=1):
        print(f"{i}. {item}")
    
    try:
        selection = int(input("Please enter a number: "))
        #print(selection)
        if selection==1:
            height = float(input("Enter height: "))
            base = float(input("Enter base: "))
            result = area_of_a_triangle(height=height, base=base)
            print(f"The Area of a triangle with a height of {height} and base {base} is {result}")

        elif selection==2:
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = volume_of_a_pyramid(length, width, height)
            print(f"The Volume of a pyramid with a length {length}, width {width} and height {height} is {result}")

        else:
            calculation_options
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

calculator()
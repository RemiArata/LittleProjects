'''
5) Define two rectangles: 
   -) one that goes from lower left of (x, y) = (-0.5, 0)
        to the upper right of (x, y) = (0.5, 1).  So it's
        a 1 x 1 square centered around x=0.
   -) the second that goes from lower left of (x, y) = (-3, 0) 
        to the upper right of (x, y) = (-2, 1).  This is also
        a 1 x 1 square that's shifted along the x axis.
Take the second rectangle, and use a loop to shift it along the 
x axis, starting at x=-3 and going to x=3 in steps of 0.1.  At

each step, compute the size of the overlap.  Print out the step
location and the size.

6) What shape does this make?

'''

from rectangle import rectangle, calc_area, find_new_square
import matplotlib.pyplot as plt

# 5) 
square_one = rectangle((-.5, 0), 1, 1)
square_two = rectangle((-3, 0), 1, 1)

tenth = .1
tenths_step = []

for _ in range(60):
    new_square = find_new_square(square_one, square_two)
    if isinstance(new_square, type(None)):
        print("Shifted Square Location")
        print(square_two)
        print("Overlap area: 0 \n")
        tenths_step.append(0)
    else:
        print("The overlap square is:")
        print(new_square)
        area = calc_area(new_square)
        print(f"The overlap area: {area} \n")
        tenths_step.append(area)
    square_two.shift_x(tenth)

plt.plot([i for i in range(60)], tenths_step)
plt.xticks([])
plt.title("Graph of Rectangle Overlap")
plt.ylabel("Area of overlap")
plt.savefig("plot_of_area_interaction.png")

# 6)
'''
The shape is a triangle wave. This makes sense because each step moves the 
    second square a linear amount. So if there is an overlap it will increase by
    a linear amount. In this case it linearly adds area until the squares are 
    perfectly overlaping (and thus the max overlap is 1). Then the area linearly 
    decreases in the same way until there is no more overlap.
'''

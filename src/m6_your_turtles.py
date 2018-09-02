"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Stephen Payne.
"""
###############################################################################
# DONE
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('midnight blue', 3)
blue_turtle.speed = 20  # Fast

bobby = rg.SimpleTurtle('turtle')
bobby.pen = rg.Pen('dark red', 17)
bobby.speed = 10

john = rg.SimpleTurtle('turtle')
john.pen = rg.Pen('yellow', 30)
john.speed = 30
# The first square will be 300 x 300 pixels:
size = 100

# Do the indented code 13 times.  Each time draws a square.
for k in range(13):

    # Put the pen down, then draw a square of the given size:
    blue_turtle.draw_square(size)

    # Move a little below and to the right of where the previous
    # square started.  Do this with the pen up (so nothing is drawn).
    blue_turtle.pen_up()
    blue_turtle.right(45)
    blue_turtle.forward(10)
    blue_turtle.left(45)

    # Put the pen down again (so drawing resumes).
    # Make the size for the NEXT square be 12 pixels smaller.
    blue_turtle.pen_down()
    size = size - 12

    blue_turtle.left(60)
    blue_turtle.forward(120)
    blue_turtle.right(120)
    blue_turtle.forward(120)
    blue_turtle.right(60)
    blue_turtle.forward(120)

for k in range(2):

    bobby.draw_circle(50)
    bobby.pen_up()
    bobby.left(90)
    bobby.forward(20)
    bobby.pen_down()

for k in range (4):
    john.pen_up()
    john.left(180)
    john.forward(50)
    john.pen_down()
    john.draw_regular_polygon(3,40)
    john.pen_up()
    john.left(90)
    john.forward(20)



window.close_on_mouse_click()

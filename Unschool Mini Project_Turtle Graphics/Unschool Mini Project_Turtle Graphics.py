### MINI PROJECT ###    ### TURTLE GRAPHICS ###
### MRIDUL KAPOOR ###   ### mridul.kapoor2002@gmail.com ###
        ### UNSCHOOL- JAVA AND PYTHON PROJECT-1 ###

#IMPORTING MODULES 
import turtle   #to create graphics
import random   #to generate random colors

#SCREEN SETTINGS
window = turtle.Screen ()               #naming screen as window
window.bgcolor("black")                 #background as black
window.colormode(255)                   #setting colors to 255
obj = turtle.Turtle()                   #turtle pen as obj

#DEFINING FUNCTION
def draw_polygon ():
    for x in range(500):                #loop
        r,b,g = random.randint(0,255),random.randint(0,255),random.randint(0,255)   #generating random color
        obj.pencolor(r,g,b)             #pen color/obj color Wwhich will draw colorful lines
        obj.speed(0)                    #speed of designing graphics #slowest = 10, fastest = 0
        obj.fd(x + 100)                 #moving forward
        obj.rt(91)                      #angle of tilting

    #TO ENSURE GRAPHICS DOESN'T STOP UNLESS CLICKED
    window.exitonclick()    

#CALLING FUNCTION
draw_polygon()


###     CODE ENDS   ###
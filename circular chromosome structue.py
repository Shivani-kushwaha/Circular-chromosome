#circular chromsome
#Import turtle library
import turtle
t = turtle.Turtle()

#Function 1: Draw outer circle
def circle():
    x = 0
    y = -100
    t.speed(5)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.circle(100)

#Function 2: Draw inner circle
def inner_circle():
    t.penup()
    x = 0
    y = -80
    t.goto(x,y)
    t.pendown()
    t.circle(80)

#Function 3: Draw first square (junction site) on the chromosome for further classification
def add_text():
    t.penup()
    t.goto(-20,-65)
    t.fillcolor("white")
    t.pendown()
    t.write("JS", True, align="Right", font = ('Ariel', '11', 'bold'))
    t.begin_fill()

    for i in range(4):
        t.forward(40)
        t.right(90)
    t.end_fill()

#Fuction 4: Draw second square and mark for centriol
def add_square():
    t.penup()
    t.goto(-20,110)
    t.pendown()
    t.fillcolor("black")
    t.write("Cen", True, align="Right", font = ('Ariel', '11', 'bold'))
    t.begin_fill()
    for i in range(4):
        t.forward(40)
        t.right(90)
    t.end_fill()



#Function 5: Label P arm and Q arm with chromosome number
def label_chromosomal_arms():
    t.penup()
    t.goto(120,0)
    t.pendown()
    t.write("Chr4 P arm", font = ('Ariel', '11', 'bold'))
    t.penup()
    t.goto(-180,0)
    t.pendown()
    t.write("Chr4 Q arm", font = ('Ariel', '11', 'bold'))


# Function 6: rectangle 1 for patient 1
def patient_one():
   t.penup()
   t.goto(-150, -150)
   t.fillcolor("Black")
   t.begin_fill()
   t.pendown()
   t.forward(300)
   t.right(90)
   t.forward(10)
   t.right(90)
   t.forward(300)
   t.right(90) 
   t.forward(10)
   t.end_fill()

#Function 7: rectangle 2 for patient 2
def patient_two():
    t.penup()
    t.left(90)
    t.left(90)
    t.goto(-150, -180)
    t.fillcolor("black")
    t.begin_fill()
    t.pendown()
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(10)
    t.end_fill()

#Function 8: rectangle 3 for patient 3
def patient_three():
    t.penup()
    t.left(90)
    t.left(90)
    t.goto(-150, -210)
    t.fillcolor("black")
    t.begin_fill()
    t.pendown()
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(10)
    t.end_fill()

#Function 9: rectangle 4 for patient 4
def patient_four():
    t.penup()
    t.left(90)
    t.left(90)
    t.goto(-150, -240)
    t.fillcolor("Black")
    t.begin_fill()
    t.pendown()
    t.left(90)
    t.forward(300)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(300)
    t.right(90)
    t.forward(10)
    t.end_fill()
    

#Label the number of patients 
#Function 10: Patient 1
def label_1():
    t.penup()
    t.forward(90)
    t.left(90)
    t.pendown()
    t.write("P1", font = ('Ariel', '11', 'bold'))

#Function 11: Patient 2
def label_2():
    t.penup()
    t.left(90)
    t.forward(30)
    t.pendown()
    t.write("P2", font = ('Ariel', '11', 'bold'))

#Function 12: Patient 3
def label_3():
    t.penup()
    t.forward(30)
    t.pendown()
    t.write("P3", font = ('Ariel', '11', 'bold'))

#Function 13: Patient 4
def label_4():
    t.penup()
    t.forward(30)
    t.pendown()
    t.write("P4", font = ('Ariel', '11', 'bold'))

#Function 14: Add the ring name
def add_ring_name():
    t.penup()
    t.left(90)
    t.left(90)
    t.forward(380)
    t.right(90)
    t.forward(135)
    t.pendown()
    t.write("r(4)", font = ('Ariel', '13', 'bold'))


#Function for marking the breakpoints with white squares in each pateint
def breakpoint_1():
    t.penup()
    t.right(90)
    t.forward(290)
    t.left(90)
    t.fillcolor("white")
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(10)
        t.right(90)
    t.end_fill()







#function for printing the image in png




#Main function 
def main():
    circle()
    inner_circle()
    add_text()
    add_square()
    label_chromosomal_arms()
    patient_one()
    patient_two()
    patient_three()
    patient_four()
    label_1()
    label_2()
    label_3()
    label_4()
    add_ring_name()
    breakpoint_1()



main()
turtle.done()
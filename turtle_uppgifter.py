import turtle as t


# Uppgift 1
# Funktionen ritar en kvadrat.
# side_length styr hur lång varje sida ska vara.
def draw_square(side_length):
    for _ in range(4):
        t.forward(side_length)
        t.left(90)


# Uppgift 2
# Funktionen flyttar pennan åt höger utan att rita.
# Den kan användas efter draw_square för att rita flera kvadrater bredvid varandra.
def move_next(distance):
    t.penup()
    t.forward(distance)
    t.pendown()


# Uppgift 3
# Funktionen ritar en cirkelliknande figur.
# steps = hur många steg/linjer som ska ritas.
# length = hur lång varje linje ska vara.
# angle = hur många grader turtle ska svänga varje gång.
#
# För en hel cirkel bör steps * angle bli 360.
# Exempel: steps=12 och angle=30 ger 12 * 30 = 360.
def draw_circle_shape(steps, length, angle):
    for _ in range(steps):
        t.forward(length)
        t.right(angle)


# Hjälpfunktion
# Flyttar turtle till början av nästa bokstav utan att rita.
def move_letter_space(distance):
    t.penup()
    t.forward(distance)
    t.pendown()


# Hjälpfunktion
# Flyttar turtle relativt från aktuell position utan att rita.
def move_without_drawing(x, y):
    t.penup()
    current_x = t.xcor()
    current_y = t.ycor()
    t.goto(current_x + x, current_y + y)
    t.pendown()


# Uppgift 4
# Bokstaven P
def draw_p(size):
    t.left(90)
    t.forward(size)
    t.right(90)
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    t.right(90)
    t.forward(size / 2)
    t.left(90)
    t.forward(size / 2)
    t.left(90)


# Bokstaven Y
def draw_y(size):
    t.penup()
    t.left(90)
    t.forward(size)
    t.right(90)
    t.pendown()

    t.right(60)
    t.forward(size / 2)
    t.left(120)
    t.forward(size / 2)

    t.backward(size / 2)
    t.right(60)
    t.forward(size / 2)

    t.left(90)


# Bokstaven T
def draw_t(size):
    t.penup()
    t.left(90)
    t.forward(size)
    t.right(90)
    t.pendown()

    t.forward(size)
    t.backward(size / 2)

    t.right(90)
    t.forward(size)
    t.left(90)


# Bokstaven H
def draw_h(size):
    t.left(90)
    t.forward(size)
    t.backward(size / 2)

    t.right(90)
    t.forward(size / 2)

    t.left(90)
    t.forward(size / 2)
    t.backward(size)

    t.right(90)


# Bokstaven O
def draw_o(size):
    for _ in range(2):
        t.forward(size / 2)
        t.left(90)
        t.forward(size)
        t.left(90)


# Bokstaven N
def draw_n(size):
    t.left(90)
    t.forward(size)

    t.right(150)
    t.forward(size * 1.15)

    t.left(150)
    t.forward(size)

    t.right(90)


# Ritar hela ordet PYTHON
def draw_python_word(size):
    draw_p(size)
    move_letter_space(size)

    draw_y(size)
    move_letter_space(size)

    draw_t(size)
    move_letter_space(size)

    draw_h(size)
    move_letter_space(size)

    draw_o(size)
    move_letter_space(size)

    draw_n(size)


# Kör turtle-demonstrationen
def run_turtle_demo():
    t.speed(6)

    # Uppgift 1 och 2:
    # Rita flera kvadrater bredvid varandra.
    for _ in range(5):
        draw_square(50)
        move_next(80)

    # Flytta till ny rad
    t.penup()
    t.goto(-200, -120)
    t.pendown()

    # Uppgift 3:
    # Rita en komplett cirkelliknande figur.
    draw_circle_shape(12, 40, 30)

    # Flytta till ny rad
    t.penup()
    t.goto(-250, -250)
    t.pendown()

    # Uppgift 4:
    # Rita ordet PYTHON.
    draw_python_word(60)

    # Låt fönstret vara öppet tills användaren stänger det.
    t.mainloop()
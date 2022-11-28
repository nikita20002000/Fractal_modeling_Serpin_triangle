import turtle

#screen settings
width, height = 1600, 900
screen = turtle.Screen()
screen.setup(width, height)
screen.screensize(3 * width, 3 * height)
screen.bgcolor('black')
screen.delay(0)

#turtle settings
nik = turtle.Turtle()
nik.pensize(3)
nik.speed(0)
nik.setpos(-width // 3, -height // 2)
nik.color('red')


#1-system settig
gens = 7
axiom = 'F'
chr_1, rule_1 = 'F', 'F-G+F+G-F'
chr_2, rule_2 = 'G', "GG"
step = 8
angle = 120

def apply_rules(axiom):
    return ''.join([rule_1 if chr == chr_1 else rule_2 if chr == chr_2 else chr for chr in axiom])

def get_result(gens, axiom):
    for gen in range(gens):
        axiom = apply_rules(axiom)
    return axiom

turtle.pencolor('white')
turtle.goto(- width // 2 + 60, height // 2 - 100)
turtle.clear()
turtle.write(f'generation: {gens}', font=("Arial", 69, "normal"))

axiom = get_result(gens, axiom)

for chr in axiom:
    if chr == chr_1 or chr == chr_2:
        nik.forward(step)
    elif chr == '+':
        nik.right(angle)
    elif chr == '-':
        nik.left(angle)

screen.exitonclick()















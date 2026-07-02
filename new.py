import turtle
import math

# --- Setup ---
t = turtle.Turtle()
t.screen.setup(width=600, height=600)
t.screen.bgcolor("black")
t.hideturtle()
t.screen.title("Python Turtle Graphics - Heart")

# --- Heart Parameters (You can adjust these) ---
scale = 15
num_points = 50
num_lines = 45
line_color = "red"

# --- Function to calculate the heart curve coordinates ---
def heart_coords(k):
    x = 16 * (math.sin(k) ** 3)
    y = 13 * math.cos(k) - 5 * math.cos(2*k) - 2 * math.cos(3*k) - math.cos(4*k)
    return x * scale, y * scale

# --- Step 1: Generate points on the heart curve ---
points = []
for i in range(num_points):
    k = (i / num_points) * (2 * math.pi)
    x, y = heart_coords(k)
    points.append((x, y))

# --- Step 2: Draw the string art ---
t.color(line_color)
t.speed(0)
t.pensize(1)
turtle.tracer(0)

for i in range(num_points):
    t.penup()
    t.goto(points[i])
    j = (i + num_lines) % num_points
    t.pendown()
    t.goto(points[j])
# --- Step 3: Display Completion Text ---
t.penup()
t.goto(0, -scale * 15)
t.color("white") 
# --- Keep the window open ---
t.write("Heart String Art", 
        align="center",
        font=("Arial", 16, "bold"))
turtle.update()
turtle.done()
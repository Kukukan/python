import turtle
import random
import time

# Set up the screen
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("navy")
screen.title("Merry Christmas from Python!")

# Create a turtle for drawing
tree = turtle.Turtle()
tree.speed(0)
tree.hideturtle()

# Create a turtle for decorations
decorations = turtle.Turtle()
decorations.speed(0)
decorations.hideturtle()

# Create a turtle for the star
star = turtle.Turtle()
star.speed(0)
star.hideturtle()

# Create a turtle for the message
message = turtle.Turtle()
message.speed(0)
message.hideturtle()

# Function to draw the tree trunk
def draw_trunk():
    tree.penup()
    tree.goto(-30, -200)
    tree.pendown()
    tree.color("saddlebrown", "sienna")
    tree.begin_fill()
    for _ in range(2):
        tree.forward(60)
        tree.left(90)
        tree.forward(40)
        tree.left(90)
    tree.end_fill()

# Function to draw a triangle (segment of the tree)
def draw_triangle(x, y, width, height, color):
    tree.penup()
    tree.goto(x, y)
    tree.pendown()
    tree.color(color)
    tree.begin_fill()
    tree.goto(x + width/2, y + height)
    tree.goto(x + width, y)
    tree.goto(x, y)
    tree.end_fill()

# Function to draw the tree
def draw_tree():
    # Draw the tree segments (from bottom to top)
    draw_triangle(-150, -150, 300, 150, "darkgreen")
    draw_triangle(-120, -50, 240, 120, "forestgreen")
    draw_triangle(-90, 50, 180, 100, "limegreen")
    
    # Draw the trunk
    draw_trunk()

# Function to draw decorations (ornaments)
def draw_decorations():
    # Define colors for ornaments
    ornament_colors = ["red", "gold", "blue", "silver", "purple", "orange", "pink"]
    
    # Draw ornaments at random positions on the tree
    for _ in range(30):
        # Random position on the tree
        x = random.randint(-140, 140)
        
        # Determine which segment the ornament should be on
        if x < -110 or x > 110:  # Bottom segment
            y_min, y_max = -150, 0
        elif x < -80 or x > 80:  # Middle segment
            y_min, y_max = -50, 70
        else:  # Top segment
            y_min, y_max = 50, 150
        
        y = random.randint(y_min, y_max)
        
        # Draw the ornament
        decorations.penup()
        decorations.goto(x, y)
        decorations.pendown()
        decorations.color(random.choice(ornament_colors))
        decorations.begin_fill()
        decorations.circle(8)
        decorations.end_fill()
        
        # Add a small highlight to each ornament
        decorations.penup()
        decorations.goto(x-3, y+5)
        decorations.pendown()
        decorations.color("white")
        decorations.begin_fill()
        decorations.circle(2)
        decorations.end_fill()

# Function to draw Christmas lights
def draw_lights():
    light_colors = ["red", "green", "gold", "blue", "yellow", "magenta"]
    
    # Draw lights along the edges of the tree segments
    segments = [
        ((-150, -150), (0, 0), (150, -150)),  # Bottom segment
        ((-120, -50), (0, 70), (120, -50)),   # Middle segment
        ((-90, 50), (0, 150), (90, 50))       # Top segment
    ]
    
    for segment in segments:
        left, top, right = segment
        
        # Calculate points along the edges
        points = []
        
        # Left edge
        for i in range(5):
            t = i / 4
            x = left[0] + (top[0] - left[0]) * t
            y = left[1] + (top[1] - left[1]) * t
            points.append((x, y))
        
        # Right edge (skip the top point to avoid duplication)
        for i in range(1, 5):
            t = i / 4
            x = top[0] + (right[0] - top[0]) * t
            y = top[1] + (right[1] - top[1]) * t
            points.append((x, y))
        
        # Draw lights at these points
        for point in points:
            decorations.penup()
            decorations.goto(point)
            decorations.pendown()
            decorations.color(random.choice(light_colors))
            decorations.begin_fill()
            decorations.circle(5)
            decorations.end_fill()

# Function to draw the star on top of the tree
def draw_star():
    star.penup()
    star.goto(0, 180)
    star.pendown()
    star.color("gold", "yellow")
    
    star.begin_fill()
    for _ in range(5):
        star.forward(40)
        star.right(144)
        star.forward(40)
        star.left(72)
    star.end_fill()

# Function to draw snowflakes
def draw_snow():
    snow = turtle.Turtle()
    snow.speed(0)
    snow.hideturtle()
    snow.color("white")
    
    for _ in range(50):
        x = random.randint(-400, 400)
        y = random.randint(-300, 300)
        size = random.randint(2, 6)
        
        snow.penup()
        snow.goto(x, y)
        snow.pendown()
        
        # Draw a simple snowflake
        for _ in range(6):
            snow.forward(size)
            snow.backward(size)
            snow.right(60)

# Function to display the message
def draw_message():
    message.penup()
    message.goto(0, -250)
    message.pendown()
    message.color("white")
    
    # Write the main message
    message.write("Merry Christmas!", align="center", font=("Arial", 24, "bold"))
    
    # Move down and write the second line
    message.penup()
    message.goto(0, -280)
    message.pendown()
    message.write("Happy Holidays from Python!", align="center", font=("Arial", 16, "normal"))

# Function to animate the lights
def animate_lights():
    # Create a turtle for animated lights
    lights = turtle.Turtle()
    lights.speed(0)
    lights.hideturtle()
    
    light_colors = ["red", "green", "gold", "blue", "yellow", "magenta", "white"]
    
    # Draw animated lights that change color
    for _ in range(20):  # Run the animation for 20 cycles
        lights.clear()
        
        # Draw blinking lights at random positions
        for _ in range(15):
            x = random.randint(-140, 140)
            
            # Determine which segment the light should be on
            if x < -110 or x > 110:  # Bottom segment
                y_min, y_max = -150, 0
            elif x < -80 or x > 80:  # Middle segment
                y_min, y_max = -50, 70
            else:  # Top segment
                y_min, y_max = 50, 150
            
            y = random.randint(y_min, y_max)
            
            # Draw the light
            lights.penup()
            lights.goto(x, y)
            lights.pendown()
            lights.color(random.choice(light_colors))
            lights.begin_fill()
            lights.circle(6)
            lights.end_fill()
        
        time.sleep(0.3)  # Pause between frames
    
    lights.clear()

# Main function to draw everything
def draw_christmas_tree():
    # Draw the tree
    draw_tree()
    
    # Draw decorations
    draw_decorations()
    
    # Draw lights
    draw_lights()
    
    # Draw the star
    draw_star()
    
    # Draw snow
    draw_snow()
    
    # Draw the message
    draw_message()
    
    # Animate lights (this will run for about 6 seconds)
    animate_lights()
    
    # Keep the window open
    turtle.done()

# Run the program
if __name__ == "__main__":
    draw_christmas_tree()
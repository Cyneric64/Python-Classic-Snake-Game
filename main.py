import turtle
import random

WIDTH = 510
HEIGHT = 510
DELAY = 150 # Ms between frames
FOOD_SIZE = 10
STEP = 20

score = 0
offsets = {
    "up": (0, STEP),
    "down": (0, -STEP),
    "left": (-STEP, 0),
    "right": (STEP, 0)
}

def game_loop():
    my_turtle.clearstamps() # Remove existing snake

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake or new_head[0] < -(WIDTH/2) or new_head[0] > WIDTH/2\
        or new_head[1] < -HEIGHT/2 or new_head[1] > HEIGHT/2:
        reset()
    else:
        # Add new head to snake body
        snake.append(new_head)

        # Check for food collision
        if not food_collision():
            # Remove the tail of the snake
            snake.pop(0) 

        # Draw the updated snake
        draw_snake()

        # Refresh screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        # Recursive loop
        screen.ontimer(game_loop, DELAY)

def draw_snake():
    for segment in snake:
        my_turtle.goto(segment[0], segment[1])
        my_turtle.color("black")
        if segment == snake[-1]:
            my_turtle.color("red") # Color the head of the snake differently
        my_turtle.stamp()

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")

def set_snake_direction(direction):
    global snake_direction
    if direction == 'up' and snake_direction != 'down': 
        snake_direction = direction
    elif direction == 'down' and snake_direction != 'up': 
        snake_direction = direction
    elif direction == 'left' and snake_direction != 'right': 
        snake_direction = direction
    elif direction == 'right' and snake_direction != 'left': 
        snake_direction = direction


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False

def get_random_food_pos():
    x = random.randint(-int((WIDTH/2)/STEP), int((WIDTH/2)/STEP))*STEP
    y = random.randint(-int((HEIGHT/2)/STEP), int((HEIGHT/2)/STEP))*STEP
    if [x, y] not in snake:
        return(x, y)
    else:
        return get_random_food_pos()

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2-y1)**2 + (x2-x1)**2)**0.5
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    # Create representation of a snake
    snake_direction = "up"
    head_start = [0, -200]
    snake = [head_start, head_start, head_start, head_start]
    
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    draw_snake()
    game_loop()




# Create a window
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("grey")
screen.tracer(0)

# Event handlers
screen.listen()
bind_direction_keys()

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("square")
my_turtle.shapesize(15/20)
my_turtle.penup()



# Create a food turtle
food = turtle.Turtle()
food.shape("circle")
food.shapesize(FOOD_SIZE/20)
food.penup()
food.color("green")

reset()

turtle.done()
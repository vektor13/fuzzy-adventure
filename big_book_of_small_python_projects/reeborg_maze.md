def turn_right():    
    for count in range(3):
        turn_left()

while not at_goal(): 
    if wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear() and wall_on_right():
        move()
    else:
        turn_right()
        move()

Reeborg's World Maze https://www.reeborg.ca/reeborg.html

As part of Day 5 in 100 Days of Python on Udemy, I spent the last three or four days really trying to figure out the best solution. What I realized is that for every move, you only know what is or isnt in front of you and what is or isnt to your right. I also realized that if forwards and right are blocked, turning left until you have a wall to the right and nothing in front of you is really helpful. From there I just travel the maze making sure that I'm always touching the right side.

#This file contains the ball class which will hold the data on the ball in pong
import math
GRAVITY = -0.5

class Ball:
    ''' Is the ball in a game of Pong '''
    def __init__(position, velocity):
        ''' This funcion takes position and velocity as tuples. of the form x,y '''
        self.position = position
        self.velocity = velocity
    def will_collide(self, position):
        ''' This function determines if a ball will collide with a given position after one time step '''
        #This function is not atm going to be used, but is a template for collisions in xandy, which for pong are more useful
        #We will be verbose here to make the code very clear, and note to come back and make it more efficient
        ball_x = self.position[0]
        ball_y = ball.position[1]
        ball_vx = ball.velocity[0]
        ball_vy = ball.velocity[1]
        intend_x = position[0]
        intend_y = position[1]
        #We assume a x/y grid like that of a normally drawn cartesian grid. So we want to know if the values cross the point, not if they actually end up on that point so we need to know where the ball is going.
        vel_x_sign = math.copysign(1, ball_vx)
        vel_y_sign = math.copysign(1, ball_vy)
        required_x = intend_x - ball_x
        required_y = intend_y - ball_y
        required_x_sign = math.copysign(1, required_x) 
        required_y_sign = math.copysign(1, required_y)
        if required_x_sign != vel_x_sign or required_y_sign != vel_y_sign:
            return False
            #Don't bother doing anything if the ball is movingthe wrong way
        else:
            if ball_x+ball_vx < vel_x_sign * intend_x or ball_y+ball_vy < vel_y_sign * intend_y:
                return False
            else:
                return True

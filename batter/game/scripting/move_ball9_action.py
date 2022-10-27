from constants import *
from game.scripting.action import Action


class MoveBall9Action(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball9 = cast.get_first_actor(BALL_GROUP_9)
        body = ball9.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
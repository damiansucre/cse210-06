from constants import *
from game.scripting.action import Action


class MoveBall8Action(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball8 = cast.get_first_actor(BALL_GROUP_8)
        body = ball8.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
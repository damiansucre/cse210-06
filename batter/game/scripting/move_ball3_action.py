from constants import *
from game.scripting.action import Action


class MoveBall3Action(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball3 = cast.get_first_actor(BALL_GROUP_3)
        body = ball3.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
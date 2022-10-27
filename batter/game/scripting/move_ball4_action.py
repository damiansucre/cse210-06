from constants import *
from game.scripting.action import Action


class MoveBall4Action(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball4 = cast.get_first_actor(BALL_GROUP_4)
        body = ball4.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
from constants import *
from game.scripting.action import Action


class MoveBall6Action(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball6 = cast.get_first_actor(BALL_GROUP_6)
        body = ball6.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
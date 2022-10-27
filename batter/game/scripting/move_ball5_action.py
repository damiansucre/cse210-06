from constants import *
from game.scripting.action import Action


class MoveBall5Action(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball5 = cast.get_first_actor(BALL_GROUP_5)
        body = ball5.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
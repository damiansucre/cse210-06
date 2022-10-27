from constants import *
from game.scripting.action import Action


class MoveBall7Action(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball7 = cast.get_first_actor(BALL_GROUP_7)
        body = ball7.get_body()
        position = body.get_position()
        velocity = body.get_velocity()
        position = position.add(velocity)
        body.set_position(position)
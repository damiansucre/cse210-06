from constants import *
from game.scripting.action import Action


class CheckOverAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        #-----------------------------------------
        ball2 = cast.get_first_actor(BALL_GROUP_2)
        body2 = ball2.get_body()
        position2 = body2.get_position()
        ball3 = cast.get_first_actor(BALL_GROUP_3)
        body3 = ball3.get_body()
        position3 = body3.get_position()
        #x = position.get_x()
        y1 = position.get_y()
        y2 = position2.get_y()
        y3 = position3.get_y()

        if y1 >= 680 and y2 >= 680 and y3 >= 680:
            stats = cast.get_first_actor(STATS_GROUP)
            stats.next_level()
            callback.on_next(NEXT_LEVEL)
        
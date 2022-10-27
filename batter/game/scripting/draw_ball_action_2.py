from constants import *
from game.scripting.action import Action


class DrawBallAction2(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball2 = cast.get_first_actor(BALL_GROUP_2)
        body = ball2.get_body()

        if ball2.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = ball2.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
from constants import *
from game.scripting.action import Action


class DrawBallAction6(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball6 = cast.get_first_actor(BALL_GROUP_6)
        body = ball6.get_body()

        if ball6.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = ball6.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
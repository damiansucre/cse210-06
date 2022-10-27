from constants import *
from game.scripting.action import Action


class DrawBallAction9(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        ball9 = cast.get_first_actor(BALL_GROUP_9)
        body = ball9.get_body()

        if ball9.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, PURPLE)
            
        image = ball9.get_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)
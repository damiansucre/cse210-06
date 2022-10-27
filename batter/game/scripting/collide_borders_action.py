from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        #over_sound = Sound(OVER_SOUND)
        #------------------------------
        ball2 = cast.get_first_actor(BALL_GROUP_2)
        body = ball2.get_body()

        ball3 = cast.get_first_actor(BALL_GROUP_3)
        body = ball3.get_body()

        ball4 = cast.get_first_actor(BALL_GROUP_4)
        body = ball4.get_body()

        ball5 = cast.get_first_actor(BALL_GROUP_5)
        body = ball5.get_body()

        ball6 = cast.get_first_actor(BALL_GROUP_6)
        body = ball6.get_body()

        ball7 = cast.get_first_actor(BALL_GROUP_7)
        body = ball7.get_body()

        ball8 = cast.get_first_actor(BALL_GROUP_8)
        body = ball8.get_body()

        ball9 = cast.get_first_actor(BALL_GROUP_9)
        body = ball9.get_body()

        ball10 = cast.get_first_actor(BALL_GROUP_10)
        body = ball10.get_body()

        if x < FIELD_LEFT:
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            #ball.bounce_y()
            #self._audio_service.play_sound(bounce_sound)
            
            #cast.remove_actor(BALL_GROUP, ball)
            #stats = cast.get_first_actor(STATS_GROUP)

            pass
    
        #------------------------------------------
        if x < FIELD_LEFT:
            ball2.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball2.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball2.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            #ball2.bounce_y()
            #self._audio_service.play_sound(bounce_sound)
            #stats = cast.get_first_actor(STATS_GROUP)
            pass

        if x < FIELD_LEFT:
            ball3.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball3.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball3.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass

        if x < FIELD_LEFT:
            ball4.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball4.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball4.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass

        if x < FIELD_LEFT:
            ball5.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball5.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball5.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass

        if x < FIELD_LEFT:
            ball6.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball6.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball6.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass

        if x < FIELD_LEFT:
            ball7.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball7.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball7.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass

        if x < FIELD_LEFT:
            ball8.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball8.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball8.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass

        if x < FIELD_LEFT:
            ball9.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball9.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball9.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass

        if x < FIELD_LEFT:
            ball10.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH):
            ball10.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        if y < FIELD_TOP:
            ball10.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH):
            pass
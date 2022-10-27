from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideRacketAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        racket = cast.get_first_actor(RACKET_GROUP)
        
        ball_body = ball.get_body()
        racket_body = racket.get_body()

        if self._physics_service.has_collided(ball_body, racket_body):
            #ball.bounce_y()
            #sound = Sound(BOUNCE_SOUND)
            #self._audio_service.play_sound(sound) 
            stats = cast.get_first_actor(STATS_GROUP)
            
            stats.lose_life()   

            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                #self._audio_service.play_sound(over_sound)
        
        #--------------------------------------------
        ball2 = cast.get_first_actor(BALL_GROUP_2)
        racket = cast.get_first_actor(RACKET_GROUP)
        
        ball_body2 = ball2.get_body()
        racket_body = racket.get_body()

        if self._physics_service.has_collided(ball_body2, racket_body):
            #ball.bounce_y()
            #sound = Sound(BOUNCE_SOUND)
            #self._audio_service.play_sound(sound) 
            stats = cast.get_first_actor(STATS_GROUP)
            
            stats.lose_life()   

            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                #self._audio_service.play_sound(over_sound)
        
        ball2 = cast.get_first_actor(BALL_GROUP_3)
        racket = cast.get_first_actor(RACKET_GROUP)
        
        ball_body2 = ball2.get_body()
        racket_body = racket.get_body()

        if self._physics_service.has_collided(ball_body2, racket_body):
            #ball.bounce_y()
            #sound = Sound(BOUNCE_SOUND)
            #self._audio_service.play_sound(sound) 
            stats = cast.get_first_actor(STATS_GROUP)
            
            stats.lose_life()   

            if stats.get_lives() > 0:
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                #self._audio_service.play_sound(over_sound)
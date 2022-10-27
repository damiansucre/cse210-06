from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        bricks = cast.get_actors(BRICK_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        #----------------------------------------------
        ball2 = cast.get_first_actor(BALL_GROUP_2)
        ball3 = cast.get_first_actor(BALL_GROUP_3)
        ball4 = cast.get_first_actor(BALL_GROUP_4)
        ball5 = cast.get_first_actor(BALL_GROUP_5)
        ball6 = cast.get_first_actor(BALL_GROUP_6)
        ball7 = cast.get_first_actor(BALL_GROUP_7)
        ball8 = cast.get_first_actor(BALL_GROUP_8)
        ball9 = cast.get_first_actor(BALL_GROUP_9)
        ball10 = cast.get_first_actor(BALL_GROUP_10)

        for brick in bricks:
            ball_body = ball.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
        
        #------------------------------------------
        for brick in bricks:
            ball_body = ball2.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball2.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
        
        for brick in bricks:
            ball_body = ball3.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball3.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)

        for brick in bricks:
            ball_body = ball4.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball4.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
        
        for brick in bricks:
            ball_body = ball5.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball5.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
        
        for brick in bricks:
            ball_body = ball6.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                ball6.bounce_y()
                sound = Sound(BOUNCE_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                cast.remove_actor(BRICK_GROUP, brick)
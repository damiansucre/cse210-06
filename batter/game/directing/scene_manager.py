import csv
from game.scripting.action_callback import ActionCallback
from constants import *
from game.casting.animation import Animation
from game.casting.ball import Ball
#----------------------
from game.casting.ball2 import Ball_2
from game.casting.ball3 import Ball_3
from game.casting.ball4 import Ball_4
from game.casting.ball5 import Ball_5
from game.casting.ball6 import Ball_6
from game.casting.ball7 import Ball_7
from game.casting.ball8 import Ball_8
from game.casting.ball9 import Ball_9
from game.casting.ball10 import Ball_10
import random

#------------------------
from game.casting.body import Body
from game.casting.brick import Brick
from game.casting.image import Image
from game.casting.label import Label
from game.casting.point import Point
from game.casting.racket import Racket
from game.casting.stats import Stats
from game.casting.text import Text 
from game.scripting.change_scene_action import ChangeSceneAction
from game.scripting.check_over_action import CheckOverAction
from game.scripting.collide_borders_action import CollideBordersAction
from game.scripting.collide_brick_action import CollideBrickAction
from game.scripting.collide_racket_action import CollideRacketAction
from game.scripting.control_racket_action import ControlRacketAction
from game.scripting.draw_ball_action import DrawBallAction
#------------------------------------------------------------
from game.scripting.draw_ball_action_2 import DrawBallAction2
from game.scripting.move_ball2_action import MoveBall2Action
from game.scripting.draw_ball_action_3 import DrawBallAction3
from game.scripting.move_ball3_action import MoveBall3Action
from game.scripting.draw_ball_action_4 import DrawBallAction4
from game.scripting.move_ball4_action import MoveBall4Action
from game.scripting.draw_ball_action_5 import DrawBallAction5
from game.scripting.move_ball5_action import MoveBall5Action
from game.scripting.draw_ball_action_6 import DrawBallAction6
from game.scripting.move_ball6_action import MoveBall6Action
from game.scripting.draw_ball_action_7 import DrawBallAction7
from game.scripting.move_ball7_action import MoveBall7Action
from game.scripting.draw_ball_action_8 import DrawBallAction8
from game.scripting.move_ball8_action import MoveBall8Action
from game.scripting.draw_ball_action_9 import DrawBallAction9
from game.scripting.move_ball9_action import MoveBall9Action
from game.scripting.draw_ball_action_10 import DrawBallAction10
from game.scripting.move_ball10_action import MoveBall10Action

from game.scripting.draw_bricks_action import DrawBricksAction
from game.scripting.draw_dialog_action import DrawDialogAction
from game.scripting.draw_hud_action import DrawHudAction
from game.scripting.draw_racket_action import DrawRacketAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.initialize_devices_action import InitializeDevicesAction
from game.scripting.load_assets_action import LoadAssetsAction
from game.scripting.move_ball_action import MoveBallAction
from game.scripting.move_racket_action import MoveRacketAction
from game.scripting.play_sound_action import PlaySoundAction
from game.scripting.release_devices_action import ReleaseDevicesAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.timed_change_scene_action import TimedChangeSceneAction
from game.scripting.unload_assets_action import UnloadAssetsAction
from game.services.raylib.raylib_audio_service import RaylibAudioService
from game.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game.services.raylib.raylib_physics_service import RaylibPhysicsService
from game.services.raylib.raylib_video_service import RaylibVideoService


class SceneManager:
    """The person in charge of setting up the cast and script for each scene."""
    
    AUDIO_SERVICE = RaylibAudioService()
    KEYBOARD_SERVICE = RaylibKeyboardService()
    PHYSICS_SERVICE = RaylibPhysicsService()
    VIDEO_SERVICE = RaylibVideoService(GAME_NAME, SCREEN_WIDTH, SCREEN_HEIGHT)

    CHECK_OVER_ACTION = CheckOverAction()
    COLLIDE_BORDERS_ACTION = CollideBordersAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_BRICKS_ACTION = CollideBrickAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    COLLIDE_RACKET_ACTION = CollideRacketAction(PHYSICS_SERVICE, AUDIO_SERVICE)
    CONTROL_RACKET_ACTION = ControlRacketAction(KEYBOARD_SERVICE)
    DRAW_BALL_ACTION = DrawBallAction(VIDEO_SERVICE)
    #-----------------------------------------------
    DRAW_BALL_ACTION_2 = DrawBallAction2(VIDEO_SERVICE)
    MOVE_BALL2_ACTION = MoveBall2Action()
    DRAW_BALL_ACTION_3 = DrawBallAction3(VIDEO_SERVICE)
    MOVE_BALL3_ACTION = MoveBall3Action()
    DRAW_BALL_ACTION_4 = DrawBallAction4(VIDEO_SERVICE)
    MOVE_BALL4_ACTION = MoveBall4Action()
    DRAW_BALL_ACTION_5 = DrawBallAction5(VIDEO_SERVICE)
    MOVE_BALL5_ACTION = MoveBall5Action()
    DRAW_BALL_ACTION_6 = DrawBallAction6(VIDEO_SERVICE)
    MOVE_BALL6_ACTION = MoveBall6Action()
    DRAW_BALL_ACTION_7 = DrawBallAction7(VIDEO_SERVICE)
    MOVE_BALL7_ACTION = MoveBall7Action()
    DRAW_BALL_ACTION_8 = DrawBallAction8(VIDEO_SERVICE)
    MOVE_BALL8_ACTION = MoveBall8Action()
    DRAW_BALL_ACTION_9 = DrawBallAction9(VIDEO_SERVICE)
    MOVE_BALL9_ACTION = MoveBall9Action()
    DRAW_BALL_ACTION_10 = DrawBallAction10(VIDEO_SERVICE)
    MOVE_BALL10_ACTION = MoveBall10Action()

    DRAW_BRICKS_ACTION = DrawBricksAction(VIDEO_SERVICE)
    DRAW_DIALOG_ACTION = DrawDialogAction(VIDEO_SERVICE)
    DRAW_HUD_ACTION = DrawHudAction(VIDEO_SERVICE)
    DRAW_RACKET_ACTION= DrawRacketAction(VIDEO_SERVICE)
    END_DRAWING_ACTION = EndDrawingAction(VIDEO_SERVICE)
    INITIALIZE_DEVICES_ACTION = InitializeDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    LOAD_ASSETS_ACTION = LoadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)
    MOVE_BALL_ACTION = MoveBallAction()
    MOVE_RACKET_ACTION = MoveRacketAction()
    RELEASE_DEVICES_ACTION = ReleaseDevicesAction(AUDIO_SERVICE, VIDEO_SERVICE)
    START_DRAWING_ACTION = StartDrawingAction(VIDEO_SERVICE)
    UNLOAD_ASSETS_ACTION = UnloadAssetsAction(AUDIO_SERVICE, VIDEO_SERVICE)

    def __init__(self):
        pass

    def prepare_scene(self, scene, cast, script):
        if scene == NEW_GAME:
            self._prepare_new_game(cast, script)
        elif scene == NEXT_LEVEL:
            self._prepare_next_level(cast, script)
        elif scene == TRY_AGAIN:
            self._prepare_try_again(cast, script)
        elif scene == IN_PLAY:
            self._prepare_in_play(cast, script)
        elif scene == GAME_OVER:    
            self._prepare_game_over(cast, script)
    
    # ----------------------------------------------------------------------------------------------
    # scene methods
    # ----------------------------------------------------------------------------------------------
    
    def _prepare_new_game(self, cast, script):
        self._add_stats(cast)
        self._add_level(cast)
        self._add_lives(cast)
        self._add_score(cast)
        self._add_ball(cast)
        #-----------------------
        self._add_ball_2(cast)
        self._add_ball_3(cast)
        self._add_ball_4(cast)
        self._add_ball_5(cast)
        self._add_ball_6(cast)
        self._add_ball_7(cast)
        self._add_ball_8(cast)
        self._add_ball_9(cast)
        self._add_ball_10(cast)
        #-----------------------
        #self._add_bricks(cast)
        self._add_racket(cast)
        self._add_dialog(cast, ENTER_TO_START)

        self._add_initialize_script(script)
        self._add_load_script(script)
        script.clear_actions(INPUT)
        script.add_action(INPUT, ChangeSceneAction(self.KEYBOARD_SERVICE, NEXT_LEVEL))
        self._add_output_script(script)
        self._add_unload_script(script)
        self._add_release_script(script)
        
    def _prepare_next_level(self, cast, script):
        self._add_ball(cast)
        #----------------------
        self._add_ball_2(cast)
        self._add_ball_3(cast)
        self._add_ball_4(cast)
        self._add_ball_5(cast)
        self._add_ball_6(cast)
        self._add_ball_7(cast)
        self._add_ball_8(cast)
        self._add_ball_9(cast)
        self._add_ball_10(cast)
        #----------------------
        #self._add_bricks(cast)
        self._add_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_output_script(script)
        script.add_action(OUTPUT, PlaySoundAction(self.AUDIO_SERVICE, WELCOME_SOUND))
        
    def _prepare_try_again(self, cast, script):
        self._add_ball(cast)
        #----------------------
        self._add_ball_2(cast)
        self._add_ball_3(cast)
        self._add_ball_4(cast)
        self._add_ball_5(cast)
        self._add_ball_6(cast)
        self._add_ball_7(cast)
        self._add_ball_8(cast)
        self._add_ball_9(cast)
        self._add_ball_10(cast)
        #----------------------
        self._add_racket(cast)
        self._add_dialog(cast, PREP_TO_LAUNCH)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(IN_PLAY, 2))
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_in_play(self, cast, script):
        self._activate_ball(cast)
        cast.clear_actors(DIALOG_GROUP)

        script.clear_actions(INPUT)
        script.add_action(INPUT, self.CONTROL_RACKET_ACTION)
        self._add_update_script(script)
        self._add_output_script(script)

    def _prepare_game_over(self, cast, script):
        self._add_ball(cast)
        #---------------------
        self._add_ball_2(cast)
        self._add_ball_3(cast)
        self._add_ball_10(cast)
        self._add_ball_4(cast)
        self._add_ball_5(cast)
        self._add_ball_6(cast)
        self._add_ball_7(cast)
        self._add_ball_8(cast)
        self._add_ball_9(cast)
        #---------------------
        self._add_racket(cast)
        self._add_dialog(cast, WAS_GOOD_GAME)

        script.clear_actions(INPUT)
        script.add_action(INPUT, TimedChangeSceneAction(NEW_GAME, 5))
        script.clear_actions(UPDATE)
        self._add_output_script(script)

    # ----------------------------------------------------------------------------------------------
    # casting methods
    # ----------------------------------------------------------------------------------------------

    def _activate_ball(self, cast):
        ball = cast.get_first_actor(BALL_GROUP)
        ball.release()
        #-----------------------
        ball2 = cast.get_first_actor(BALL_GROUP_2)
        ball2.release()
        ball3 = cast.get_first_actor(BALL_GROUP_3)
        ball3.release()
        ball4 = cast.get_first_actor(BALL_GROUP_4)
        ball4.release()
        ball5 = cast.get_first_actor(BALL_GROUP_5)
        ball5.release()
        ball6 = cast.get_first_actor(BALL_GROUP_6)
        ball6.release()
        ball7 = cast.get_first_actor(BALL_GROUP_7)
        ball7.release()
        ball8 = cast.get_first_actor(BALL_GROUP_8)
        ball8.release()
        ball9 = cast.get_first_actor(BALL_GROUP_9)
        ball9.release()
        ball10 = cast.get_first_actor(BALL_GROUP_10)
        ball10.release()
        #-----------------------

    def _add_ball(self, cast):
        cast.clear_actors(BALL_GROUP)
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP, ball)
    
    #---------------------------
    def _add_ball_2(self, cast):
        cast.clear_actors(BALL_GROUP_2)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_2, ball)
    def _add_ball_3(self, cast):
        cast.clear_actors(BALL_GROUP_3)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_3, ball)
    def _add_ball_4(self, cast):
        cast.clear_actors(BALL_GROUP_4)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_4, ball)
    def _add_ball_5(self, cast):
        cast.clear_actors(BALL_GROUP_5)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_5, ball)
    def _add_ball_6(self, cast):
        cast.clear_actors(BALL_GROUP_6)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_6, ball)
    def _add_ball_7(self, cast):
        cast.clear_actors(BALL_GROUP_7)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_7, ball)
    def _add_ball_8(self, cast):
        cast.clear_actors(BALL_GROUP_8)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_8, ball)
    def _add_ball_9(self, cast):
        cast.clear_actors(BALL_GROUP_9)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_9, ball)
    def _add_ball_10(self, cast):
        cast.clear_actors(BALL_GROUP_10)
        #---------------------
        x= random.randint(0,1000)
        #x = CENTER_X - BALL_WIDTH / 2
        y= random.randint(60,300)
        #y = SCREEN_HEIGHT - RACKET_HEIGHT - BALL_HEIGHT  
        position = Point(x, y)
        size = Point(BALL_WIDTH, BALL_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        image = Image(BALL_IMAGE)
        ball = Ball(body, image, True)
        cast.add_actor(BALL_GROUP_10, ball)
    #---------------------------------

    #def _add_bricks(self, cast):
    #    cast.clear_actors(BRICK_GROUP)
        
    #    stats = cast.get_first_actor(STATS_GROUP)
    #    level = stats.get_level() % BASE_LEVELS
    #    filename = LEVEL_FILE.format(level)

    #    with open(filename, 'r') as file:
    #        reader = csv.reader(file, skipinitialspace=True)

    #        for r, row in enumerate(reader):
    #            for c, column in enumerate(row):

    #                x = FIELD_LEFT + c * BRICK_WIDTH
    #                y = FIELD_TOP + r * BRICK_HEIGHT
    #                color = column[0]
    #                frames = int(column[1])
     #               points = BRICK_POINTS 
                    
    #                if frames == 1:
    #                    points *= 2
                    
    #                position = Point(x, y)
    #                size = Point(BRICK_WIDTH, BRICK_HEIGHT)
    #               velocity = Point(0, 0)
    #                images = BRICK_IMAGES[color][0:frames]

    #                body = Body(position, size, velocity)
     #               animation = Animation(images, BRICK_RATE, BRICK_DELAY)

    #                brick = Brick(body, animation, points)
    #                cast.add_actor(BRICK_GROUP, brick)

    def _add_dialog(self, cast, message):
        cast.clear_actors(DIALOG_GROUP)
        text = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, CENTER_Y)
        label = Label(text, position)
        cast.add_actor(DIALOG_GROUP, label)

    def _add_level(self, cast):
        cast.clear_actors(LEVEL_GROUP)
        text = Text(LEVEL_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_LEFT)
        position = Point(HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LEVEL_GROUP, label)

    def _add_lives(self, cast):
        cast.clear_actors(LIVES_GROUP)
        text = Text(LIVES_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_RIGHT)
        position = Point(SCREEN_WIDTH - HUD_MARGIN, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(LIVES_GROUP, label)

    def _add_score(self, cast):
        cast.clear_actors(SCORE_GROUP)
        text = Text(SCORE_FORMAT, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        position = Point(CENTER_X, HUD_MARGIN)
        label = Label(text, position)
        cast.add_actor(SCORE_GROUP, label)

    def _add_stats(self, cast):
        cast.clear_actors(STATS_GROUP)
        stats = Stats()
        cast.add_actor(STATS_GROUP, stats)

    def _add_racket(self, cast):
        cast.clear_actors(RACKET_GROUP)
        x = CENTER_X - RACKET_WIDTH / 2
        y = SCREEN_HEIGHT - RACKET_HEIGHT
        position = Point(x, y)
        size = Point(RACKET_WIDTH, RACKET_HEIGHT)
        velocity = Point(0, 0)
        body = Body(position, size, velocity)
        animation = Animation(RACKET_IMAGES, RACKET_RATE)
        racket = Racket(body, animation)
        cast.add_actor(RACKET_GROUP, racket)

    # ----------------------------------------------------------------------------------------------
    # scripting methods
    # ----------------------------------------------------------------------------------------------
    def _add_initialize_script(self, script):
        script.clear_actions(INITIALIZE)
        script.add_action(INITIALIZE, self.INITIALIZE_DEVICES_ACTION)

    def _add_load_script(self, script):
        script.clear_actions(LOAD)
        script.add_action(LOAD, self.LOAD_ASSETS_ACTION)
    
    def _add_output_script(self, script):
        script.clear_actions(OUTPUT)
        script.add_action(OUTPUT, self.START_DRAWING_ACTION)
        script.add_action(OUTPUT, self.DRAW_HUD_ACTION)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION)
        #-----------------------------------------------
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_2)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_3)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_4)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_5)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_6)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_7)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_8)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_9)
        script.add_action(OUTPUT, self.DRAW_BALL_ACTION_10)
        #script.add_action(OUTPUT, self.DRAW_BRICKS_ACTION)
        script.add_action(OUTPUT, self.DRAW_RACKET_ACTION)
        script.add_action(OUTPUT, self.DRAW_DIALOG_ACTION)
        script.add_action(OUTPUT, self.END_DRAWING_ACTION)

    def _add_release_script(self, script):
        script.clear_actions(RELEASE)
        script.add_action(RELEASE, self.RELEASE_DEVICES_ACTION)
    
    def _add_unload_script(self, script):
        script.clear_actions(UNLOAD)
        script.add_action(UNLOAD, self.UNLOAD_ASSETS_ACTION)
        
    def _add_update_script(self, script):
        script.clear_actions(UPDATE)
        script.add_action(UPDATE, self.MOVE_BALL_ACTION)
        #------------------------------------------------
        script.add_action(UPDATE, self.MOVE_BALL2_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL3_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL4_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL5_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL6_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL7_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL8_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL9_ACTION)
        script.add_action(UPDATE, self.MOVE_BALL10_ACTION)
        #------------------------------------------------
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.COLLIDE_BORDERS_ACTION)
        #script.add_action(UPDATE, self.COLLIDE_BRICKS_ACTION)
        script.add_action(UPDATE, self.COLLIDE_RACKET_ACTION)
        script.add_action(UPDATE, self.MOVE_RACKET_ACTION)
        script.add_action(UPDATE, self.CHECK_OVER_ACTION)
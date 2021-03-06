import constants
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.cycle import Cycle
from game.scripting.trail_grows import TrailGrows
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService



def main():
    
    
    # create the cast
    cast = Cast()
    cast.add_actor("CYCLE A", Cycle(constants.GREEN,"CYCLE A"))
    cast.add_actor("CYCLE B", Cycle(constants.RED,"CYCLE B"))
    cast.add_actor("PLAYER ONE", Score())
    cast.add_actor("PLAYER TWO", Score())


    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()
    

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("update", TrailGrows())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)



if __name__ == "__main__":
    main()
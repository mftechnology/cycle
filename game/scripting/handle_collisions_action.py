import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._who_losted = ""

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
           # self._handle_food_collision(cast)
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)
    '''''
    def _handle_cycle_collision(self, cast):
        """Updates the score nd moves the body if the snake collides with the another snake body.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        scoreA = cast.get_first_actor("PLAYER ONE")
        scoreB = cast.get_first_actor("PLAYER TWO")
        cycleA = cast.get_first_actor("CYCLE A")
        cycleB = cast.get_first_actor("CYCLE B")
        headB = cycleB.get_head()
        headA = cycleA.get_head()
        segmentsA = cycleA.get_segments()
        segmentsB = cycleB.get_segments()

        if headA.get_position().equals(segmentsB.get_position()):
            pointsB = scoreB.get_points()
            scoreB.add_points(pointsB)
            scoreA.reset()
        elif headB.get_position().equals(segmentsA.get_position()):
            pointsA = scoreA.get_points()
            scoreA.add_points(pointsA)
            scoreB.reset()
    '''        
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        # Get Score
        scoreA = cast.get_first_actor("PLAYER ONE")
        scoreB = cast.get_first_actor("PLAYER TWO")

        # To verify cycle B
        cycleA = cast.get_first_actor("CYCLE A")
        headA = cycleA.get_segments()[0]
        segmentsA = cycleA.get_segments()[1:]


         # To verify cycle B
        cycleB = cast.get_first_actor("CYCLE B")
        headB = cycleB.get_segments()[0]
        segmentsB = cycleB.get_segments()[1:]



        ##if there are colison on the cycle A = Bollean TRUE
        for segmentA in segmentsA:
            ##if there are colison on the cycle B = Bollean TRUE  
            for segmentB in segmentsB:  
                if headA.get_position().equals(segmentA.get_position()) or headA.get_position().equals(segmentB.get_position()):
                    self._is_game_over = True
                    scoreB.add_points(constants.POINTS)                           
                    self._who_losted = "CYCLE A"

                if headB.get_position().equals(segmentB.get_position()) or headB.get_position().equals(segmentA.get_position()):
                    self._is_game_over = True
                    scoreA.add_points(constants.POINTS)              
                    self._who_losted = "CYCLE B"
       
        return self._is_game_over        
         
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            actions = script.get_actions("update")
            trail_grow = actions[2]
            trail_grow.set_is_game_over(True)
            if self._who_losted == "CYCLE A" :
                cycle = cast.get_first_actor("CYCLE A")
                segments = cycle.get_segments()
            else:
                cycle = cast.get_first_actor("CYCLE B")
                segments = cycle.get_segments()
       

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text(f"GAME OVER! THE {self._who_losted} LOST!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for cycle in segments:
                cycle.set_color(constants.WHITE)
            
          



    
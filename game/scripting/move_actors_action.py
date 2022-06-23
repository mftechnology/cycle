from game.scripting.action import Action


class MoveActorsAction(Action):
    """
    An update action that moves all the actors.
    
    The responsibility of MoveActorsAction is to move all the actors that have a velocity greater
    than zero.
    """

    def execute(self, cast, script):
        """Executes the move actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        # set position score
        scoreA = cast.get_first_actor("PLAYER ONE")
        scoreB = cast.get_first_actor("PLAYER TWO")
        scoreA.set_position("PLAYER ONE")
        scoreB.set_position("PLAYER TWO")

       

        actors = cast.get_all_actors()
        for actor in actors:
            actor.move_next()
        
        
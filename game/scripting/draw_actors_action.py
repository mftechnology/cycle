from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        Player_One = cast.get_first_actor("PLAYER ONE")
        Player_Two= cast.get_first_actor("PLAYER TWO")
     
        
        
        cycleA = cast.get_first_actor("CYCLE A")
        segmentsA = cycleA.get_segments()
        
        
        cycleB = cast.get_first_actor("CYCLE B") 
        segmentsB = cycleB.get_segments()
        
        

    

        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(segmentsA)
        self._video_service.draw_actors(segmentsB)
        self._video_service.draw_actor(Player_One)
        self._video_service.draw_actor(Player_Two)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()
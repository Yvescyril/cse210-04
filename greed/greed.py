 # this file should be named __main__.py                                                          # used by

import random

from game.casting.actor import Actor                            # director.py
from game.casting.artifact import Artifact                      # director.py
from game.casting.cast import Cast                              # director.py                     

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService      # director.py
from game.services.video_service import VideoService            # director.py

from game.shared.color import Color                             # director.py
from game.shared.point import Point                             # director.py

#parameters for creating the actors
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = random.randint(1,10) #like in the director.py, the number of the primitive artifacts created
cast = Cast()


def main():
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X/2)
    y = int(MAX_Y-CELL_SIZE)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)

    # create the primitive artifacts, the following codes are the same as the function create artifacts, you can reorganize it if you will
    texts = ["O", "*"]
    for n in range(DEFAULT_ARTIFACTS):
        text = random.choice(texts)
        x = random.randint(1, MAX_X)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        cast.add_actor("artifacts", artifact)
        
       # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

if __name__ == "__main__":
    main()

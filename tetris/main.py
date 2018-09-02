"""Tetris!"""

___name___         = "Tetris"
___license___      = "MIT"
___categories___   = ["Games"]
___dependencies___ = ["dialogs", "app", "ugfx_helper", "random", "sleep", "buttons"]

import math, ugfx, ugfx_helper, time, random, sleep, buttons
from tilda import Buttons

ugfx_helper.init()
ugfx.clear()

########################################

ugfx.text(5, 5, "Hello World", ugfx.RED)
            
########################################
            
app.restart_to_default()

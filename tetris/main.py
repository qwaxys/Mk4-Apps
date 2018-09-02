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

ugfx.clear()
while true:
            if Buttons.is_pressed(Buttons.JOY_Left):     ugfx.text(5, 5, "Left", ugfx.RED)
            elif Buttons.is_pressed(Buttons.JOY_Right):  ugfx.text(5, 5, "Right", ugfx.RED)
            elif Buttons.is_pressed(Buttons.JOY_Down):   ugfx.text(5, 5, "Down", ugfx.RED)
            elif Buttons.is_pressed(Buttons.JOY_Up):     ugfx.text(5, 5, "Up", ugfx.RED)
            elif Buttons.is_pressed(Buttons.JOY_Center): ugfx.text(5, 5, "Center", ugfx.RED)
            elif Buttons.is_pressed(Buttons.BTN_Menu):   ugfx.text(5, 5, "Menu", ugfx.RED)
            elif Buttons.is_pressed(Buttons.BTN_A):      ugfx.text(5, 5, "A", ugfx.RED)
            elif Buttons.is_pressed(Buttons.BTN_B):      ugfx.text(5, 5, "B", ugfx.RED)
            sleep.wfi()
            
########################################
            
app.restart_to_default()

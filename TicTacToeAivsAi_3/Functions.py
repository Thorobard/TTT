import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import random as rnd
import time as tm
import gc
#import Global_Variables as ga
import TicTacToeAivsAi_MAIN as ttt
import Classes as cl
import CONSTANTS as cst
#put in path and dimensions x, y to get an image

def photo_ttt( path, x, y):
    photo = (Image.open(path))
    resized_photo = photo.resize((x, y), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_photo)


#ai, randomized decision making
def ai_ttt():   
    x = len(cl.GlobalVariables.list_btn)
    if x > 0:
        decision = int(rnd.random()*x)
        cl.GlobalVariables.list_btn[decision].change_color_ttt_btn()


#abstraction of victory in tic tac toe
def check_victory(x, y, z):
    
    if cl.GlobalVariables.list_game_state[x] == cl.GlobalVariables.list_game_state[y] and cl.GlobalVariables.list_game_state[y] == cl.GlobalVariables.list_game_state[z]:
        cl.GlobalVariables.victory = True
    

#test all combinations for victory
def bruteforce_victory():
        
    check_victory(0, 1, 2)
    check_victory(3, 4, 5)
    check_victory(6, 7, 8)

    check_victory(0, 3, 6)
    check_victory(1, 4, 7)
    check_victory(2, 5, 8)

    check_victory(0, 4, 8)
    check_victory(6, 4, 2)
    
#-----------------------------------------------------------------------------------------------------

#restart button function
def restart_game():
    
    cl.Button_Attributes(
        cl.TTT_Frames_and_WIN.tic_tac_toe_frame,
        cst.TTT_COLOR, 
        cl.Buttons_and_Labels.victory_label, 
        cl.Buttons_and_Labels.standings_label_yellow, 
        cl.Buttons_and_Labels.standings_label_red
    ).destroyer()

    cl.GlobalVariables.list_game_state = []
    cl.GlobalVariables.list_btn = []
    cl.GlobalVariables.victory = False
    cl.GlobalVariables.turn = False
    cl.GlobalVariables.bool_ai_vs_ai = False

    cl.Button_Attributes(
        cl.TTT_Frames_and_WIN.tic_tac_toe_frame, 
        cst.TTT_COLOR, cl.Buttons_and_Labels.victory_label, 
        cl.Buttons_and_Labels.standings_label_yellow, 
        cl.Buttons_and_Labels.standings_label_red
    ) 
       
    cl.Buttons_and_Labels.victory_label.config(
        text=""
    )   
    cl.Buttons_and_Labels.who_starts_button.config(
        background="Yellow", text="Yellow starts!"
    )

    cl.GlobalVariables.move_count = 0
    cl.GlobalVariables.data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#-----------------------------------------------------------------------------------------------------    
    

def who_starts():
   
    if len(cl.GlobalVariables.list_btn) == 9:
        if cl.GlobalVariables.turn == False:
            cl.GlobalVariables.turn = True
            cl.Buttons_and_Labels.who_starts_button.config(background="Red", text="Red Starts!")
            ai_ttt()
        else:
            cl.GlobalVariables.turn = False
            cl.Buttons_and_Labels.who_starts_button.config(background="Yellow", text="Yellow starts!")


def ai_vs_ai():
    global bool_ai_vs_ai
    bool_ai_vs_ai = True
    who_starts()

def get_loop_count():
    whatever = cl.Buttons_and_Labels.loop_count_textbox.get(1.0, 10.0)
    print(whatever)
    cl.Buttons_and_Labels.loop_count_label.configure(text=whatever)
    return int(whatever)


def loop_ai_vs_ai():
    for i in range(get_loop_count()):
        print("Durchgang:", i)
        ai_vs_ai()
        i += 1
        restart_game()



def reset_stats():
    cl.Buttons_and_Labels.standings_label_red.configure(text="0")
    cl.Buttons_and_Labels.standings_label_yellow.configure(text="0")
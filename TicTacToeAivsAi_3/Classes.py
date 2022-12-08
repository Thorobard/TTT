import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import random as rnd
import time as tm
import gc
import CONSTANTS as cst
#import TicTacToeAivsAi_3 as ttt
import Functions as ftn
#-----------------------------------------------------------------------------------------------------
class GlobalVariables:
    turn = False
    victory = False
    
    bool_ai_vs_ai = False
    move_count = 0

    list_game_state = []
    list_btn = []
    data_list = [0, 0, 0,
                0, 0, 0,
                0, 0, 0]
    data = open('data.txt', 'a')

    red_score = 0
    yellow_score = 0

#-----------------------------------------------------------------------------------------------------
class Button_TTT:


    #buttons and the lists for game state, and checking the state of the buttons (0=still white, 1=yellow(player), 2=red(ai))
    def __init__(self, x, y):
        
            
        self.int_btn = 0
        self.ttt_btn = tk.Button(TTT_Frames_and_WIN.button_frame, background=(cst.TTT_COLOR), command=self.change_color_ttt_btn)    
        self.ttt_btn.grid(row=x, column=y, sticky=tk.W+tk.E+tk.S+tk.N)

        GlobalVariables.list_btn.append(self)
        GlobalVariables.list_game_state.append(self)
        self.victory_label = Buttons_and_Labels.victory_label
        self.standings_label_yellow = Buttons_and_Labels.standings_label_yellow
        self.standings_label_red = Buttons_and_Labels.standings_label_red
        
    def destroy_the_fucking_btns(self):
        self.ttt_btn.destroy()
        print("Hello WOrld")
#-----------------------------------------------------------------------------------------------------
    #basically the game
    def change_color_ttt_btn(self):
        
        if self.int_btn == 0 and GlobalVariables.victory == False:

            #yellow turn
            if GlobalVariables.turn == False:             
                self.ttt_btn.config(background=('Yellow'))
                GlobalVariables.list_btn.remove(self)
                self.int_btn = 1
                x = GlobalVariables.list_game_state.index(self)
                GlobalVariables.list_game_state.remove(self)
                GlobalVariables.list_game_state.insert(x, self.int_btn)
                GlobalVariables.move_count += 1
                GlobalVariables.data_list[x] = 1
                ftn.bruteforce_victory()
                print(GlobalVariables.victory)
                if GlobalVariables.victory == True:
                    #print("move", move_count, "playfield = ", data_list)
                    GlobalVariables.data.write('\n')
                    GlobalVariables.data.write(str(GlobalVariables.move_count))
                    GlobalVariables.data.write(str(GlobalVariables.data_list))
                    GlobalVariables.yellow_score += 1
                    self.standings_label_yellow.config(text=GlobalVariables.yellow_score)
                    self.victory_label.config(text="Victory!")
                    
                    
                    
                GlobalVariables.turn = True
                ftn.ai_ttt()

            #red turn   
            else:               
                self.ttt_btn.config(background=('Red'))
                GlobalVariables.list_btn.remove(self)
                self.int_btn = 2
                x = GlobalVariables.list_game_state.index(self)
                GlobalVariables.list_game_state.remove(self)
                GlobalVariables.list_game_state.insert(x, self.int_btn)
                GlobalVariables.data_list[x] = 2
                if GlobalVariables.move_count > 0:
                    #data.write('\n')
                    #data.write(str(move_count))
                    #data.write(str(data_list))
                    print("move", GlobalVariables.move_count, "playfield = ", GlobalVariables.data_list)
                ftn.bruteforce_victory()
                
                if GlobalVariables.victory == True:
                    GlobalVariables.red_score += 1
                    self.standings_label_red.config(text=GlobalVariables.red_score)
                    self.victory_label.config(text="Defeat!")
                   

                GlobalVariables.turn = False
                if GlobalVariables.bool_ai_vs_ai == True:
                    ftn.ai_ttt()
#-----------------------------------------------------------------------------------------------------
    #ai, randomized decision making
    def ai_ttt():   
        x = len(GlobalVariables.list_btn)
        if x > 0:
            decision = int(rnd.random()*x)
            GlobalVariables.list_btn[decision].change_color_ttt_btn()
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
#the buttons are defined here
class Button_Attributes:


    def __init__(self):
        self.btn_0 = Button_TTT(0, 0)
        self.btn_1 = Button_TTT(0, 1)
        self.btn_2 = Button_TTT(0, 2)
        self.btn_3 = Button_TTT(1, 0)
        self.btn_4 = Button_TTT(1, 1)
        self.btn_5 = Button_TTT(1, 2)
        self.btn_6 = Button_TTT(2, 0)
        self.btn_7 = Button_TTT(2, 1)
        self.btn_8 = Button_TTT(2, 2)
    def destroyer(self):
        self.btn_0.destroy_the_fucking_btns()
        self.btn_1.destroy_the_fucking_btns()
        self.btn_2.destroy_the_fucking_btns()
        self.btn_3.destroy_the_fucking_btns()
        self.btn_4.destroy_the_fucking_btns()
        self.btn_5.destroy_the_fucking_btns()
        self.btn_6.destroy_the_fucking_btns()
        self.btn_7.destroy_the_fucking_btns()
        self.btn_8.destroy_the_fucking_btns()
        
#-----------------------------------------------------------------------------------------------------

class TTT_Frames_and_WIN:

    #WINDOW

    win = tk.Tk()
    win.geometry("900x900")
    win.configure(bg=(cst.WIN_BG))
    win.title("Tic_Tac_Toe")


    #FRAMES
    #other button frame
    button_frame = tk.Frame(win,  highlightbackground=('blueviolet'), highlightthickness=5)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)      
    button_frame.rowconfigure(0, weight=1)      
    button_frame.rowconfigure(1, weight=1)      
    button_frame.rowconfigure(2, weight=1)
    
    #button frame
    tic_tac_toe_frame = tk.Frame(
        win,
        highlightbackground=('blueviolet'), 
        highlightthickness=5
    )

    tic_tac_toe_frame.columnconfigure(0, weight=2, minsize=100)
    tic_tac_toe_frame.columnconfigure(1, weight=2, minsize=100)
    tic_tac_toe_frame.columnconfigure(2, weight=2, minsize=100)      
    tic_tac_toe_frame.rowconfigure(0, weight=2, minsize=100)      
    tic_tac_toe_frame.rowconfigure(1, weight=2, minsize=100)      
    tic_tac_toe_frame.rowconfigure(2, weight=2, minsize=100)

class Buttons_and_Labels:
#-----------------------------------------------------------------------------------------------------
    #labels
    title_label = tk.Label(
        background=cst.WIN_BG, 
        font=('Comic Sans MS', 25), 
        text="Tic-Tac-Toe!!!", 
        foreground='Skyblue'
    )

    victory_label = tk.Label(
        background=cst.WIN_BG, 
        font=('Comic Sans MS', 20),
        foreground='Gold'
    )

    standings_label_yellow = tk.Label(
        background=cst.WIN_BG, 
        font=('Comic Sans MS', 20), 
        foreground='Yellow', 
        text="0"
    )
    standings_label_red = tk.Label(
        background=cst.WIN_BG, 
        font=('Comic Sans MS', 20), 
        foreground='Red', 
        text="0"
        )

    loop_count_label = tk.Label(
        TTT_Frames_and_WIN.button_frame, 
        background=cst.WIN_BG, 
        font=('Comic Sans MS', 20), 
        foreground='GREEN', 
        text="0", 
        height=1
    )
#-----------------------------------------------------------------------------------------------------
    #buttons
    puddle_photo = ftn.photo_ttt(
        "Assets\puddle.jpg", 
        150, 100
    )
    start_button = tk.Button(
        TTT_Frames_and_WIN.button_frame, 
        text="New Game", 
        image=puddle_photo, 
        compound='bottom', 
        font=('Comic Sans MS', 20), 
        command=ftn.restart_game, 
        height=100
    )
   
    who_starts_button = tk.Button(
        TTT_Frames_and_WIN.button_frame, 
        text=("Yellow starts!"), 
        font=('Comic Sans MS', 20), 
        background='Yellow', 
        command=ftn.who_starts
    )

    ai_vs_ai_button = tk.Button(
        TTT_Frames_and_WIN.button_frame, 
        font=('Comic Sans MS', 20), 
        background='Black', 
        text="Ai vs Ai", 
        foreground="Skyblue", 
        command=ftn.ai_vs_ai
    )
    
    ai_vs_ai_loop_button = tk.Button(
        TTT_Frames_and_WIN.button_frame, 
        font=('Comic Sans MS', 20), 
        background='Black', 
        text="Ai vs Ai Loop", 
        foreground="Skyblue", 
        command=ftn.loop_ai_vs_ai
    )
    loop_count_textbox = tk.Text(
        TTT_Frames_and_WIN.button_frame, 
        font=('Comic Sans MS', 20), 
        background='Black', 
        foreground="Skyblue", 
        height=1, width=5
    )
    get_loop_count_button = tk.Button(
        TTT_Frames_and_WIN.button_frame, 
        font=('Comic Sans MS', 20), 
        background='Black', 
        text="get loop count", 
        foreground="Skyblue", 
        command=ftn.get_loop_count
    )
    
    reset_standings_button = tk.Button(
        TTT_Frames_and_WIN.button_frame, 
        font=('Comic Sans MS', 20), 
        background='Black', 
        text="reset standings", 
        foreground="Skyblue", 
        command=ftn.reset_stats
        )
#-----------------------------------------------------------------------------------------------------
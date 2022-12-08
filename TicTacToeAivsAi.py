import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import random as rnd
import time as tm

WIN_BG = '#696969'
LABEL_BG = 'Red'
BUTTON1_BG = 'Blue'
TEXT_COLROR = 'White'
TTT_COLOR = 'White'

victory = False
turn = False
bool_ai_vs_ai = False
move_count = 0

list_game_state = []
list_btn = []
data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
data = open('data.txt', 'a')

red_score = 0
yellow_score = 0


class Button_TTT:


    #buttons and the lists for game state, and checking the state of the buttons (0=still white, 1=yellow(player), 2=red(ai))
    def __init__(self, x, y):
        global list_btn    
        global list_game_state
            
        self.int_btn = 0
        self.ttt_btn = tk.Button(tic_tac_toe_frame, background=(TTT_COLOR), command=self.change_color_ttt_btn)    
        self.ttt_btn.grid(row=x, column=y, sticky=tk.W+tk.E+tk.S+tk.N)

        list_btn.append(self)
        list_game_state.append(self)
        print(self.int_btn)

    #basically the game
    def change_color_ttt_btn(self):
        global turn, red_score, yellow_score, data_list, move_count
        if self.int_btn == 0 and victory == False:

            #yellow turn
            if turn == False:             
                self.ttt_btn.config(background=('Yellow'))
                list_btn.remove(self)
                self.int_btn = 1
                x = list_game_state.index(self)
                list_game_state.remove(self)
                list_game_state.insert(x, self.int_btn)
                move_count += 1
                data_list[x] = 1
                bruteforce_victory()

                if victory == True:
                    print("move", move_count, "playfield = ", data_list)
                    data.write('\n')
                    data.write(str(move_count))
                    data.write(str(data_list))
                    yellow_score += 1
                    standings_label_yellow.config(text=yellow_score)
                    victory_label.config(text="Victory!")
                    
                    
                    
                turn = True
                ai_ttt()

            #red turn   
            else:               
                self.ttt_btn.config(background=('Red'))
                list_btn.remove(self)
                self.int_btn = 2
                x = list_game_state.index(self)
                list_game_state.remove(self)
                list_game_state.insert(x, self.int_btn)
                data_list[x] = 2
                if move_count > 0:
                    data.write('\n')
                    data.write(str(move_count))
                    data.write(str(data_list))
                    print("move", move_count, "playfield = ", data_list)
                bruteforce_victory()
                
                if victory == True:
                    red_score += 1
                    standings_label_red.config(text=red_score)
                    victory_label.config(text="Defeat!")
                   

                turn = False
                if bool_ai_vs_ai == True:
                    ai_ttt()


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


#put in path and dimensions x, y to get an image
def photo_ttt( path, x, y):
    photo = (Image.open(path))
    resized_photo = photo.resize((x, y), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_photo)


#ai, randomized decision making
def ai_ttt():   
    x = len(list_btn)
    if x > 0:
        decision = int(rnd.random()*x)
        list_btn[decision].change_color_ttt_btn()


#abstraction of victory in tic tac toe
def check_victory(x, y, z):
    global victory
    if list_game_state[x] == list_game_state[y] and list_game_state[y] == list_game_state[z]:
        victory = True


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


#restart button function
def start_game():
    global list_game_state, list_btn, victory, turn, bool_ai_vs_ai, move_count, data_list
    list_game_state = []
    list_btn = []
    victory = False
    turn = False
    bool_ai_vs_ai = False
    Button_Attributes()    
    victory_label.config(text="")   
    who_starts_button.config(background="Yellow", text="Yellow starts!")
    move_count = 0
    data_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

def who_starts():
    global who_starts_button, turn
    if len(list_btn) == 9:
        if turn == False:
            turn = True
            who_starts_button.config(background="Red", text="Red Starts!")
            ai_ttt()
        else:
            turn = False
            who_starts_button.config(background="Yellow", text="Yellow starts!")


def ai_vs_ai():
    global bool_ai_vs_ai
    bool_ai_vs_ai = True
    who_starts()

#main
def main():
    global tic_tac_toe_frame
    global victory_label
    global  standings_label_red, standings_label_yellow, who_starts_button
    
    #window
    win = tk.Tk()
    win.geometry("900x900")
    win.configure(bg=(WIN_BG))
    win.title("Tic_Tac_Toe")

    #labels
    title_label = tk.Label(background=WIN_BG, font=('Comic Sans MS', 25), text="Tic-Tac-Toe!!!", foreground='Skyblue')
    #game_state_text = tk.Label(background=WIN_BG, font=('Comic Sans MS', 9),  foreground='Skyblue', )
    victory_label = tk.Label(background=WIN_BG, font=('Comic Sans MS', 20),foreground='Gold')

    standings_label_yellow = tk.Label(background=WIN_BG, font=('Comic Sans MS', 20), foreground='Yellow', text="0")
    standings_label_red = tk.Label(background=WIN_BG, font=('Comic Sans MS', 20), foreground='Red', text="0")

    #buttons
    puddle_photo = photo_ttt("Assets\puddle.jpg", 300, 200)
    start_button = tk.Button(win, text="New Game", image=puddle_photo, compound='bottom', font=('Comic Sans MS', 20), command=start_game)

    who_starts_button = tk.Button(win, text=("Yellow starts!"), font=('Comic Sans MS', 20), background='Yellow', command=who_starts)

    ai_vs_ai_button = tk.Button(win, font=('Comic Sans MS', 20), background='Black', text="Ai vs Ai", foreground="Skyblue", command=ai_vs_ai)

    #button frame
    tic_tac_toe_frame = tk.Frame(win,  highlightbackground=('blueviolet'), highlightthickness=5)
    tic_tac_toe_frame.columnconfigure(0, weight=2)
    tic_tac_toe_frame.columnconfigure(1, weight=2)
    tic_tac_toe_frame.columnconfigure(2, weight=2)      
    tic_tac_toe_frame.rowconfigure(0, weight=2)      
    tic_tac_toe_frame.rowconfigure(1, weight=2)      
    tic_tac_toe_frame.rowconfigure(2, weight=2)      
        
    Button_Attributes()      

    #packing   
    title_label.pack(anchor=tk.N, side='top', padx=5, pady=5)

    standings_label_yellow.pack(anchor=tk.N+tk.W, padx=20, pady=50, side=tk.LEFT)
    standings_label_red.pack(anchor=tk.N+tk.E, side=tk.RIGHT, padx=20, pady=50)   

    victory_label.pack(padx=10, pady=10, )

    tic_tac_toe_frame.pack(pady=50, fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S, expand=True)

    start_button.pack(anchor=tk.N+tk.W, side=tk.LEFT)
    who_starts_button.pack(anchor=tk.N+tk.E, side=tk.RIGHT)
    ai_vs_ai_button.pack()

    #main loop
    win.mainloop()

#press F5, to start the game! 
if __name__ == '__main__':
    main()
    data.close
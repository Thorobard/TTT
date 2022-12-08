import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import random as rnd
import time as tm
win_BG = '#696969'
LABEL_BG = 'Red'
BUTTON1_BG = 'Blue'
TEXT_COLROR = 'White'
victory = False
ttt_color = 'White'
turn = False
list_game_state = []
list_btn = []


class Button_TTT:
     

    
    def __init__(self, x, y):
        global list_btn    
        global list_game_state
        self.int_btn = 0
        self.ttt_btn = tk.Button(tic_tac_toe_frame, background=(ttt_color), command=self.change_color_ttt_btn)    
        self.ttt_btn.grid(row=x, column=y, sticky=tk.W+tk.E+tk.S+tk.N)
        list_btn.append(self)
        list_game_state.append(self)
    def change_color_ttt_btn(self):
        global turn
        if self.int_btn == 0 and victory == False:
            if turn == False:             
                self.ttt_btn.config(background=('Yellow'))
                list_btn.remove(self)
                self.int_btn = 1
                x = list_game_state.index(self)
                list_game_state.remove(self)
                list_game_state.insert(x, self.int_btn)
                print(list_game_state)
                game_state_text.config(text=turn)
                bruteforce_victory()
                if victory == True:
                    victory_label.config(text="Victory!")
                    print("Victory")
                    print(turn)
                    
                turn = True
                ai_ttt()
                
            else:
                
                self.ttt_btn.config(background=('Red'))
                list_btn.remove(self)
                self.int_btn = 2
                x = list_game_state.index(self)
                list_game_state.remove(self)
                list_game_state.insert(x, self.int_btn)
                bruteforce_victory()
                if victory == True:
                    victory_label.config(text="Defeat!")
                    print("Defeat")
                    print(turn)
                turn = False
                
                

    
def photo_ttt( path, x, y):
    photo = (Image.open(path))
    resized_photo = photo.resize((x, y), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized_photo)

def ai_ttt():
    
    x = len(list_btn)
    if x > 0:
        decision = int(rnd.random()*x)
        list_btn[decision].change_color_ttt_btn()
    
def check_victory(x, y, z):
    global victory
    if list_game_state[x] == list_game_state[y] and list_game_state[y] == list_game_state[z]:
        victory = True
        

def bruteforce_victory():
    
    check_victory(0, 1, 2)
    check_victory(3, 4, 5)
    check_victory(6, 7, 8)

    check_victory(0, 3, 6)
    check_victory(1, 4, 7)
    check_victory(2, 5, 8)

    check_victory(0, 4, 8)
    check_victory(6, 4, 2)
    
            


def main():
    global tic_tac_toe_frame
    global victory_label
    global game_state_text
    win = tk.Tk()
    win.geometry("900x900")
    win.configure(bg=(win_BG))
    win.title("Tic_Tac_Toe")




    title_label = tk.Label(background=win_BG, font=('Comic Sans MS', 25), text="Tic-Tac-Toe!!!", foreground='Skyblue')
    game_state_text = tk.Label(background=win_BG, font=('Comic Sans MS', 9),  foreground='Skyblue', )
    victory_label = tk.Label(background=win_BG, font=('Comic Sans MS', 20),foreground='Gold')
    tic_tac_toe_frame = tk.Frame(win,  highlightbackground=('blueviolet'), highlightthickness=5)
    tic_tac_toe_frame.columnconfigure(0, weight=1)
    tic_tac_toe_frame.columnconfigure(1, weight=1)
    tic_tac_toe_frame.columnconfigure(2, weight=1)
    tic_tac_toe_frame.rowconfigure(0, weight=1)
    tic_tac_toe_frame.rowconfigure(1, weight=1)
    tic_tac_toe_frame.rowconfigure(2, weight=1)



        

    puddle_photo = photo_ttt("Assets\puddle.jpg", 300, 200)




    btn_0 = Button_TTT(0, 0)
    btn_1 = Button_TTT(0, 1)
    btn_2 = Button_TTT(0, 2)
    btn_3 = Button_TTT(1, 0)
    btn_4 = Button_TTT(1, 1)
    btn_5 = Button_TTT(1, 2)
    btn_6 = Button_TTT(2, 0)
    btn_7 = Button_TTT(2, 1)
    btn_8 = Button_TTT(2, 2)








    #packing
    title_label.pack(padx=5, pady=5)
    tk.Label(win, image=puddle_photo , bg="Black").pack()
    game_state_text.pack()
    victory_label.pack(padx=10, pady=10)
    tic_tac_toe_frame.pack(padx=50, pady=50, fill=tk.BOTH, expand=True)




    print(list_btn)

    win.mainloop()

 
if __name__ == '__main__':
    main()







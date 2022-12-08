import tkinter as tk
import sys
import os
from PIL import Image, ImageTk
import random as rnd
import time as tm
import gc
import Classes as cl
import CONSTANTS as cst
import Functions as ftn




#main
def main():

#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
    #allocate cells to labels and buttons
    cl.Buttons_and_Labels.start_button.grid(row=0, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
    cl.Buttons_and_Labels.who_starts_button.grid(row=0, column=1, sticky=tk.W+tk.E+tk.S+tk.N)
    cl.Buttons_and_Labels.ai_vs_ai_button.grid(row=0, column=2, sticky=tk.W+tk.E+tk.S+tk.N)
    cl.Buttons_and_Labels.ai_vs_ai_loop_button.grid(row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
    cl.Buttons_and_Labels.loop_count_textbox.grid(row=1, column=1, sticky=tk.W+tk.E+tk.S+tk.N)
    cl.Buttons_and_Labels.get_loop_count_button.grid(row=1, column=2, sticky=tk.W+tk.E+tk.S+tk.N)
    cl.Buttons_and_Labels.loop_count_label.grid(row=2, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
    cl.Buttons_and_Labels.reset_standings_button.grid(row=2, column=1, sticky=tk.W+tk.E+tk.S+tk.N)
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
    #create game board
    cl.Button_Attributes(cl.TTT_Frames_and_WIN.tic_tac_toe_frame, cst.TTT_COLOR, cl.Buttons_and_Labels.victory_label, cl.Buttons_and_Labels.standings_label_yellow, cl.Buttons_and_Labels.standings_label_red)      
#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
    #packing   
    cl.Buttons_and_Labels.title_label.pack(anchor=tk.N, side='top', padx=5, pady=5)

    cl.Buttons_and_Labels.standings_label_yellow.pack(anchor=tk.N+tk.W, padx=20, pady=50, side=tk.LEFT)
    cl.Buttons_and_Labels.standings_label_red.pack(anchor=tk.N+tk.E, side=tk.RIGHT, padx=20, pady=50)   
    
    cl.Buttons_and_Labels.victory_label.pack(padx=10, pady=10, )
    cl.TTT_Frames_and_WIN.button_frame.pack(fill=tk.BOTH, side=tk.TOP, anchor=tk.N, expand=True)
    cl.TTT_Frames_and_WIN.tic_tac_toe_frame.pack(pady=25, fill=tk.BOTH, side=tk.BOTTOM, anchor=tk.S, expand=True)
#-----------------------------------------------------------------------------------------------------
   
    cl.TTT_Frames_and_WIN.win.mainloop()

#-----------------------------------------------------------------------------------------------------
#press F5, to start the game! 
if __name__ == '__main__':
    main()
    cl.GlobalVariables.data.close
#-----------------------------------------------------------------------------------------------------
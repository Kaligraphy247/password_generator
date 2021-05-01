# GUI for password generator

# Credits
# =================================
# icons from www.iconarchive.com
# back link to https://icons8.com
# ================================

import tkinter, os, webbrowser, schedule, time, os
from tkinter import PhotoImage, BOTH, END, messagebox


def main():
# HIGH LEVEL-ish FUNCTION
    def set_icon():
        """ Sets icons based on OS """
        if os.name == "nt":
            root.iconbitmap('img/password.ico')
        if os.name == 'posix':
            root_img = PhotoImage(file = 'img/password.png')
            root.iconphoto(False, root_img)

    # define window
    root = tkinter.Tk()
    root.geometry("520x320")
    root.resizable(0,0)
    root.title("Password Generator")
    set_icon()


    # FUNCTIONS


    # LAYOUTS
    auto_gen_frame = tkinter.LabelFrame(root, padx=5, pady=5)
    gen_frame = tkinter.LabelFrame(root, padx=5, pady=5)
    auto_gen_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
    gen_frame.pack(fill=BOTH, expand=True, padx=5,pady=5)
    

    # AUTO GENERATE PASSWORD LAYOUT
    auto_title = tkinter.Label(auto_gen_frame, text="Auto Generate",)
    auto_title.grid(expand=True)











    root.mainloop()

# PROGRAM ENDS
main()
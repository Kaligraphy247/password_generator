# GUI for password generator

# Credits
# =================================
# icons from www.iconarchive.com
# back link to https://icons8.com
# ================================

from tkinter import PhotoImage, BOTH, END, messagebox
import tkinter, time, os

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
    def generate_password():
        '''Generates Password'''
        print(gen_pass_entry.get())
        password_generator = secrets.token_hex(gen_pass_entry) # gen. the password
        


    # LAYOUTS
    auto_gen_frame = tkinter.LabelFrame(root, padx=5, pady=5)
    gen_frame = tkinter.LabelFrame(root, padx=5, pady=5)
    auto_gen_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
    gen_frame.pack(fill=BOTH, expand=True, padx=5,pady=5)
    

    # AUTO GENERATE PASSWORD LAYOUT
    auto_title = tkinter.Label(auto_gen_frame, text="Auto Generate", underline=0)
    auto_gen_msg = tkinter.Label(auto_gen_frame, text="Password Length")
    auto_gen_entry_box = tkinter.Entry(auto_gen_frame, width=45)
    auto_gen_btn = tkinter.Button(auto_gen_frame, text="Generate", width=8, height=1, underline=0 )
    auto_gen_export_btn = tkinter.Button(auto_gen_frame, text="Export", width=8, height=1, underline=0)

    # grid
    auto_title.grid(row=0, column=0)
    auto_gen_msg.grid(row=1, column=0)
    auto_gen_entry_box.grid(row=1, column=1, padx=5, pady=5, sticky="WE")
    auto_gen_btn.grid(row=2, column=0,sticky="W")
    auto_gen_export_btn.grid(row=2, column=1,sticky="W")


    # GENERATE PASSWORD LAYOUT
    gen_title = tkinter.Label(gen_frame, text="Generate Password", underline=0)
    gen_pass = tkinter.Label(gen_frame, text="Password Length")
    gen_pass_entry = tkinter.Entry(gen_frame, text="", width=45)
    gen_pass_entry.insert("0", "10")
    gen_btn = tkinter.Button(gen_frame, text="Generate", height=1,underline=0)
    export_btn = tkinter.Button(gen_frame, text="Export", height=1,underline=0)
    exit_btn = tkinter.Button(gen_frame, text="Quit",height=1, underline=0, command=root.destroy)
    
    #grid
    gen_title.grid(row=0, column=0)
    gen_pass.grid(row=1, column=0)
    gen_pass_entry.grid(row=1, column=1, padx=5, pady=5, sticky="WE")
    gen_btn.grid(row=2, column=0, sticky="W")
    export_btn.grid(row=2, column=1, sticky="W")
    exit_btn.grid(row=3, column=0)











    root.mainloop()

# PROGRAM ENDS
main()
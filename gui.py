# GUI for password generator

# Credits
# =================================
# icons from www.iconarchive.com
# back link to https://icons8.com
# ================================


import tkinter, time, os, secrets
from tkinter import PhotoImage, BOTH, END, messagebox, filedialog


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
    root.geometry("520x420")
    #root.resizable(0,0)
    root.title("Password Generator")
    set_icon()


    # FUNCTIONS
    def generate_password():
        '''Generates Password'''
        conv_to_int = int(gen_pass_entry.get())
        conv_to_int = conv_to_int // 2
        print(conv_to_int)
        password_generator = secrets.token_hex(conv_to_int) # gen. the password
        text_box1.insert("1.0", password_generator + "\n")
        print(password_generator)
        #messagebox.showinfo("Success", "Password has been Generated!")
        

    def export_password():
        '''exports password to a txt file'''
        with open("password.txt", "w") as file:
            file.write(text_box1.get("1.0", "end"))
        messagebox.showinfo("Export", f"Exported!")
        #filedialog.asksaveasfilename(initialdir="./", title="Select File", filetypes=((".txt file", "*.txt"), ("all files", "*.*")))

    def clear():
        '''clears the text box'''
        text_box.delete("1.0", "end")
        text_box1.delete("1.0", "end")
        #messagebox.showinfo("Clear", "cleared!")

    def auto_gen_password():
        '''Auto Generates Password'''
        conv_to_int = int(auto_gen_entry_box.get())
        conv_to_int = conv_to_int // 2
        print(conv_to_int)
        password_generator = secrets.token_hex(conv_to_int)
        text_box.insert("1.0", password_generator + "\n")
        print(password_generator)

    def auto_export_password():
        '''exports password from auto generate textbox'''
        with open("auto_password.txt", "w") as file:
            file.write(text_box.get("1.0", "end"))
        messagebox.showinfo("Export", f"Exported!")

    # LAYOUTS
    auto_gen_frame = tkinter.LabelFrame(root, padx=5, pady=5)
    gen_frame = tkinter.LabelFrame(root, padx=5, pady=5)
    auto_gen_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)
    gen_frame.pack(fill=BOTH, expand=True, padx=5,pady=5)
    

    # AUTO GENERATE PASSWORD LAYOUT
    auto_title = tkinter.Label(auto_gen_frame, text="Auto Generate", underline=0)
    auto_gen_msg = tkinter.Label(auto_gen_frame, text="Password Length")
    auto_gen_entry_box = tkinter.Entry(auto_gen_frame, width=45)
    auto_generate_btn = tkinter.Button(auto_gen_frame, text="Generate", width=8, height=1, underline=0, command=auto_gen_password)
    auto_export_btn = tkinter.Button(auto_gen_frame, text="Export", width=8, height=1, underline=0, command=auto_export_password)
    text_box = tkinter.Text(auto_gen_frame, width=40, height=4, padx=5, pady=5)
    auto_clear_btn = tkinter.Button(gen_frame, text="Clear",height=1, underline=0, command=clear)

    # grid
    auto_title.grid(row=0, column=0, padx=5, pady=5)
    auto_gen_msg.grid(row=1, column=0, padx=5, pady=5)
    auto_gen_entry_box.grid(row=1, column=1, padx=5, pady=5)
    auto_generate_btn.grid(row=2, column=0, padx=5, pady=5)
    auto_export_btn.grid(row=2, column=1, padx=5, pady=5)
    text_box.grid(row=3, column=0, padx=5, pady=5)
    auto_clear_btn.grid(row=4, column=0, padx=5, pady=5)



    # GENERATE PASSWORD LAYOUT
    gen_title = tkinter.Label(gen_frame, text="Generate Password", underline=0, font=("arial bold",12))
    gen_pass = tkinter.Label(gen_frame, text="Password Length")
    gen_pass_entry = tkinter.Entry(gen_frame, text="", width=45)
    gen_pass_entry.insert("0", "10")
    generate_btn = tkinter.Button(gen_frame, text="Generate", height=1,underline=0, command=generate_password)
    export_btn = tkinter.Button(gen_frame, text="Export", height=1,underline=0, command=export_password)
    exit_btn = tkinter.Button(gen_frame, text="Quit",height=1, underline=0, command=root.destroy)
    text_box1 = tkinter.Text(gen_frame, width=40, height=4, padx=5, pady=5)
    clear_btn = tkinter.Button(gen_frame, text="Clear",height=1, underline=0, command=clear)

    #grid
    gen_title.place(relx=0.5, rely=1.0, anchor="s")
    #gen_title.grid(row=0, column=0)

    gen_pass.place(relx=0.0, rely=0.0)
    #gen_pass.grid(row=1, column=0)

    #gen_pass_entry.place(relx=0.0, rely=0.0)
    gen_pass_entry.grid(row=1, column=1, padx=5, pady=5)
    generate_btn.grid(row=2, column=0)
    export_btn.grid(row=2, column=1)
    exit_btn.grid(row=3, column=0)
    text_box1.grid(row=4)
    clear_btn.grid(row=5)


    root.mainloop()

# PROGRAM ENDS
main()
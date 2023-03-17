import random
import tkinter

class window:
    root = tkinter.Tk()
    root.geometry("400x300")
    root.configure(bg="black")
    root.title("Password generator")
    root.resizable(False, False)
    photo = tkinter.PhotoImage(file="lock.png")
    root.wm_iconphoto(False, photo)

class initial_values:

    letters_symbols = {"lowered_letters": "abcdefghijklmnopqrstuvwxyz", "uppered_letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                       "numbers": "1234567890", "symbols": "@#$%&+-?!/()[]"}

    password_symbols = letters_symbols["lowered_letters"] + letters_symbols["uppered_letters"] + letters_symbols["numbers"] + letters_symbols["symbols"]
    password_database = open("password_database.txt", "a")

    password_generator_list = []

class service_class:
    def __init__(self, root, password_generator_list):
        self.root = root
        self.password_generator_list = password_generator_list

    def service(self):

        def service_variable():
            service1 = service_entry.get()
            initial_values.password_generator_list.append(service1)

        #service
        service_label = tkinter.Label(self.root, text="For what service/webpage is this password for: ", fg="white", bg="black", font="Verdana").pack()
        service_entry = tkinter.Entry(self.root)
        service_entry.pack(pady=10)
        service_button = tkinter.Button(self.root, text="Enter", command=service_variable, height=1, font="Verdana").place(x=300, y=27)

class password_class:
    def __init__(self, root):
        self.root = root

    def password(self):

        def password_variable():
            try:
                password1 = int(password_entry.get())
            except ValueError:
                tkinter.Label(self.root, text="The password length must be a number", fg="white", bg="black", font="Verdana").pack()
            else:
                initial_values.password_generator_list.append(int(password1))

        #password
        password_label = tkinter.Label(self.root, text="Length of your password: ", fg="white", bg="black", font="Verdana").pack()
        password_entry = tkinter.Entry(self.root)
        password_entry.pack(pady=10)
        password_button = tkinter.Button(self.root, text="Enter", command=password_variable, height=1, font="Verdana").place(x=300, y=87)

class generator_class:

    def __init__(self, root, password_symbols, password_database):
        self.root = root
        self.password_symbols = password_symbols
        self.password_database = password_database

    def password_generator(self):

        def generate_function():

            password_generating = "".join(random.sample(initial_values.password_symbols, int(initial_values.password_generator_list[1])))
            generated_label = tkinter.Label(self.root, text=f"{initial_values.password_generator_list[0]} password: {password_generating}",
                                    fg="white", bg="black", font="Verdana")
            generated_label.pack()
            initial_values.password_database.write(f"{initial_values.password_generator_list[0]} password: {password_generating}\n")
            initial_values.password_generator_list = []

        #generator
        generate = tkinter.Button(self.root, text="Generate", command=generate_function, height=2, width=10, font="Verdana").pack(pady=20)

class new_window_class():

    def __init__(self, root):
        self.root = root

    def openNewWindow():
        newWindow = tkinter.Toplevel(window.root)
        newWindow.title("Passwords")
        newWindow.geometry("400x300")
        newWindow.configure(bg="black")
        photo = tkinter.PhotoImage(file="lock.png")
        newWindow.wm_iconphoto(False, photo)
        with open('password_database.txt') as f:
            for i in f:
                tkinter.Label(newWindow, text=f"{i}", fg="white", bg="black", font=("Verdana", 10),).pack(pady=0.5)

    newWindow_button = tkinter.Button(window.root, text="Saved passwords", command=openNewWindow, height=2, width=15, font=("Verdana",6)).place(x=310, y=270)

import tkinter as tk


class Load_frame1:

    def __init__(self,frame1, frame2):
        self.frame1 = frame1
        self.frame2 = frame2


    def clear_widgets(frame):
        for widget in frame.winfo_children():
            widget.destroy()


    def load_frame1():
        clear_widgets(frame2)
        frame1.tkraise()
        frame1.pack_propagate(False)

        logo_img = ImageTk.PhotoImage(file=logo_path)
        logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
        logo_widget.image = logo_img
        logo_widget.pack()

        tk.Label(frame1,
                 text="Whot would you do to do?",
                 bg=bg_color,
                 fg="white",
                 font=("TkMenuFont", 14)
                 ).pack(pady=20)

        tk.Button(
            frame1,
            text="zadej pojistence",
            font=("TkHeadingFont", 15),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: zadej_pojistence()
        ).pack(pady=10)

        tk.Button(
            frame1,
            text="vypis pojistence",
            font=("TkHeadingFont", 15),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: vypis()
        ).pack(pady=10)

        tk.Button(
            frame1,
            text="vyhledej pojistence",
            font=("TkHeadingFont", 15),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: vyhledej()
        ).pack(pady=10)

        tk.Button(
            frame1,
            text="vymazat pojistence",
            font=("TkHeadingFont", 15),
            bg="#28393a",
            fg="white",
            cursor="hand2",
            activebackground="#badee2",
            activeforeground="black",
            command=lambda: delete()
        ).pack(pady=10)
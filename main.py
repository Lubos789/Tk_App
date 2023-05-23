import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import sqlite3



#-----------------Settings-----------------------------------
bg_color = "#272838"
logo_path = "image/Bez názvu-1.png"
nadpis_color = "#EB9486"
nadpis_size = 20
button_bg = "#7E7F9A"
button_f = "#F9F8F8"
entry_text_color = "#F3DE8A"
white = "#F9F8F8"


def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

#-------------------Frame1 Home------------------------------

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)

    logo_img = ImageTk.PhotoImage(file=logo_path)
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_color)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
             text="Co si prejete udelat:",
             bg=bg_color,
             fg=white,
             font=("TkMenuFont", nadpis_size)
             ).pack(pady=20)

    tk.Button(
        frame1,
        text="Zadej pojistence",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: zadej_pojistence()
    ).pack(pady=10)

    tk.Button(
        frame1,
        text="Vypis pojistence",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: vypis()
    ).pack(pady=10)

    tk.Button(
        frame1,
        text="Vyhledej pojistence",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: vyhledej()
    ).pack(pady=10)

    tk.Button(
        frame1,
        text="Vymazat pojistence",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: delete()
    ).pack(pady=10)


#----------------Button Zadej pojistence----------------------------

def zadej_pojistence():
    frame2.tkraise()
    clear_widgets(frame1)

    tk.Label(frame2,
             text="Vymazat pojistence:",
             bg=bg_color,
             fg=white,
             font=("TkMenuFont", nadpis_size),
             pady=20,
             ).grid(column=0, columnspan=2, row=0)

    jmeno = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f, cursor="hand2")
    jmeno.grid(column=1,row=1, pady=3)
    jmeno.focus()
    tk.Label(frame2,text="Jmeno:",font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column=0,row=1)

    prijmeni = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f,cursor="hand2")
    prijmeni.grid(column=1, row=2, pady=(0,3))
    tk.Label(frame2, text="Prijmeni:",font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column=0,row=2)

    telefon = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f,cursor="hand2")
    telefon.grid(column=1, row=3, pady=(0,3))
    tk.Label(frame2,
             text="Telefon:", font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column=0, row=3)

    vek = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f,cursor="hand2")
    vek.grid(column=1, row=4,pady=(0,3))
    tk.Label(frame2,
             text="Vek:",font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column=0, row=4)

    tk.Button(
        frame2,
        text="Zpet do menu",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).grid(column=0, columnspan=2, row=6)

    tk.Button(
        frame2,
        text="Nahraj pojistence",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: novy_pojisteny()
    ).grid(pady=10, column=0, columnspan=2, row=5)

    def novy_pojisteny():
        jmeno_get = jmeno.get()
        prijmeni_get = prijmeni.get()
        telefon_get = telefon.get()
        vek_get = vek.get()

        connection = sqlite3.connect("Tk_pojistovna.db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO pojistenci (jmeno, prijmeni, telefon ,vek) "
                       f"VALUES ('{jmeno_get}', '{prijmeni_get}', '{telefon_get}', '{vek_get}')")
        connection.commit()
        connection.close()
        messagebox.showinfo(title="Confirm", message="Data byla ulozena")
        load_frame1()


#----------------Button Vypis pojistenych----------------------------

def vypis():
    frame2.tkraise()
    clear_widgets(frame1)

    tk.Label(frame2,
             text="Vypis pojistenych:",
             bg=bg_color,
             fg="#EB9486",
             font=("TkMenuFont", nadpis_size),
             pady=20
             ).grid(row=0, column=0, columnspan=4)
    tk.Label(frame2,text="Jmeno",bg=bg_color,fg="#F3DE8A",font=("TkMenuFont", 14), pady=10, padx=30).grid(column=0, row=1)
    tk.Label(frame2, text="Prijmeni", bg=bg_color, fg="#F3DE8A", font=("TkMenuFont", 14), pady=10, padx=30).grid(column=1, row=1)
    tk.Label(frame2, text="Telefon", bg=bg_color, fg="#F3DE8A", font=("TkMenuFont", 14), pady=10, padx=30).grid(column=2, row=1)
    tk.Label(frame2, text="Vek", bg=bg_color, fg="#F3DE8A", font=("TkMenuFont", 14), pady=10, padx=30).grid(column=3, row=1)
    connection = sqlite3.connect("Tk_pojistovna.db")
    cursor = connection.cursor()
    radek = 3
    for row in cursor.execute("select * from pojistenci"):
        jmeno, prijmeni, telefon, vek = row[1], row[2], row[3], row[4]

        tk.Label(frame2, text=jmeno, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=0, row=radek)
        tk.Label(frame2, text=prijmeni, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=1, row=radek)
        tk.Label(frame2, text=telefon, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=2, row=radek)
        tk.Label(frame2, text=vek, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=3, row=radek)
        radek += 1

    connection.close()

    tk.Button(
        frame2,
        text="Zpet do menu",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).grid(column=0, columnspan=4, pady=20)


#----------------Button Vyhledej pojistence----------------------------

def vyhledej():
    frame2.tkraise()
    clear_widgets(frame1)

    tk.Label(frame2,
             text="Vyhldedat v databazi:",
             bg=bg_color,
             fg=white,
             font=("TkMenuFont",nadpis_size),
             pady=20
             ).grid(column=0, columnspan=4, row=0)

    tk.Label(frame2,text="Jmeno:",font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column=1, row=1, sticky="e", padx=20)

    jmeno_vyhledej = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f, cursor="hand2")
    jmeno_vyhledej.grid(column=2, row=1, sticky="w",pady=3)
    jmeno_vyhledej.focus()

    tk.Label(frame2,text="Prijmeni:",font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column= 1, row=2, sticky="e", padx=20)

    prijmeni_vyhldej = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f, cursor="hand2")
    prijmeni_vyhldej.grid(column=2, row=2, sticky="w")



    tk.Button(
        frame2,
        text="Vyhledej",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: vypis_hledaneho()
    ).grid(column=0, columnspan=4, row=3, pady=(20,10), padx=30)

    tk.Button(
        frame2,
        text="Zpet do menu",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).grid(column=0, columnspan=4, row=4, padx=30, pady=(0, 30))

    def vypis_hledaneho():
        check = False
        jmeno = jmeno_vyhledej.get()
        prijmeni = prijmeni_vyhldej.get()
        connection = sqlite3.connect("Tk_pojistovna.db")
        cursor = connection.cursor()
        radek = 7
        for row in cursor.execute(
                f"select * from pojistenci where jmeno = '{jmeno}' and prijmeni = '{prijmeni}'"):
                jmeno_db, prijmeni_db, telefon_db, vek_db = row[1], row[2], row[3], row[4]
                if row[1] != None:
                    check = True
                    tk.Label(frame2, text="Jmeno", bg=bg_color, fg="white", font=("TkMenuFont", 14), padx=20).grid(column=0, row=5)
                    tk.Label(frame2, text="Prijmeni", bg=bg_color, fg="white", font=("TkMenuFont", 14), padx=20).grid(column=1, row=5)
                    tk.Label(frame2, text="Telefon", bg=bg_color, fg="white", font=("TkMenuFont", 14), padx=20).grid(column=2, row=5)
                    tk.Label(frame2, text="Vek", bg=bg_color, fg="white", font=("TkMenuFont", 14), padx=20).grid(column=3, row=5)
                    tk.Label(frame2, text=jmeno_db, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=0, row=radek)
                    tk.Label(frame2, text=prijmeni_db, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=1, row=radek)
                    tk.Label(frame2, text=telefon_db, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=2, row=radek)
                    tk.Label(frame2, text=vek_db, bg=bg_color, fg="white", font=("TkMenuFont", 14)).grid(column=3, row=radek)
                    radek += 1

        if check == False:
            messagebox.showwarning("Chyba!", "Zaznam v databazi nenalezen")

        connection.close()

#----------------Button Vymazat pojistence----------------------------

def delete():
    frame2.tkraise()
    clear_widgets(frame1)

    tk.Label(frame2,
             text="Zadejte osobu k vymazani:",
             bg=bg_color,
             fg=white,
             font=("TkMenuFont", nadpis_size),
             pady=20
             ).grid(column=0, columnspan=4, row=0)

    tk.Label(frame2,
             text="Jmeno:",font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column=1, row=1, sticky="e", padx=30)

    jmeno_vyhledej = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f, cursor="hand2")
    jmeno_vyhledej.grid(column=2, row=1, sticky="w",pady=3)
    jmeno_vyhledej.focus()

    tk.Label(frame2,
             text="Prijmeni:",font=("TkHeadingFont", 13), bg=bg_color, fg=white).grid(column= 1, row=2, sticky="e", padx=30)

    prijmeni_vyhldej = tk.Entry(frame2,font=("TkHeadingFont", 13), bg=button_bg, fg=button_f, cursor="hand2")
    prijmeni_vyhldej.grid(column=2, row=2, sticky="w")

    tk.Button(
        frame2,
        text="Vymazat!",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: delete_pojistence()
    ).grid(column=0, columnspan=4, row=3, pady=(20,10), padx=30)

    tk.Button(
        frame2,
        text="Zpet do menu",
        font=("TkHeadingFont", 15),
        bg=button_bg,
        fg=button_f,
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame1()
    ).grid(column=0, columnspan=4, row=6)

    def delete_pojistence():
        check = False
        jmeno = jmeno_vyhledej.get()
        prijmeni = prijmeni_vyhldej.get()
        connection = sqlite3.connect("Tk_pojistovna.db")
        cursor = connection.cursor()
        for row in cursor.execute(f"select * from pojistenci where jmeno = '{jmeno}' and prijmeni = '{prijmeni}'"):
            if row[1] == jmeno:
                check = True
                cursor.execute(f'DELETE FROM pojistenci WHERE uzivatele_id = "{row[0]}"')
                connection.commit()
                messagebox.showinfo("Info", "Zaznam byl upesne odstranen")
                load_frame1()
        if check == False:
            messagebox.showerror("Chyba", "Zaznam nenalezen")
        connection.close()


#------------------Start program------------------------------------------

root = tk.Tk()
root.title("Pojistovna App")
# root.eval("tk::PlaceWindow . top")
frame1 = tk.Frame(root, width=500, height=600, bg=bg_color)
frame2 = tk.Frame(root, width=500, height=600, bg=bg_color)

# frame1.grid(row=0, column=0)
# frame2.grid(row=0, column=0)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0) #sticky="nesw")

load_frame1()

root.mainloop()
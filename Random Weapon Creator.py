from tkinter import *
from PIL import ImageTk, Image
from random import randint
import random
import sqlite3
from tkinter import ttk
from pathlib import Path

path = Path(__file__).resolve().parent

HEIGHT = 500
WIDTH = 800

root = Tk()
root.title('Random Weapon Picker')
img = PhotoImage(file=str(path) + "\\" + 'JRLogo.png')
root.tk.call('wm', 'iconphoto', root._w, img)

i = 0
dis = StringVar()
exo = StringVar()
mas = StringVar()
mag = StringVar()

def distance(value):
    pass
def exotic(value):
    pass
def master(value):
    pass
def magic(value):    
    pass

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = Frame(root, bg='black', bd=5)
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)

aframe = Frame(root, bg='black', bd=5)
aframe.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)

# entry = tk.Entry(frame, font=40)
# entry.place(relwidth=0.65, relheight=1)

dislabel = Label(frame, bg='black', fg="#00ffff", text="Would you like a melee or ranged weapon?")
dislabel.pack(anchor=W)

discheck1 = Radiobutton(frame, text="Melee", variable=dis, bg='black', value="Melee", fg="#00ffff", selectcolor="black", command=lambda: distance(dis.get()))
discheck1.pack(anchor=W)

discheck2 = Radiobutton(frame, text="Ranged", variable=dis, bg='black', value="Ranged", fg="#00ffff", selectcolor="black", command=lambda: distance(dis.get()))
discheck2.pack(anchor=W)

exolabel = Label(frame, bg='black', fg="#00ffff", text="May I consider an exotic weapon?")
exolabel.pack(anchor=W, pady=2)

exocheck1 = Radiobutton(frame, text="Yes", variable=exo, value="Yes", bg='black', fg="#00ffff", selectcolor="black", command=lambda: exotic(exo.get()))
exocheck1.pack(anchor=W)

exocheck2 = Radiobutton(frame, text="No", variable=exo, value="No", bg='black', fg="#00ffff", selectcolor="black", command=lambda: exotic(exo.get()))
exocheck2.pack(anchor=W)

maslabel = Label(frame, bg='black', fg="#00ffff", text="Shall I pay for a Masterwork?")
maslabel.pack(anchor=W, pady=2)

mascheck1 = Radiobutton(frame, text="Yes", variable=mas, value="Yes", bg='black', fg="#00ffff", selectcolor="black", command=lambda: master(mas.get()))
mascheck1.pack(anchor=W)

mascheck2 = Radiobutton(frame, text="No", variable=mas, value="No", bg='black', fg="#00ffff", selectcolor="black", command=lambda: master(mas.get()))
mascheck2.pack(anchor=W)

maglabel = Label(frame, bg='black', fg="#00ffff", text="Shall I infuse it with Magic?")
maglabel.pack(anchor=W, pady=2)

magcheck1 = Radiobutton(frame, text="Yes", variable=mag, value="Yes", bg='black', fg="#00ffff", selectcolor="black", command=lambda: magic(mag.get()))
magcheck1.pack(anchor=W)

magcheck2 = Radiobutton(frame, text="No", variable=mag, value="No", bg='black', fg="#00ffff", selectcolor="black", command=lambda: magic(mag.get()))
magcheck2.pack(anchor=W)

def hide_all_frames():
    for widget in aframe.winfo_children():
        widget.destroy()

    aframe.pack_forget()

def roll_weapon():
    i = 0
#hides previous frames
    hide_all_frames()
#random choice for melee standard weapon
    if dis.get() == "Melee" and exo.get() == "No":
        melee_standard = ["Gauntlet (1d3)", "Dagger (1d4)",	"Punching Dagger (1d4)", "Spiked Gauntlet (1d4)", "Light Mace (1d6)", "Sickle (1d6)", "Club (1d6)",	"Heavy Mace (1d8)",	"Morningstar (1d8)", "Shortspear (1d6)", "Longspear (1d8)",	"Quarterstaff (1d6-1d6)",	"Spear (1d8)",	"Throwing Axe (1d6)",	"Light Hammer (1d4)",	"Handaxe (1d6)",	"Kukri (1d4)",	"Light Pick (1d4)",	"Sap (1d6)",	"Light Shield (1d3)",	"Spiked Armor (1d6)",	"Light Spiked Shield (1d4)",	"Short Sword (1d6)",	"Battleaxe (1d8)",	"Flail (1d8)",	"Longsword (1d8)",	"Heavy Pick (1d6)",	"Rapier (1d6)",	"Scimitar (1d6)",	"Heavy Shield (1d4)",	"Spiked Heavy Shield (1d6)",	"Trident (1d8)",	"Warhammer (1d8)",	"Falchion (2d4)",	"Glaive (2d10)",	"Greataxe (1d12)",	"Greatclub (1d10)",	"Heavy Flail (1d8)",	"Greatsword (2d6)",	"Guisarme (2d4)",	"Halberd (1d10)",	"Lance (1d8)",	"Ranseur (2d4)",	"Scythe (2d4)"]
        rmstan = randint(0, len(melee_standard)-1)
        wep = melee_standard[rmstan]
        mstancreate = str(path) + "\\" + wep + ".png"
        global mstan_img
        mstan_img = ImageTk.PhotoImage(Image.open(mstancreate))
        show_mstan = Label(aframe, image=mstan_img)
        show_mstan.pack()
#random choice for melee exotic weapon
    if dis.get() == "Melee" and exo.get() == "Yes":
        melee_exotic = ["Kama (1d6)",	"Nunchaku (1d6)",	"Sai (1d4)",	"Siangham (1d6)",	"Bastard Sword (1d10)",	"Dwarven Waraxe (1d10)",	"Whip (1d3)",	"Orc Double Axe (1d8-1d8)",	"Spiked Chain (2d4)",	"Dire Flail (1d8-1d8)",	"Gnome Hooked Hammer (1d8-1d6)",	"Two Bladed Sword (1d8-1d8)",	"Dwarven Urgosh (1d8-1d6)"]
        rmexo = randint(0, len(melee_exotic)-1)
        wep = melee_exotic[rmexo]
        mexocreate = str(path) + "\\" + wep + ".png"
        global mexo_img
        mexo_img = ImageTk.PhotoImage(Image.open(mexocreate))
        show_mexo = Label(aframe, image=mexo_img)
        show_mexo.pack()
#random choice for ranged standard weapon
    if dis.get() == "Ranged" and exo.get() == "No":
        ranged_standard = ["Heavy Crossbow (1d10)", "Light Crossbow (1d8)", "Dart (1d4)", "Javelin (1d6)", "Sling (1d4)", "Longbow (1d8)", "Composite Longbow (1d8)", "Shortbow (1d6)", "Composite Shortbow (1d6)"]
        rrstan = randint(0, len(ranged_standard)-1)
        wep = ranged_standard[rrstan]
        rstancreate = str(path) + "\\" + ranged_standard[rrstan] + ".png"
        global rstan_img
        rstan_img = ImageTk.PhotoImage(Image.open(rstancreate))
        show_rstan = Label(aframe, image=rstan_img)
        show_rstan.pack()
#random choice for ranged exotic weapon
    if dis.get() == "Ranged" and exo.get() == "Yes":
        ranged_exotic = ["Bolas (1d4)", "Hand Crossbow (1d4)", "Repeating Heavy Crossbow (1d10)", "Repeating Light Crossbow (1d8)", "Net (no damage)", "Shuriken (1d2)"]
        rrexo = randint(0, len(ranged_exotic)-1)
        wep = ranged_exotic[rrexo]
        rexocreate = str(path) + "\\" + ranged_exotic[rrexo] + ".png"
        global rexo_img
        rexo_img = ImageTk.PhotoImage(Image.open(rexocreate))
        show_rexo = Label(aframe, image=rexo_img)
        show_rexo.pack()
#masterwork
    if mas.get() == "Yes":
        i = 1
    if mas.get() == "No":
        i = 0
#random choice for enchantments
    if mag.get() == "Yes":
        enchantments = ["Anarchic",	"Axiomatic", "Bane", "Brilliant Energy",	"Dancing",	"Defending",	"Disruption",	"Distance",	"Flaming",	"Flaming Burst",	"Frost",	"Ghost Touch",	"Holy",	"Icy Burst",	"Keen",	"Ki Focus",	"Merciful",	"Mighty Cleaving",	"Returning",	"Seeking",	"Shock",	"Shocking Burst",	"Speed",	"Spell Storing",	"Thundering",	"Throwing",	"Unholy",	"Vicious",	"Vorpal",	"Wounding"]
        rmag = random.choice(enchantments)
    if mag.get() == "No":
        rmag = "no enchantments"

    finalwep = "Here is your weapon.  It is a " + wep + ", has a boost to hit of " + str(i) + ", and has " + rmag + " on it."

    final = Label(aframe, text=finalwep, wraplength=250, justify="center", bg="black", fg="#00ffff")
    final.pack(pady=15, expand="yes")

button = Button(frame, text="Roll Weapon", bg='gray', command=roll_weapon)
button.pack(pady=10, anchor=W)



#Create Database
def database():
    #create new window
    top = Toplevel(bg='black')
    top.title('Weapon Database')
    img = PhotoImage(file=str(path) + "\\" + 'JRLogo.png')
    top.tk.call('wm', 'iconphoto', top._w, img)

    conn = sqlite3.connect('weapon_list.db')
    c = conn.cursor()

    # def delete():
    #     searched_label.destroy()
    weaponout = Frame(top, bg="black")
    weaponout.place(relx=0.5, rely=0.3, relheight=0.65, relwidth=0.48)

    def hide_weaponout():
        for widget in weaponout.winfo_children():
            widget.destroy()

    def query():
        conn = sqlite3.connect('weapon_list.db')
        c = conn.cursor()
        #query the database
        c.execute("SELECT * FROM weapons")
        records = c.fetchall()

        print_records = ''
        for record in records:
            print_records += str(record[0]) + " have a damage of " +str(record[1]) + "\n"

        query_label = Label(top, text=print_records, bg="black", fg="#00ffff")
        query_label.grid(row=5, column=0, columnspan=2)

    def submit(event):
        
        conn = sqlite3.connect('weapon_list.db')
        c = conn.cursor()

        #Insert into table
        c.execute("INSERT INTO weapons VALUES (:weapon, :damage)",
            {
                'weapon': weapon.get(),
                'damage': damage.get()
            })

        conn.commit()
        conn.close()
        #clear text boxes
        weapon.delete(0, END)
        damage.delete(0, END)

    def searchname(event):
        hide_weaponout()
        conn = sqlite3.connect('weapon_list.db')
        c = conn.cursor()
        selected = drop.get()
        if selected == "Weapon":
            sql = "SELECT * FROM weapons WHERE weapon LIKE ? "
            searched = '%' + search_box.get().title() + '%'
        if selected == "Damage":
            sql = "SELECT * FROM weapons WHERE damage LIKE ? "
            searched = '%' + search_box.get() + '%'

        name = (searched, )
        c.execute(sql, name)
        result = c.fetchall()

        if not result:
            result = ("Record Not Found...")
            searched_label = Label(weaponout, text=result, bg="black", fg="#00ffff")
            searched_label.grid(row=2, column=4, columnspan=2, pady=10)
        else:
            for index, x in enumerate(result):
                num=4
                index +=2
                for y in x:
                    searched_label = Label(weaponout, text=y, bg="black", fg="#00ffff")
                    searched_label.grid(row=index, column=num)
                    num +=1

        # searched_label = Label(top, text=result, bg="black", fg="#00ffff")
        # searched_label.grid(row=1, column=5, columnspan=3, pady=10)

        
#create query button
    query_btn = Button(top, text="Show Weapons", command=query, bg='gray')
    query_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=127)


    # c.execute("""CREATE TABLE weapons (
    #     weapon text,
    #     damage text
    #     )""")

#create textboxes
    weapon = Entry(top, width=30)
    weapon.grid(row=0, column=1, padx=20)

    damage = Entry(top, width=30)
    damage.bind("<Return>", submit)
    damage.grid(row=1, column=1, padx=20)
#create textbox labels
    weapon_name = Label(top, text="Weapon", bg='black', fg="#00ffff")
    weapon_name.grid(row=0, column=0)

    damage_label = Label(top, text="Damage", bg='black', fg="#00ffff")
    damage_label.grid(row=1, column=0)
#create submit button
    submit_btn = Button(top, text="Add Weapon to Database", command=submit, bg='gray')
    submit_btn.bind("<Button-1>", submit)
    submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    conn.commit()
    conn.close()

    search_box = Entry(top)
    search_box.bind("<Return>", searchname)
    search_box.grid(row=0, column=7, padx=10, pady=10)

    # search_label = Label(top, text="Search:", bg="black", fg="#00ffff")
    # search_label.grid(row=0, column=5, columnspan=2, padx=5, pady=10)

    search_button = Button(top, text="Search", bg="gray", command=searchname)
    search_button.bind("<Button-1>", searchname)
    search_button.grid(row=0, column=8, padx=10, pady=10)

    drop = ttk.Combobox(top, value=["Weapon", "Damage"])
    drop.current(0)
    drop.grid(row=0, column=5, columnspan=2, padx=5, pady=10)

database_btn = Button(frame, text="Database", bg='gray', command=database)
database_btn.place(relx=0.35, rely=0.62)

root.mainloop()
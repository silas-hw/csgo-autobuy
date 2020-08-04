import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter import ttk
from tkinter.constants import ANCHOR, CENTER
import keyboard
from CLI import Bind

window = tk.Tk()
window.wm_geometry("500x500")
frame = tk.Frame(window, width=450, height=450)

frame1 = tk.Frame(frame, width=40)

def entry_key():
    key = keyboard.read_hotkey(suppress=False)
    keybind.key = key
    hotkey_display.config(text=key)

hotkey_record = tk.Button(frame1, text="record", width=8, command=entry_key)
hotkey_record.grid(row=1, column=0)

hotkey_display = tk.Label(frame1, bg="lightblue", width=20)
hotkey_display.grid(row=1, column=1)

keybind = Bind(hotkey_display.cget('text'))

def kb_generate():
    kb_display.config(state="normal")
    kb_display.delete(0, 'end')
    kb_display.insert(0, keybind.command)
    kb_display.config(state="readonly")

kb_display = tk.Entry(frame1, bg="pink", width=20)
kb_display.grid(row=0, column=1)
kb_btn = tk.Button(frame1, text="Generate", width=8, command=kb_generate).grid(row=0, column=0)

weapons_frame = tk.Frame(frame, width=400, height=200)

weapons = {
    "M4A4":"m4a1",
    "M4A1-S":"m4a1_silencer",
    "Ak47":"ak47",
    "Aug":"aug",
    "Awp":"awp",
    "Famas":"famas",
    "Gs3sg1":"gs3sg1",
    "Galil":"galilar",
    "Scar 20":"scar20",
    "SG-556":"sg556",
    "SSG":"ssg08",
    "PP-Bizon":"bizon",
    "Mac-10":"mac10",
    "MP7":"mp7",
    "MP9":"mp9",
    "MP5-sd":"mp5sd",
    "P90":"p90",
    "UMP-45":"ump45",
    "M249":"m249",
    "Mag7":"mag7",
    "Negev":"negev",
    "Nova":"nova",
    "Sawed-off":"sawedoff",
    "XM1014":"xm1014",
    "USP":"usp_silencer",
    "Desert eagle":"deagle",
    "Dual Barettas":"elite",
    "Fiveseven":"fiveseven",
    "Glock":"glock",
    "P2000":"hkp2000",
    "P250":"p250",
    "Tec-9":"tec9",
    "cz75-Auto":"cz75a",
    "R8 revolver":"revolver",
    "Flashbang":"flashbang",
    "Decoy":"weapon_decoy",
    "He grenade":"hegrenade",
    "Incgrenade":"incgrenade",
    "Molotov":"molotov",
    "Smoke":"smokegrenade",
    "Zeus":"taser",
    "Vest":"vest",
    "Vest and helmet":"vesthelm",
}

def add_weapon(combo):
    weapon_list.insert(1.0, f"{combo.get()}\n")
    keybind.addWeapon(weapons[combo.get()])

def clear_weapons():
    keybind.weapons = []
    weapon_list.delete(1.0, 'end')

weapon_select = tk.Frame(weapons_frame, width=200, height=200)

ar_label = tk.Label(weapon_select, text="Rifle")
ar_options = ttk.Combobox(weapon_select, values=["Famas", "M4A4", "M4A1-S", "Aug", "Galil", "Ak47", "SG-556", "Awp", "Gs3sg1", "Scar 20", "SSG"])
ar_add = tk.Button(weapon_select, text="+", command=lambda: add_weapon(ar_options))
ar_label.grid(row=0, column=0)
ar_options.grid(row=0, column=1)
ar_options.config(state='readonly')
ar_add.grid(row=0, column=2)

smg_label = tk.Label(weapon_select, text="SMG")
smg_options = ttk.Combobox(weapon_select, values=["PP-Bizon", "Mac-10", "MP7", "MP9", "MP5-sd", "UMP-45"])
smg_add = tk.Button(weapon_select, text="+", command=lambda: add_weapon(smg_options))
smg_label.grid(row=1, column=0)
smg_options.grid(row=1, column=1)
smg_options.config(state='readonly')
smg_add.grid(row=1, column=2)

heavy_label = tk.Label(weapon_select, text="Heavy")
heavy_options = ttk.Combobox(weapon_select, values=["M249", "Negev", "Mag7", "Sawed-off", "Nova", "XM1014"])
heavy_add = tk.Button(weapon_select, text="+", command=lambda: add_weapon(heavy_options))
heavy_label.grid(row=2, column=0)
heavy_options.grid(row=2, column=1)
heavy_options.config(state='readonly')
heavy_add.grid(row=2, column=2)

pistol_label = tk.Label(weapon_select, text="Pistol")
pistol_options = ttk.Combobox(weapon_select, values=["USP",  "P2000", "Glock", "P250", "Dual Barettas", "Fiveseven", "Tec-9", "cz75-Auto", "R8 revolver", "Desert eagle"])
pistol_add = tk.Button(weapon_select, text="+", command=lambda: add_weapon(pistol_options))
pistol_label.grid(row=3, column=0)
pistol_options.grid(row=3, column=1)
pistol_options.config(state='readonly')
pistol_add.grid(row=3, column=2)

util_label = tk.Label(weapon_select, text="Utilities")
util_options = ttk.Combobox(weapon_select, values=["Flashbang",  "Decoy", "He grenade", "Incgrenade", "Molotov", "Smoke", "Zeus", "Vest", "Vest and helmet"])
util_add = tk.Button(weapon_select, text="+", command=lambda: add_weapon(util_options))
util_label.grid(row=4, column=0)
util_options.grid(row=4, column=1)
util_options.config(state='readonly')
util_add.grid(row=4, column=2)

weapon_display = tk.Frame(weapons_frame, width=200, height=200)
weapon_list = tkst.ScrolledText(weapon_display, bg="pink", width=15, height=8)
weapon_list.grid(row=0, column=0)

clear = tk.Button(weapons_frame, text="Clear", command=clear_weapons)
clear.grid(row=1, column=1)

frame1.grid(row=0, column=0)
weapons_frame.grid(row=1, column=0)
weapon_select.grid(row=0, column=0)
weapon_display.grid(row=0, column=1)
frame.place(x=250, y=250, anchor=CENTER)
window.mainloop()
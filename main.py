from scraper import Scraper
from player import Player
from stats import Stats
from database import Database

import tkinter as tk


qb_list = Scraper("qb_list", [])
rb_list = Scraper("rb_list", [])
wr_list = Scraper("wr_list", [])

#qb_list.get_list("qb")
#rb_list.get_list("rb")
#wr_list.get_list("wr")

rb_list.content = Database.open_db()
for item in rb_list.content:
    item.dump_player()

Database.close_db(rb_list.content)

'''
i = 0
new_list = []
for player in rb_list.content:
    new_list.append(Player(player["name"], "blank", "rb", Stats.create_list()))
    i += 1
rb_list.content = new_list

for rb in rb_list.content:
    print(rb.name, rb.team, rb.position)
    rb.get_stats()

'''
'''
eelliot = Player("Ezekiel Elliott", "dal", "rb", Stats.create_list())
eelliot.get_stats()
'''

# I'm going to start working on a gui to run on setup down here
# Create instance fo window
win = tk.Tk()

# Add a title to the GUI
win.title("FFScraper")

frame = tk.Frame(win)
frame.pack()

tk.Label(frame, text="This is a message").pack()
tk.Button(frame, text="This is a button").pack()
win.resizable(False, False)

label2 = tk.Label(frame, text="label 2")
label2.pack()
label2.config(text = "new message")
label2.pack()

# Start the GUI and create main loop
win.mainloop()

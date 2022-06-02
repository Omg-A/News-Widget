from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("500x600")
root.overrideredirect(True)
bg_color = "light blue"
root.configure(background=bg_color)

label_title = Label(root, text="BBC News Update", font=("Helvetica", 18,'bold'), fg="royal blue", bg=bg_color)
label_title.place(relx=0.5, rely=0.05, anchor=CENTER)

#Title 1
news1 = Label(root, text="Title 1:", font=("Helvetica", 15,'bold'), wraplength=500, bg=bg_color)
news1.place(relx=0.5, rely=0.2, anchor=CENTER)

desc1 = Label(root, text="Description:", font=("Helvetica", 10,'bold'), wraplength=500, bg=bg_color)
desc1.place(relx=0.5, rely=0.3, anchor=CENTER)

#Title 2
news2 = Label(root, text="Title 2:", font=("Helvetica", 15,'bold'), wraplength=500, bg=bg_color)
news2.place(relx=0.5, rely=0.4, anchor=CENTER)

desc2 = Label(root, text="Description:", font=("Helvetica", 10,'bold'), wraplength=500, bg=bg_color)
desc2.place(relx=0.5, rely=0.5, anchor=CENTER)

#Title 3
news3 = Label(root, text="Title 3:", font=("Helvetica", 15,'bold'), wraplength=500, bg=bg_color)
news3.place(relx=0.5, rely=0.6, anchor=CENTER)

desc3 = Label(root, text="Description:", font=("Helvetica", 10,'bold'), wraplength=500, bg=bg_color)
desc3.place(relx=0.5, rely=0.7, anchor=CENTER)

#Title 4
news4 = Label(root, text="Title 4:", font=("Helvetica", 15,'bold'), wraplength=500, bg=bg_color)
news4.place(relx=0.5, rely=0.8, anchor=CENTER)

desc4 = Label(root, text="Description:", font=("Helvetica", 10,'bold'), wraplength=500, bg=bg_color)
desc4.place(relx=0.5, rely=0.9, anchor=CENTER)

#Working
api_request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=cb3775a2d72c47fb94b32336ebf01620")
open_bbc_page = json.loads(api_request.content)

title1 = open_bbc_page["articles"][0]["title"]
des1 = open_bbc_page["articles"][0]["description"]

title2 = open_bbc_page["articles"][1]["title"]
des2 = open_bbc_page["articles"][1]["description"]

title3 = open_bbc_page["articles"][2]["title"]
des3 = open_bbc_page["articles"][2]["description"]

title4 = open_bbc_page["articles"][3]["title"]
des4 = open_bbc_page["articles"][3]["description"]

news1["text"] = "Title 1: " + title1
desc1["text"] = "Description: " + des1

news2["text"] = "Title 2: " + title2
desc2["text"] = "Description: " + des2

news3["text"] = "Title 3: " + title3
desc3["text"] = "Description: " + des3

news4["text"] = "Title 4: " + title4
desc4["text"] = "Description: " + des4

root.mainloop()
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.geometry("1024x640")

window.title("第六組掃地機器人")

panelFrame = tk.Frame(window, width=window.winfo_width(), height =window.winfo_height())
panelFrame.place(x=0, y=0)
img = ImageTk.PhotoImage(Image.open("map.jpg"))

background = tk.Label(panelFrame, image =img)
background.pack(side="top", fill="both", expand="yes")

window.mainloop()
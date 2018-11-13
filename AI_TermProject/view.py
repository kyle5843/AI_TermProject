
import tkinter as tk


def make_label(master, x, y, *args, **kwargs):
    f = tk.Frame(master, height=50, width=50)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)
    lab = tk.Label(f, *args, **kwargs)
    lab.pack(fill=tk.BOTH, expand=1)
    return lab


def make_button(master, x, y, *args, **kwargs):
    f = tk.Frame(master, height=50, width=50)
    f.pack_propagate(0)  # don't shrink
    f.place(x=x, y=y)
    b = tk.Button(f, *args, **kwargs)
    b.pack(fill=tk.BOTH, expand=1)
    return b


def update(x, y, color):
    (globals()['X%s%s' % (x, y)]).configure(background=color)


def show_window(impassable_coordinate_list, path_log):
    for x in range(0, 10):
        for y in range(0, 10):
            globals()['X%s%s' % (x, y)] = make_label(rootWindow, x * 50, y * 50, text='', background='white',
                                                     borderwidth=1, relief="solid")

    for impassable in impassable_coordinate_list:
        update(impassable[0], impassable[1], "black")

    pre_step = path_log[0]
    for step in path_log:
        rootWindow.after(30, update(pre_step[0], pre_step[1], "cyan4"))
        pre_step = step
        rootWindow.after(30, update(step[0], step[1], "chartreuse1"))
        rootWindow.update()

    rootWindow.mainloop()


rootWindow = tk.Tk()
rootWindow.geometry("500x500")
rootWindow.title("尋路測試")

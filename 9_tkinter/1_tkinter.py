from tkinter import *
from tkinter.ttk import *
from threading import Thread


count = 0


def clicked():
    global count
    click_count.configure(text=count)
    count += 1


def get_main_window():
    window = Tk()
    window.title('Просто окно программы')
    window.geometry('400x800')
    window.resizable(False, False)
    return window


w = get_main_window()

click_count = Label(w, text=count, font='Arial 35')
click_count.pack()
btn = Button(w, text='Кликай тут', command=clicked)
click_count.configure(text=count)
btn.pack()

Entry().pack(padx=8, pady= 40)

enabled = IntVar()


enabled_checkbutton = Checkbutton(text="Включить", variable=enabled)
enabled_checkbutton.pack(padx=6, pady=6, anchor=NW)


enabled_label = Label(textvariable=enabled)
enabled_label.pack(padx=6, pady=6, anchor=NW)


radio_variable = StringVar()
radio_btn_1 = Radiobutton(text="Текст 1", value = '1', variable=radio_variable)
radio_btn_2 = Radiobutton(text="Текст 2", value = '2', variable=radio_variable)
position = {"padx":6, "pady":6, "anchor":NW}
radio_btn_1.pack(**position)
radio_btn_2.pack(**position)


values = ["Var 1", "Var 2", "Var 3", "Var 4"]
vars = Variable(value=values)
listbox = Listbox(listvariable=vars)
listbox.pack(anchor=NW, fill=X, padx=5, pady=5)


value_var = IntVar(value=0)
def start(): progressbar.start(1000)
progressbar =  Progressbar(orient="horizontal", variable=value_var)
progressbar.pack(fill=X, padx=6, pady=6)
start_btn = Button(text="Старт", command=start)
start_btn.pack(anchor=NE, padx=6, pady=6)


w.mainloop()

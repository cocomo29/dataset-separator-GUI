from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog
import pandas as pd

def new(user):
    try:
        global newdf
        data = pd.read_excel(filename)
        newdf = data.loc[data.Month == user]  #Month is the separator
        #if new file is empty, it means your input wasnt present in the file
        newdf.to_excel(f'{filename}({user}).xlsx', index=True) 
        canvas.create_text(
    312,
    350,
    anchor="nw",
    text="File Generated!",
    fill="#32CD32",
    font=("Roboto Bold", 14 * -1))
    except:
        canvas.create_text(
    315,
    350,
    anchor="nw",
    text="Invalid Input",
    fill="#ff0000",
    font=("Roboto Bold", 14 * -1))

def dowork():
    starting_month = entry3.get()
    ending_month = entry4.get()
    user = starting_month.title() + "-" + ending_month.title()
    new(user)

window = Tk()
window.title("Enerrgy Call Center")
window.geometry("713x423")
window.configure(bg = "#FFFFFF")

lineImage = PhotoImage(
    file=("assets/line.png"))
logo_image = PhotoImage(
    file=("assets/logo.png"))
blueImage = PhotoImage(
    file=("assets/blue.png"))
exitImage = PhotoImage(
    file=("assets/exit.png"))
generateImage = PhotoImage(
    file=("assets/generate.png"))

canvas = Canvas(
    window,
bg = "#FFFFFF",
height = 423,
width = 713,
bd = 0,
highlightthickness = 0,
relief = "ridge")

logo = Button(
image=logo_image,
background="#FFFFFF",
borderwidth=0,
highlightthickness=0,
relief="flat")
logo.place(
x=9,
y=11,
width=98,
height=83)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
0.0,
0.0,
713.0,
423.0,
fill="#FFFFFF",)

exit = Button(
image=exitImage,
borderwidth=0,
highlightthickness=0,
relief="flat")
exit.place(
x=558,
y=369.0,
width=134,
height=40.0)
exit.bind("<Button-1>", lambda event: window.destroy())

generate = Button(
image=generateImage,
borderwidth=0,
highlightthickness=0,
command= dowork,
relief="flat")
generate.place(
x=291,
y=294.0,
width=133,
height=40.0)

blue = Button(
image=blueImage,
borderwidth=0,
highlightthickness=0,
relief="flat")
blue.place(
x=357.0,
y=151.0,
width=95.0,
height=25.2)
entry3 = Entry(
bd=0,
bg="#07AAF8",
fg="#000716",
highlightthickness=0,
font=("Bahnschrift SemiLight", 13 * -1))
entry3.bind("<Return>", lambda event: print(entry3.get()))
entry3.place(
x=363,
y=155,
width=82,
height=15)

blue = Button(
image=blueImage,
borderwidth=0,
highlightthickness=0,
relief="flat")
blue.place(
x=357.0,
y=193.0,
width=95.0,
height=25.2)
entry4 = Entry(
bd=0,
bg="#07AAF8",
fg="#000716",
highlightthickness=0,
font=("Bahnschrift SemiLight", 13 * -1))
entry3.bind("<Return>", lambda event: print(entry4.get()))
entry4.place(
x=363,
y=197,
width=82,
height=15)

blue = Button(
image=blueImage,
borderwidth=0,
highlightthickness=0,
relief="flat")
blue.place(
x=357.0,
y=235.0,
width=95.0,
height=25.2)

def browse():
    global filename
    try:
        filename = filedialog.askopenfilename(initialdir="Desktop", title="Select A File", filetypes=(("XLSX Files", "*.xlsx"), ("All Files", "*.*")))
    except:
        filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("XLSX Files", "*.xlsx"), ("All Files", "*.*")))

blue.bind("<Button-1>", lambda event: browse())

canvas.create_text(
266.0,
90.0,
anchor="nw",
text="CHOOSE MONTH",
fill="#000000",
font=("Roboto Extra Bold", 24 * -1))
canvas.create_text(
266.0,
154.0,
anchor="nw",
text="Starting",
fill="#060606",
font=("Roboto Bold", 17 * -1))
canvas.create_text(
266.0,
193.0,
anchor="nw",
text="Ending",
fill="#000000",
font=("Roboto Bold", 17 * -1))
canvas.create_text(
266.0,
238.0,
anchor="nw",
text="File",
fill="#000000",
font=("Roboto Bold", 17 * -1))

line = Button(
image=lineImage,
borderwidth=30,
border=30,
# bordercolor="#07AAF8",
highlightthickness=30,
relief="flat")
line.place(
x=266.0,
y=86.6,
width=197.0,
height=2)
line = Button(
image=lineImage,
borderwidth=30,
border=30,
highlightthickness=30,
relief="flat")
line.place(
x=266.0,
y=116.0,
width=197.0,
height=2)

canvas.create_rectangle(
9.0,
11.0,
107.0,
94.0,
fill="#FFFFFF",
outline="")

window.resizable(False, False)
window.mainloop()
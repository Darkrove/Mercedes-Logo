from tkinter import *
root = Tk()
canvas=Canvas(root,bg='black')
canvas.create_oval(20,20,200,200,outline='yellow')
canvas.create_oval(12,12,208,208,outline='yellow')

canvas.create_line(105,20,85,110,fill='yellow')
canvas.create_line(105,20,105,115,fill='yellow')
canvas.create_line(105,20,125,110,fill='yellow')

canvas.create_line(40,170,85,110,fill='yellow')
canvas.create_line(40,170,105,115,fill='yellow')
canvas.create_line(40,170,105,130,fill='yellow')

canvas.create_line(175,170,125,110,fill='yellow')
canvas.create_line(175,170,105,115,fill='yellow')
canvas.create_line(175,170,105,130,fill='yellow')

canvas.create_line(85,110,105,115,fill='yellow')
canvas.create_line(105,130,105,115,fill='yellow')
canvas.create_line(125,110,105,115,fill='yellow')

canvas.create_text(150,230,text='Mercedes-Benz',font=('Arial Black',25),fill='yellow')
canvas.pack()
root.mainloop()
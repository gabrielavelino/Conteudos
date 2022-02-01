from tkinter import *

 
def on_move(event):
    component=event.widget
    locx, locy = component.winfo_x(), component.winfo_y()
    w , h = master.winfo_width(),master.winfo_height()
    mx ,my = component.winfo_width(),component.winfo_height()
    xpos=(locx+event.x)-(15)
    ypos=(locy+event.y)-int(my/2)
    if xpos>=0 and ypos>=0 and w-abs(xpos)>=0 and h-abs(ypos)>=0 and xpos<=w-5 and ypos<=h-5:
       component.place(x=xpos,y=ypos)

 

master = Tk()
master.geometry('1250x720')

imageLogo = PhotoImage(file= "bblack.png")
background = Label(image=imageLogo)

#msg = Label(master, text = "Rei")
#msg.config(bg='lightgreen', font=('times', 24, 'italic'))
background.bind('<B1-Motion>',on_move)
background.place(x=10,y=20)
mainloop()
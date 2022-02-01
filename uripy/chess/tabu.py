from tkinter import *
from PIL import Image
def game():  
    root = Tk()
    root.title('TutorChess')
    root.geometry('800x600')
    root.config(background = 'black')
    root.resizable(width = False, height = False)
    root.iconbitmap('icon.ico')

    frame = Frame(root)
    frame.pack()
    canvas = Canvas(frame,bg='black',width=800,height=600)
    canvas.pack()
   
    #TABULEIRO XADREZ
    imagemTabuleiro = PhotoImage(file = "board.png")
    canvas.create_image(400,300,image=imagemTabuleiro)
    
    #MOVIMENTOS DAS PEÇAS
    def on_move(event):
        component=event.widget
        locx, locy = component.winfo_x(), component.winfo_y()
        w , h = canvas.winfo_width(),canvas.winfo_height()
        mx ,my = component.winfo_width(),component.winfo_height()
        xpos=(locx+event.x)-(15)
        ypos=(locy+event.y)-int(my/2)
        if xpos>=0 and ypos>=0 and w-abs(xpos)>=0 and h-abs(ypos)>=0 and xpos<=w-5 and ypos<=h-5:
            component.place(x=xpos,y=ypos)
    
    #IMAGENS DAS PEÇAS    
    imgCavalo = PhotoImage(file= "bblack.png")
    #cavalo = Label(canvas,image=imgCavalo)
    #cavalo.place(x=10,y=10)
    cavalo = canvas.create_image(250,30,image=imgCavalo)
    canvas.bind('<B1-Motion>',on_move)

    root.mainloop()

game()
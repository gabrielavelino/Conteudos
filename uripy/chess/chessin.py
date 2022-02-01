from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title('TutorChess')
root.geometry('800x600')
root.config(background = 'black')
root.resizable(width = False, height = False)
root.iconbitmap('icon.ico')



# Imagem de fundo
imageLogo = PhotoImage(file= "chessbackground.png")
background = Label(image=imageLogo)
background.place(x=0,y=0, relwidth=1,relheight=1)


# Chamar o jogo
def game():  
    board = Toplevel()
    board.title('TutorChess')
    board.geometry('800x600')
    board.resizable(width = False, height = False)
    board.iconbitmap('icon.ico')
    
    #TABULEIRO XADREZ
    imagemTabuleiro = PhotoImage(file = "board.png")
    Tabuleiro = Label(board, image=imagemTabuleiro)
    Tabuleiro.place(x=0,y=0,relwidth=1,relheight=1)
    
    #FUNÇAO MOVIMENTO DA PEÇA
    def on_move(event):
        component=event.widget
        locx, locy = component.winfo_x(), component.winfo_y()
        w , h =board.winfo_width(),board.winfo_height()
        mx ,my =component.winfo_width(),component.winfo_height()
        xpos=(locx+event.x)-(15)
        ypos=(locy+event.y)-int(my/2)
        if xpos>=0 and ypos>=0 and w-abs(xpos)>=0 and h-abs(ypos)>=0 and xpos<=w-5 and ypos<=h-5:
            component.place(x=xpos,y=ypos)
    
    
 
   #IMAGENS DAS PEÇAS PRETAS
    imgBCavalo = PhotoImage(file= "nblack.png")
    bcavalo = Label(board,image=imgBCavalo)
    bcavalo.bind('<B1-Motion>',on_move)
    bcavalo.place(x=110,y=5)
    
    imgBTorre = PhotoImage(file= "rblack.png")
    btorre = Label(board,image=imgBTorre)
    btorre.bind('<B1-Motion>',on_move)
    btorre.place(x=20,y=5)

    imgBBispo = PhotoImage(file= "bblack.png")
    bbispo = Label(board,image=imgBBispo)
    bbispo.bind('<B1-Motion>',on_move)
    bbispo.place(x=215,y=5)

    imgRainha = PhotoImage(file= "qblack.png")
    rainha = Label(board,image=imgRainha)
    rainha.bind('<B1-Motion>',on_move)
    rainha.place(x=315,y=5)

    imgRei = PhotoImage(file= "kblack.png")
    rei = Label(board,image=imgRei)
    rei.bind('<B1-Motion>',on_move)
    rei.place(x=415,y=5)

    imgBBispo2 = PhotoImage(file= "bblack.png")
    bbispo2 = Label(board,image=imgBBispo2)
    bbispo2.bind('<B1-Motion>',on_move)
    bbispo2.place(x=515,y=5)

    imgBCavalo2 = PhotoImage(file= "nblack.png")
    bcavalo2 = Label(board,image=imgBCavalo2)
    bcavalo2.bind('<B1-Motion>',on_move)
    bcavalo2.place(x=615,y=5)

    imgBTorre2 = PhotoImage(file= "rblack.png")
    btorre2 = Label(board,image=imgBTorre2)
    btorre2.bind('<B1-Motion>',on_move)
    btorre2.place(x=715,y=5)

    imgBPeao1 = PhotoImage(file= "pblack.png")
    bpeao1 = Label(board,image=imgBPeao1)
    bpeao1.bind('<B1-Motion>',on_move)
    bpeao1.place(x=20,y=80)

    imgBPeao2 = PhotoImage(file= "pblack.png")
    bpeao2 = Label(board,image=imgBPeao2)
    bpeao2.bind('<B1-Motion>',on_move)
    bpeao2.place(x=110,y=80)

    imgBPeao3 = PhotoImage(file= "pblack.png")
    bpeao3 = Label(board,image=imgBPeao3)
    bpeao3.bind('<B1-Motion>',on_move)
    bpeao3.place(x=215,y=80)

    imgBPeao4 = PhotoImage(file= "pblack.png")
    bpeao4 = Label(board,image=imgBPeao4)
    bpeao4.bind('<B1-Motion>',on_move)
    bpeao4.place(x=315,y=80)

    imgBPeao5 = PhotoImage(file= "pblack.png")
    bpeao5 = Label(board,image=imgBPeao5)
    bpeao5.bind('<B1-Motion>',on_move)
    bpeao5.place(x=415,y=80)

    imgBPeao6 = PhotoImage(file= "pblack.png")
    bpeao6 = Label(board,image=imgBPeao6)
    bpeao6.bind('<B1-Motion>',on_move)
    bpeao6.place(x=515,y=80)

    imgBPeao7 = PhotoImage(file= "pblack.png")
    bpeao7 = Label(board,image=imgBPeao7)
    bpeao7.bind('<B1-Motion>',on_move)
    bpeao7.place(x=615,y=80)

    imgBPeao8 = PhotoImage(file= "pblack.png")
    bpeao8 = Label(board,image=imgBPeao8)
    bpeao8.bind('<B1-Motion>',on_move)
    bpeao8.place(x=715,y=80)


   #IMAGENS DAS PEÇAS BRANCAS
    imgWTorre = PhotoImage(file= "rblack.png")
    wtorre = Label(board,image=imgWTorre)
    wtorre.bind('<B1-Motion>',on_move)
    wtorre.place(x=20,y=530)

    imgWTorre2 = PhotoImage(file= "rblack.png")
    wtorre2 = Label(board,image=imgWTorre2)
    wtorre2.bind('<B1-Motion>',on_move)
    wtorre2.place(x=715,y=530)



   
    board.mainloop()

   
   

# Butões do Menu
butaoNew = Button(root, text='New Game Player x CPU',padx=65,pady=5,fg='snow',bg='black',command = game)
butaoNew.place(relx=0.5,rely=0.4,anchor=CENTER)
butaoPvP = Button(root,text='New Game Player x Player',padx=60,pady=5,fg='snow',bg='black',command = game)
butaoPvP.place(relx=0.5,rely=0.5,anchor=CENTER)
butaoExit = Button(root,text='SAIR',padx=117,pady=5,fg='snow',bg='black',command=root.quit)
butaoExit.place(relx=0.5,rely=0.8,anchor=CENTER)



root.mainloop()
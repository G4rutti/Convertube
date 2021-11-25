from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import youtube_dl

class Convertube():
    cor_fundo = '#E61B00'
    cor_botao = '#660C00'

    def __init__(self):
        self.root = root 
        self.configura_tela()
        self.widgets()

        root.mainloop()

    def configura_tela(self):
        self.root.iconbitmap('Convertube/youtube-logo-5-2.ico.ico')
        self.root.geometry('450x200')
        self.root.title('Convertube')
        self.root.resizable(False,False)
        self.root.configure(bg=self.cor_fundo)

    def widgets(self):
        frame1 = Frame(root, width=450, height=50, bg='#B31500')
        frame1.pack()

        txt1 = Label(root, text='Convertube',fg='white',bg='#B31500', font='Arial 18 bold')
        txt1.place(x=18,y=8)

        txt2 = Label(root, text='Link:',fg='white',bg=self.cor_fundo, font='Arial 12 bold')
        txt2.place(x=30, y=60)

        self.entry1 = Entry(root, bg='white', fg='black', font='Arial 10 bold', border=0)
        self.entry1.place(x=34,y=87,width=225,height=20)

        self.cbox = ttk.Combobox(root, values=['.mp3','.mp4'])
        self.cbox.place(x=320,y=87, width=90, height=23)

        btn1 = Button(root, text='Baixar', bg=self.cor_botao, fg='white', font='Arial 10 bold',command=self.function ,border=0)
        btn1.place(x=30,y=148, width=104, height=29)

    def function(self):
        url = self.entry1.get()
        formato = self.cbox.get()

        try:
            if formato == '.mp4':
                with youtube_dl.YoutubeDL({'format':'best'}) as ydl:
                    ydl.download([url])
        except:
            messagebox.showinfo(title='Algo deu errado!', message='Algo seu errado e não conseguimos completar a tarefa.')

        try:
            if formato == '.mp3':
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                }
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
        except:
            messagebox.showinfo(title='Algo deu errado!', message='Algo seu errado e não conseguimos completar a tarefa.')



root = Tk()
Convertube()
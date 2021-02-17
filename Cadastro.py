from tkinter import *
from platform import *

class Front_End():
    
    def __init__(self):
        
        self.janelaCadastro = Tk()
        self.janelaCadastro.geometry('500x500')
        self.janelaCadastro.title('Cadastro')
        
        self.sistemaOperacional = system()
        
        if self.sistemaOperacional == 'Windows':
            self.janelaCadastro.state('zoomed')
        else:
            self.janelaCadastro.attributes('-zoomed', True)
        
        self.lbNome = Label(self.janelaCadastro, text='Nome')
        self.lbCPF = Label(self.janelaCadastro, text='CPF')
        self.lbSenha = Label(self.janelaCadastro, text='Senha')
        self.lbConfirmaSenha = Label(self.janelaCadastro, text='Confirme Senha')

        self.janelaCadastro.mainloop()

instancia = Front_End()
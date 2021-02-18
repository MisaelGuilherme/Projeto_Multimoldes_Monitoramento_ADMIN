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
        
        self.frameDadosLogin = Frame(self.janelaCadastro, highlightbackground='black', highlightthickness=2)
        self.frameDadosLogin.place(relx=0.100, rely=0.200, relwidth=0.800, relheight=0.250)
        
        self.lbDados = Label(self.frameDadosLogin, text='Dados', font=('impact', 12))
        self.lbDados.place(relx=0.010, rely=0.010)
        
        self.lbNome = Label(self.frameDadosLogin, text='Nome', font=('impact',13))
        self.lbCPF = Label(self.frameDadosLogin, text='CPF', font=('impact',13))
        self.lbSenha = Label(self.frameDadosLogin, text='Senha', font=('impact',13))
        self.lbConfirmaSenha = Label(self.frameDadosLogin, text='Confirme Senha', font=('impact',13))
        
        self.lbNome.place(relx=0.020, rely=0.300)
        self.lbCPF.place(relx=0.380, rely=0.300)
        self.lbSenha.place(relx=0.020, rely=0.600)
        self.lbConfirmaSenha.place(relx=0.270, rely=0.600)
        

        self.campoNome = Entry(self.frameDadosLogin, font=('arial',13))
        self.campoCPF = Entry(self.frameDadosLogin, font=('arial',13))
        self.campoSenha = Entry(self.frameDadosLogin, font=('arial',13))
        self.campoConfirmaSenha = Entry(self.frameDadosLogin, font=('arial',13))
        
        self.campoNome.place(relx=0.080, rely=0.300, relwidth=0.280)
        self.campoCPF.place(relx=0.425, rely=0.300, relwidth=0.175)
        self.campoSenha.place(relx=0.085, rely=0.600, relwidth=0.175)
        self.campoConfirmaSenha.place(relx=0.410, rely=0.600, relwidth=0.175)

        self.janelaCadastro.mainloop()

instancia = Front_End()
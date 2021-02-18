from tkinter import *
from tkinter import ttk
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
        
        self.frameDadosLogin = Frame(self.janelaCadastro, highlightbackground='grey', highlightthickness=2)
        self.frameDadosLogin.place(relx=0.100, rely=0.200, relwidth=0.800, relheight=0.250)
        
        self.lbDados = Label(self.frameDadosLogin, text='Dados', font=('impact', 14))
        self.lbDados.place(relx=0.010, rely=0.010)
        
        self.lbNome = Label(self.frameDadosLogin, text='Nome', font=('impact',12))
        self.lbCPF = Label(self.frameDadosLogin, text='CPF', font=('impact',12))
        self.lbSenha = Label(self.frameDadosLogin, text='Senha', font=('impact',12))
        self.lbConfirmaSenha = Label(self.frameDadosLogin, text='Confirme Senha', font=('impact',12))
        
        self.lbNome.place(relx=0.020, rely=0.300)
        self.lbCPF.place(relx=0.380, rely=0.300)
        self.lbSenha.place(relx=0.020, rely=0.600)
        self.lbConfirmaSenha.place(relx=0.270, rely=0.600)
        

        self.campoNome = Entry(self.frameDadosLogin, font=('arial',12))
        self.campoCPF = Entry(self.frameDadosLogin, font=('arial',12))
        self.campoSenha = Entry(self.frameDadosLogin, font=('arial',12))
        self.campoConfirmaSenha = Entry(self.frameDadosLogin, font=('arial',12))
        
        self.campoNome.place(relx=0.080, rely=0.300, relwidth=0.280)
        self.campoCPF.place(relx=0.425, rely=0.300, relwidth=0.175)
        self.campoSenha.place(relx=0.085, rely=0.600, relwidth=0.175)
        self.campoConfirmaSenha.place(relx=0.410, rely=0.600, relwidth=0.175)
        
        self.frameAtribuicao = Frame(self.janelaCadastro, highlightbackground='grey', highlightthickness=2)
        self.frameAtribuicao.place(relx=0.100, rely=0.460, relwidth=0.800, relheight=0.250)
        
        self.lbAtribuicao = Label(self.frameAtribuicao, text='Atribuição', font=('impact', 14))
        self.lbAtribuicao.place(relx=0.010, rely=0.010)
        
        self.lbSerramento = Label(self.frameAtribuicao, text='Serramento', font=('impact', 11))
        self.lbAplainamento = Label(self.frameAtribuicao, text='Aplainamento', font=('impact', 11))
        self.lbTorneamento = Label(self.frameAtribuicao, text='Torneamento', font=('impact', 11))
        self.lbFresagem = Label(self.frameAtribuicao, text='Fresagem', font=('impact', 11))
        self.lbFurar = Label(self.frameAtribuicao, text='Furar', font=('impact', 11))
        self.lbBrochamento = Label(self.frameAtribuicao, text='Brochamento', font=('impact', 11))
        self.lbEletroerosao = Label(self.frameAtribuicao, text='Eletroerosao', font=('impact', 11))
        
        self.lbSerramento.place(relx=0.020, rely=0.400)
        self.lbAplainamento.place(relx=0.15, rely=0.400)
        self.lbTorneamento.place(relx=0.28, rely=0.400)
        self.lbFresagem.place(relx=0.41, rely=0.400)
        self.lbFurar.place(relx=0.54, rely=0.400)
        self.lbBrochamento.place(relx=0.67, rely=0.400)
        self.lbEletroerosao.place(relx=0.80, rely=0.400)

        self.lbbox1 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.lbbox1['values'] = ('Select', '0', '1', '2', '3')
        self.lbbox1.current(0)
        
        self.lbbox2 = ttk.Combobox(self.frameAtribuicao, font=('arial', 13), state="readonly")
        self.lbbox2['values'] = ('Select', '0', '1', '2', '3')
        self.lbbox2.current(0)

        self.lbbox3 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.lbbox3['values'] = ('Select', '0', '1', '2', '3')
        self.lbbox3.current(0)
    
        self.lbbox4 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.lbbox4['values'] = ('Select', '0', '1', '2', '3')
        self.lbbox4.current(0)
        
        self.lbbox5 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.lbbox5['values'] = ('Select', '0', '1', '2', '3')
        self.lbbox5.current(0)
        
        self.lbbox6 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.lbbox6['values'] = ('Select', '0', '1', '2', '3')
        self.lbbox6.current(0)
        
        self.lbbox7 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.lbbox7['values'] = ('Select', '0', '1', '2', '3')
        self.lbbox7.current(0)        
                        
        self.lbbox1.place(relx=0.020, rely=0.600, relwidth=0.11)
        self.lbbox2.place(relx=0.15, rely=0.600, relwidth=0.11)
        self.lbbox3.place(relx=0.28, rely=0.600, relwidth=0.11)
        self.lbbox4.place(relx=0.41, rely=0.600, relwidth=0.11)
        self.lbbox5.place(relx=0.54, rely=0.600, relwidth=0.11)
        self.lbbox6.place(relx=0.67, rely=0.600, relwidth=0.11)
        self.lbbox7.place(relx=0.80, rely=0.600, relwidth=0.11)

        self.janelaCadastro.mainloop()

instancia = Front_End()
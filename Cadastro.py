from tkinter import *
from tkinter import ttk
from platform import *
from tkinter import messagebox
import mysql.connector
import threading

class Back_End():
    
    def connection_database(self):

        self.bancoServer = mysql.connector.connect(
                                                    host='10.0.0.65',
                                                    database='empresa_funcionarios',
                                                    user='MultimoldesClient',
                                                    password='')
        self.cursor = self.bancoServer.cursor()
    
    def encerrando_conexao_database(self):
        
        self.bancoServer.close()
        self.cursor.close()
    
    def inserindo_dados_cadastro(self):
        
        #Atribuição dos campos cadastrais nas variáveis
        
        a = self.campoNome.get().upper()
        b = self.campoCPF.get()
        c = self.campoConfirmaSenha.get()
        
        #Atribuição dos valores dos boxes de seleção nas variáves
        
        A = self.box1.get()
        B = self.box2.get()
        C = self.box3.get()
        D = self.box4.get()
        E = self.box5.get()
        F = self.box6.get()
        G = self.box7.get()
        
        #Inserrindo dados no Banco de Dados Servidor
        
        self.cursor.execute("INSERT INTO funcionarios VALUES (ID, '"+a+"','"+b+"','"+c+"')")
        self.bancoServer.commit()
        
        self.cursor.execute("INSERT INTO habilidade_funcionarios VALUES ('"+a+"','"+b+"','"+A+"','"+B+"','"+C+"','"+D+"','"+E+"','"+F+"','"+G+"')")
        self.bancoServer.commit()
        
        if messagebox.showinfo('Alerta', 'Usuário cadastrado com sucesso!'):
        
            self.campoNome.delete(0, END)
            self.campoCPF.delete(0, END)
            self.campoConfirmaSenha.delete(0, END)
            self.campoSenha.delete(0, END)
            
            self.box1.current(0)
            self.box2.current(0)
            self.box3.current(0)
            self.box4.current(0)
            self.box5.current(0)
            self.box6.current(0)
            self.box7.current(0)
            
            self.campoNome.focus_force()
        
    def verificar_campos_cadastro(self):
        
        #Atribuição dos campos cadastrais nas variáveis
        
        a = self.campoNome.get()
        b = self.campoCPF.get()
        c = self.campoSenha.get()
        d = self.campoConfirmaSenha.get()
        
        #Atribuição dos valores dos boxes de seleção nas variáves
        
        A = self.box1.get()
        B = self.box2.get()
        C = self.box3.get()
        D = self.box4.get()
        E = self.box5.get()
        F = self.box6.get()
        G = self.box7.get()
        
        #Verificando se algum campo não foi preenchido

        if a == '' or b == '' or c == '' or d == '' or A == 'Select' or B == 'Select' or C == 'Select' or D == 'Select' or E == 'Select' or F == 'Select' or G == 'Select':
            
            #Mudando cor para preto caso o usuário tenha errado em algum campo e tenha corrigdo
            
            self.lbNome['fg'] = 'black'
            self.lbCPF['fg'] = 'black'
            self.lbSenha['fg'] = 'black'
            self.lbConfirmaSenha['fg'] = 'black'
            
            self.campoNome['bg'] = 'white'
            self.campoCPF['bg'] = 'white'
            self.campoSenha['bg'] = 'white'
            self.campoConfirmaSenha['bg'] = 'white'
            
            self.lbSerramento['fg'] = 'black'
            self.lbAplainamento['fg'] = 'black'
            self.lbTorneamento['fg'] = 'black'
            self.lbFresagem['fg'] = 'black'
            self.lbFurar['fg'] = 'black'
            self.lbBrochamento['fg'] = 'black'
            self.lbEletroerosao['fg'] = 'black'
        
            if a == '':
                
                self.campoNome['bg'] = 'pink'
                self.lbNome['fg'] = 'red'
            
            if b == '':
                
                self.campoCPF['bg'] = 'pink'
                self.lbCPF['fg'] = 'red'
            
            if c == '':

                self.campoSenha['bg'] = 'pink'
                self.lbSenha['fg'] = 'red'
        
            if d == '':
        
                self.campoConfirmaSenha['bg'] = 'pink'
                self.lbConfirmaSenha['fg'] = 'red'
            
            if A == 'Select':
                self.lbSerramento['fg'] = 'red'
            
            if B == 'Select':
                self.lbAplainamento['fg'] = 'red'
            
            if C == 'Select':
                self.lbTorneamento['fg'] = 'red'
            
            if D == 'Select':
                self.lbFresagem['fg'] = 'red'
            
            if F == 'Select':
                self.lbFurar['fg'] = 'red'
            
            if G == 'Select':
                self.lbBrochamento['fg'] = 'red'
            
            if E == 'Select':
                self.lbEletroerosao['fg'] = 'red'
            
            return messagebox.showerror('Alerta', 'Verifique os campos')
        
        elif len(a) < 6 or len(b) < 11 or len(c) < 8 or len(d) < 8 or c != d:
            
            #Mudando cor para preto caso o usuário tenha errado em algum campo e tenha corrigdo
            
            self.lbNome['fg'] = 'black'
            self.lbCPF['fg'] = 'black'
            self.lbSenha['fg'] = 'black'
            self.lbConfirmaSenha['fg'] = 'black'
            
            self.campoNome['bg'] = 'white'
            self.campoCPF['bg'] = 'white'
            self.campoSenha['bg'] = 'white'
            self.campoConfirmaSenha['bg'] = 'white'
            
            self.lbSerramento['fg'] = 'black'
            self.lbAplainamento['fg'] = 'black'
            self.lbTorneamento['fg'] = 'black'
            self.lbFresagem['fg'] = 'black'
            self.lbFurar['fg'] = 'black'
            self.lbBrochamento['fg'] = 'black'
            self.lbEletroerosao['fg'] = 'black'
        
            if len(a) < 6:
                    
                    self.campoNome['bg'] = 'pink'
                    self.lbNome['fg'] = 'red'
                
            if len(b) < 11:
                
                self.campoCPF['bg'] = 'pink'
                self.lbCPF['fg'] = 'red'
            
            if len(c) < 8:

                self.campoSenha['bg'] = 'pink'
                self.lbSenha['fg'] = 'red'
        
            if len(d) < 8:
        
                self.campoConfirmaSenha['bg'] = 'pink'
                self.lbConfirmaSenha['fg'] = 'red'
                
            return messagebox.showerror('Alerta', 'Verifique os campos')
        
        try:   
            
            if self.bancoServer.is_connected():
                
                self.inserindo_dados_cadastro()
            
        except:
            messagebox.showerror('Alerta', 'Erro ao tentar conexão com Banco de Dados')
            self.connection_database()
        
    def crud_os_finalizada(self):
        
        self.connection_database()
        
        #Buscando os dados de os Finalizado do Banco de Dados para inserir na Treeview
        self.cursor.execute('use empresa_funcionarios')
        self.cursor.execute("select ID, Operador, OS, codigoPeca, CodigoOperacao, Tipo from monitoria_funcionarios order by id desc limit 1")
        valido = self.cursor.fetchall()
        
        if len(valido) >= 1:
            
            #Buscando o último dado do banco e último dado da lista, se for diferente: é um novo dado, e será inserido na Treeview
            if self.finalizado == [] or valido[0] != self.finalizado[-1]:
                
                idd = valido[0][0]
                nome = valido[0][1]
                os = valido[0][2]
                peca = valido[0][3]
                operacao = valido[0][4]
                tipo = valido[0][5]
                
                self.visualiza.insert("", "end", values=(idd, nome, os, peca, operacao, tipo))
                
                #Adcionando novo dado na lista para não se repetir na Treeview
                self.finalizado.append(valido[0])
                
                self.encerrando_conexao_database()
        
        self.janelaCadastro.after(1000, self.crud_os_finalizada)
    
class Front_End(Back_End):
    
    def __init__(self):
        
        self.janelaCadastro = Tk()
        self.janelaCadastro.geometry('1000x500')
        self.janelaCadastro.title('Janela Principal')
        
        self.sistemaOperacional = system()
        
        #Configurando o ambiente para se maximizado de acordo com o sistema operacional
        
        if self.sistemaOperacional == 'Windows':
            self.janelaCadastro.state('zoomed')
        else:
            self.janelaCadastro.attributes('-zoomed', True)
            
        self.connection_database()
        
        self.abas = ttk.Notebook(self.janelaCadastro)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        
        self.abas.add(self.aba1, text='Principal')
        self.abas.add(self.aba2, text='Cadastro')
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        ############################################## ABA 1 #########################################
        
        #Criando Treeview para visualização dos dados de OS Finalizados
        
        self.visualiza = ttk.Treeview(self.aba1, column=('1','2','3','4','5','6'), show='headings')
        self.visualiza.heading('1', text='ID')
        self.visualiza.heading('2', text='NOME')
        self.visualiza.heading('3', text='OS Finalizadas')
        self.visualiza.heading('4', text='PEÇA')
        self.visualiza.heading('5', text='OPERAÇÃO')
        self.visualiza.heading('6', text='TIPO')
        
        self.visualiza.column("1", width=-50, anchor='n')
        self.visualiza.column("2", width=170, anchor='n')
        self.visualiza.column("3", width=1, anchor='n')
        self.visualiza.column("4", width=1, anchor='n')
        self.visualiza.column("5", width=1, anchor='n')
        self.visualiza.column("6", width=30, anchor='n')
        
        self.visualiza.place(relx=0, rely=0.600, relwidth=0.480, relheight=0.400)
        
        scrollbar = Scrollbar(self.aba1, orient="vertical", command=self.visualiza.yview)
        self.visualiza.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=0.480, rely=0.600, relheight=0.400)
        
        self.cursor.execute("select Id, Operador, OS, codigoPeca, CodigoOperacao, Tipo from monitoria_funcionarios")
        valido = self.cursor.fetchall()

        self.finalizado = []

        if len(valido) >= 1:
            
            for c in valido:
                
                self.finalizado.append(c)
                
            #utilizando estrutura de repetição para inserir os dados obtidos já armazenado na lista "finalizado"
            for i in range (len(self.finalizado)):

                #extraindo do banco de dados as informações e armazenando nas variáveis
                idd = self.finalizado[i][0]
                nome = self.finalizado[i][1]
                os = self.finalizado[i][2]
                peca = self.finalizado[i][3]
                operacao = self.finalizado[i][4]
                tipo = self.finalizado[i][5]
                
                self.visualiza.insert("", "end", values=(idd, nome, os, peca, operacao, tipo))

        
        threading.Thread(target=self.crud_os_finalizada).start()
        
        #Criando Treeview para visualização dos dados de OS Pausados
        
        self.visualiza2 = ttk.Treeview(self.aba1, column=('1','2','3','4','5'), show='headings')
        self.visualiza2.heading('1', text='NOME')
        self.visualiza2.heading('2', text='OS Pausadas')
        self.visualiza2.heading('3', text='PEÇA')
        self.visualiza2.heading('4', text='OPERAÇÃO')
        self.visualiza2.heading('5', text='TIPO')
        
        self.visualiza2.column("1", width=30, anchor='n')
        self.visualiza2.column("2", width=30, anchor='n')
        self.visualiza2.column("3", width=30, anchor='n')
        self.visualiza2.column("4", width=30, anchor='n')
        self.visualiza2.column("5", width=30, anchor='n')
        
        self.visualiza2.place(relx=0.500, rely=0.600, relwidth=0.480, relheight=1)
        
        scrollbar2 = Scrollbar(self.aba1, orient="vertical", command=self.visualiza2.yview)
        self.visualiza2.configure(yscrollcommand=scrollbar2.set)
        scrollbar2.place(relx=0.980, rely=0.600, relheight=0.400)
        
        
        ############################################## ABA 2 #########################################
        
        
        corPadrao = self.janelaCadastro['bg']
        
        #Configurando Imagem da Logo Multimoldes
        
        image = PhotoImage(file='image/logo-multimoldes.png')
        
        self.logo = Label(self.aba2, image=image, bg=corPadrao)
        self.logo.pack()
        
        #Frame de Login dos registros de conta do usuário
        
        self.frameDadosLogin = Frame(self.aba2, highlightbackground='grey', highlightthickness=2)
        self.frameDadosLogin.place(relx=0.100, rely=0.200, relwidth=0.800, relheight=0.250)
        
        #labels referente aos campos de login
        
        self.lbDados = Label(self.frameDadosLogin, text='Dados', font=('impact', 14))
        self.lbDados.place(relx=0.010, rely=0.010)
        
        self.lbNome = Label(self.frameDadosLogin, text='Nome', font=('impact',12))
        self.lbCPF = Label(self.frameDadosLogin, text='CPF', font=('impact',12))
        self.lbSenha = Label(self.frameDadosLogin, text='Senha', font=('impact',12))
        self.lbSenhaErro = Label(self.frameDadosLogin, text='', font=('arial', 10), fg='red')
        self.lbConfirmaSenha = Label(self.frameDadosLogin, text='Confirme Senha', font=('impact',12))
        self.lbConfirmaSenhaErro = Label(self.frameDadosLogin, text='', font=('arial', 10), fg='red')
        
        self.lbNome.place(relx=0.020, rely=0.300)
        self.lbCPF.place(relx=0.470, rely=0.300)
        self.lbSenha.place(relx=0.020, rely=0.600)
        self.lbSenhaErro.place(relx=0.110, rely=0.750)
        self.lbConfirmaSenha.place(relx=0.300, rely=0.600)
        self.lbConfirmaSenhaErro.place(relx=0.440, rely=0.750)
        
        #Função que impedirá que o usuário digite valores diferentes do que o campos propõe
        
        def verifica_campo(*args):
            
            value = strNome.get()
            if len(value) > 0:
                
                if value[-1].isnumeric():
                    strNome.set(value[:-1])
                else:
                    strNome.set(value[:50])
            
            value2 = nCPF.get()
            if len(value2) > 0:
                
                if not value2[-1].isnumeric():
                    nCPF.set(value2[:-1])
                else:
                    nCPF.set(value2[:11])

            value3 = nSenha.get()
            if len(value3) > 0:
                                
                if not value3[-1].isnumeric():
                    nSenha.set(value3[:-1])
                else:
                    nSenha.set(value3[0:8])
                    
                if len(value3) >= 8:
                    self.campoConfirmaSenha.configure(state=NORMAL)
                else:
                    self.campoConfirmaSenha.configure(state=DISABLED)
            
            else:
                self.lbConfirmaSenhaErro['text'] = ''
                self.campoConfirmaSenha.configure(state=DISABLED)
            
            value4 = nConfirmaSenha.get()
            if len(value4) > 0:
                
                if len(value4) == 8 and value4 != value3:
                    self.lbConfirmaSenhaErro['text'] = 'As senhas não coincidem'
                
                elif len(value4) == 8 and value4 == value3:
                    self.lbConfirmaSenhaErro['text'] = ''
                    
                if not value4[-1].isnumeric():
                    nConfirmaSenha.set(value4[:-1])
                else:
                    nConfirmaSenha.set(value4[:8])
            else:
                self.lbConfirmaSenhaErro['text'] = ''
        
        #Variáveis que será utilizadas para verificação dos campos
        
        strNome = StringVar()
        strNome.trace('w', verifica_campo)

        nCPF = StringVar()
        nCPF.trace('w', verifica_campo)
        
        nSenha = StringVar()
        nSenha.trace('w', verifica_campo)
        
        nConfirmaSenha = StringVar()
        nConfirmaSenha.trace('w', verifica_campo)

        #Campos de preenchimento dos dados de login
        
        self.campoNome = Entry(self.frameDadosLogin, font=('arial',12), textvariable=strNome)
        self.campoNome.focus_force()
        self.campoCPF = Entry(self.frameDadosLogin, font=('arial',12), textvariable=nCPF)
        self.campoSenha = Entry(self.frameDadosLogin, font=('arial',12), show='*', textvariable=nSenha)
        self.campoConfirmaSenha = Entry(self.frameDadosLogin, font=('arial',12), show='*', textvariable=nConfirmaSenha,state=DISABLED)
        
        self.campoNome.place(relx=0.080, rely=0.300, relwidth=0.350)
        self.campoCPF.place(relx=0.518, rely=0.300, relwidth=0.175)
        self.campoSenha.place(relx=0.085, rely=0.600, relwidth=0.175)
        self.campoConfirmaSenha.place(relx=0.430, rely=0.600, relwidth=0.175)
        
        def mostrar_senha(*args):

            if senhaVisible.get() == 1:
                
                self.campoSenha['show'] = ''
                self.campoConfirmaSenha['show'] = ''
            
            else:
                
                self.campoSenha['show'] = '*'
                self.campoConfirmaSenha['show'] = '*'
        
        senhaVisible = IntVar()
        
        self.check = Checkbutton(self.frameDadosLogin, text='Mostrar Senha', variable=senhaVisible, command=mostrar_senha)
        self.check.place(relx=0.620, rely=0.600)
        
        #Frame de atribuição das habilidades dos funcionários
        
        self.frameAtribuicao = Frame(self.aba2, highlightbackground='grey', highlightthickness=2)
        self.frameAtribuicao.place(relx=0.100, rely=0.460, relwidth=0.800, relheight=0.250)
        
        #labels referente aos campos de Atribuição
        
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
        
        #Boxes de seleção para o nível de habilidades do usuário em cada operação

        self.box1 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.box1['values'] = ('Select', '0', '1', '2', '3')
        self.box1.current(0)
        
        self.box2 = ttk.Combobox(self.frameAtribuicao, font=('arial', 13), state="readonly")
        self.box2['values'] = ('Select', '0', '1', '2', '3')
        self.box2.current(0)

        self.box3 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.box3['values'] = ('Select', '0', '1', '2', '3')
        self.box3.current(0)
    
        self.box4 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.box4['values'] = ('Select', '0', '1', '2', '3')
        self.box4.current(0)
        
        self.box5 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.box5['values'] = ('Select', '0', '1', '2', '3')
        self.box5.current(0)
        
        self.box6 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.box6['values'] = ('Select', '0', '1', '2', '3')
        self.box6.current(0)
        
        self.box7 = ttk.Combobox(self.frameAtribuicao, font=('arial',13), state="readonly")
        self.box7['values'] = ('Select', '0', '1', '2', '3')
        self.box7.current(0)        
                        
        self.box1.place(relx=0.020, rely=0.600, relwidth=0.11)
        self.box2.place(relx=0.15, rely=0.600, relwidth=0.11)
        self.box3.place(relx=0.28, rely=0.600, relwidth=0.11)
        self.box4.place(relx=0.41, rely=0.600, relwidth=0.11)
        self.box5.place(relx=0.54, rely=0.600, relwidth=0.11)
        self.box6.place(relx=0.67, rely=0.600, relwidth=0.11)
        self.box7.place(relx=0.80, rely=0.600, relwidth=0.11)
        
        #Botão que confirmará os dados quando solicitado
        
        self.botaoConfirmar = Button(self.aba2, text='Confirmar', font=('arial black', 13), command=self.verificar_campos_cadastro)
        self.botaoConfirmar.place(relx=0.82, rely=0.90)

        self.janelaCadastro.mainloop()

instancia = Front_End()
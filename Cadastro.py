from tkinter import *
from tkinter import ttk
from platform import *
from tkinter import messagebox
from datetime import *
import mysql.connector
import threading

class Database():
    
    def connection_database(self):
        
        try:
            
            self.bancoServer = mysql.connector.connect(
                                                        host='localhost',
                                                        database='empresa_funcionarios',
                                                        user='MultimoldesClient',
                                                        password='')
            self.cursor = self.bancoServer.cursor()
            self.bancoConnect = True
        
        except:
            self.bancoConnect = False
    
    def encerrando_conexao_database(self):
    
        self.bancoServer.close()
        self.cursor.close()
    
class Back_End(Database):
    
    def crud_os_finalizada(self):
        
        valido = ''
        
        self.connection_database()
        
        if self.bancoConnect:
        
            #Buscando os dados de os Finalizado do Banco de Dados para inserir na Treeview
            self.cursor.execute("select ID, Operador, OS, codigoPeca, CodigoOperacao, Tipo from monitoria_funcionarios where DataFinal = '"+self.dataHoje+"' order by id desc limit 1 ")
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
                
                self.bancoServer.close()
                self.cursor.close()
        
        self.janelaInicial.after(1000, self.crud_os_finalizada)
        
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
            
            if E == 'Select':
                self.lbFurar['fg'] = 'red'
            
            if F == 'Select':
                self.lbBrochamento['fg'] = 'red'
            
            if G == 'Select':
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
            messagebox.showerror('Alerta', 'Erro conexão com Banco de Dados não estabelecida')
    
    def inserindo_dados_cadastro(self):
            
        #Verificando se o CPF digitado no campo não está cadastrado no banco
        
        self.cursor.execute("select * from funcionarios where CPF = "+self.campoCPF.get())
        valido = self.cursor.fetchall()

        if len(valido) == 1:
            return messagebox.showinfo('Alerta', 'O CPF - '+self.campoCPF.get()+', já possui cadastro')

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
        
        try:
        
            self.cursor.execute("INSERT INTO funcionarios VALUES (ID, '"+a+"','"+b+"','"+c+"')")
            self.bancoServer.commit()
            
            self.cursor.execute("INSERT INTO habilidade_funcionarios VALUES ('"+a+"','"+b+"','"+A+"','"+B+"','"+C+"','"+D+"','"+E+"','"+F+"','"+G+"')")
            self.bancoServer.commit()
        
        except:
            return messagebox.showerror('Alerta', 'Erro ao inserir dados. Verifique a conexão com o banco')
        
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
    
    def exibir_detalhes_frame1(self, event):
        
        selecionada = self.visualiza.selection()[0]
        x = self.visualiza.item(selecionada, "values")
        
        i_d = x[0]
        
        if self.bancoServer.is_connected():
            self.cursor.execute("select Operador, CPF, ID, OS, CodigoPeca, CodigoOperacao, Tipo, HoraLogin, HoraInicial, HoraFinal, DataInicial, DataFinal, TempProgramado, tempGasto, tempOperando, TempGastoExt, VezTempExt from monitoria_funcionarios where id = "+i_d)
            
            valido = self.cursor.fetchall()
            
            for dado in valido:
                nome, cpf, idd, os, peca, operacao, tipo, horaLogin, horaInicial, horaFinal, dataInicial, dataFinal, tempProgramado, tempGasto, tempOperando, tempExtra, vezTempoExtra = dado
                
                self.lbInfo1['fg'] ='black'
                self.lbInfo2['fg'] ='black'
                self.lbInfo3['fg'] ='black'
                self.lbInfo4['fg'] ='black'
                self.lbInfo5['fg'] ='black'
                self.lbInfo6['fg'] ='black'
                self.lbInfo7['fg'] ='black'
                self.lbInfo8['fg'] ='black'
                self.lbInfo9['fg'] ='black'
                self.lbInfo10['fg'] ='black'
                self.lbInfo11['fg'] ='black'
                self.lbInfo12['fg'] ='black'
                self.lbInfo13['fg'] ='black'
                self.lbInfo14['fg'] ='black'
                self.lbInfo15['fg'] ='black'
                self.lbInfo16['fg'] ='black'
                self.lbInfo17['fg'] ='black'
                
                self.nomeF1['text'] = nome
                self.cpfF1['text'] = cpf
                self.idF1['text'] = idd
                self.osF1['text'] = os
                self.pecaF1['text'] = peca
                self.operacaoF1['text'] = operacao
                self.tipoF1['text'] = tipo
                self.horaLoginF1['text'] = horaLogin
                self.horaInicialF1['text'] = horaInicial
                self.horaFinalF1['text'] = horaFinal
                self.dataInicialF1['text'] = dataInicial
                self.dataFinalF1['text'] = dataFinal
                self.tempProgramadoF1['text'] = tempProgramado
                self.tempGastoF1['text'] = tempGasto
                self.tempOperandoF1['text'] = tempOperando
                self.tempExtraF1['text'] = tempExtra
                self.vezTempoExtraF1['text'] = vezTempoExtra
                
                if tempExtra != '00:00:00': self.tempExtraF1['fg'] = 'red'                    
                else: self.tempExtraF1['fg'] = '#006dfa'
                    
                if vezTempoExtra != '0': self.vezTempoExtraF1['fg'] = 'red'
                else: self.vezTempoExtraF1['fg'] = '#006dfa'
    
class Front_End(Back_End):
    
    def __init__(self):
        
        self.janelaInicial = Tk()
        self.janelaInicial.geometry('1000x500')
        self.janelaInicial.title('Multimoldes Admin')
        
        self.sistemaOperacional = system()
        
        #Configurando o ambiente para se maximizado de acordo com o sistema operacional
        
        if self.sistemaOperacional == 'Windows': 
            self.janelaInicial.state('zoomed')
        else:
            self.janelaInicial.attributes('-zoomed', True)
        
        corPadrao = self.janelaInicial['bg']
        
        self.connection_database()
        if not self.bancoConnect:
            messagebox.showerror('Alerta', 'Erro na conexão com Banco de Dados')
        
        #Criando e adicionando abas
        
        self.abas = ttk.Notebook(self.janelaInicial)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)
        
        self.abas.add(self.aba1, text='Principal')
        self.abas.add(self.aba2, text='Cadastrar')
        self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        
        #Configurando Imagem da Logo Multimoldes na aba Cadastro
        
        image = PhotoImage(file='image/logo-multimoldes.png')
        
        self.logo = Label(self.aba2, image=image, bg=corPadrao)
        self.logo.pack()
        
        self.aba_principal()
        
        self.aba_cadastro()

        self.janelaInicial.mainloop()
    
    def aba_principal(self):
        
        #Labels de indicação
        
        lbDetalhes1 = Label(self.aba1, text='OS Finalizada', font=('arial', 14, 'bold'))
        lbDetalhes1.place(relx=0.020, rely=0.055)
        
        lbDetalhes2 = Label(self.aba1, text='OS Pausada', font=('arial', 14, 'bold'))
        lbDetalhes2.place(relx=0.530, rely=0.055)
        
        #Frame de Visualização de dados Os Finalizada
        
        frameDetalhe1 = Frame(self.aba1, highlightbackground='grey', highlightthickness=2)
        frameDetalhe1.place(relx=0.010, rely=0.120, relwidth=0.450, relheight=0.400)
        
        #Labels Informativos de dados do Frame de Visualização de Os Finalizada
        
        corPadrao = self.janelaInicial['bg']
        
        self.lbInfo1 = Label(frameDetalhe1, text='Nome', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo1.place(relx=0.020, rely=0.025)
        
        self.lbInfo2 = Label(frameDetalhe1, text='CPF', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo2.place(relx=0.50, rely=0.025)
        
        self.lbInfo3 = Label(frameDetalhe1, text='ID', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo3.place(relx=0.850, rely=0.025)
        
        self.lbInfo4 = Label(frameDetalhe1, text='OS', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo4.place(relx=0.020, rely=0.170)
        
        self.lbInfo5 = Label(frameDetalhe1, text='Peça', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo5.place(relx=0.210, rely=0.170)
        
        self.lbInfo6 = Label(frameDetalhe1, text='Operação', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo6.place(relx=0.450, rely=0.170)
        
        self.lbInfo7 = Label(frameDetalhe1, text='Tipo', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo7.place(relx=0.730, rely=0.170)
        
        self.lbInfo8 = Label(frameDetalhe1, text='Hora de Login', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo8.place(relx=0.020, rely=0.320)
        
        self.lbInfo9 = Label(frameDetalhe1, text='Hora Inicial', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo9.place(relx=0.350, rely=0.320)
        
        self.lbInfo10 = Label(frameDetalhe1, text='Hora Final', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo10.place(relx=0.650, rely=0.320)
        
        self.lbInfo11 = Label(frameDetalhe1, text='Data Inicial', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo11.place(relx=0.020, rely=0.470)
        
        self.lbInfo12 = Label(frameDetalhe1, text='Data Final', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo12.place(relx=0.40, rely=0.470)
        
        self.lbInfo13 = Label(frameDetalhe1, text='T. Programado', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo13.place(relx=0.020, rely=0.620)
        
        self.lbInfo14 = Label(frameDetalhe1, text='T. Gasto', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo14.place(relx=0.380, rely=0.620)
        
        self.lbInfo15 = Label(frameDetalhe1, text='T. Operando', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo15.place(relx=0.670, rely=0.620)
        
        self.lbInfo16 = Label(frameDetalhe1, text='T. Extra', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo16.place(relx=0.020, rely=0.760)
        
        self.lbInfo17 = Label(frameDetalhe1, text='Número de Vezes', font=('arial', 10, 'bold'), fg=corPadrao)
        self.lbInfo17.place(relx=0.350, rely=0.760)
        
        #Labels de captura de dados do frame visualização 1
        
        self.nomeF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.nomeF1.place(relx=0.10, rely=0.025, relwidth=0.390)
        
        self.cpfF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.cpfF1.place(relx=0.560, rely=0.025, relwidth=0.270)
        
        self.idF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.idF1.place(relx=0.900, rely=0.025, relwidth=0.050)
        
        self.osF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.osF1.place(relx=0.100, rely=0.170, relwidth=0.060)
        
        self.pecaF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.pecaF1.place(relx=0.320, rely=0.170, relwidth=0.080)
        
        self.operacaoF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.operacaoF1.place(relx=0.620, rely=0.170, relwidth=0.070)
        
        self.tipoF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tipoF1.place(relx=0.810, rely=0.170, relwidth=0.170)
        
        self.horaLoginF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.horaLoginF1.place(relx=0.200, rely=0.320, relwidth=0.130)
        
        self.horaInicialF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.horaInicialF1.place(relx=0.500, rely=0.320, relwidth=0.130)
        
        self.horaFinalF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.horaFinalF1.place(relx=0.800, rely=0.320, relwidth=0.130)
        
        self.dataInicialF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.dataInicialF1.place(relx=0.210, rely=.470, relwidth=0.130)
        
        self.dataFinalF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.dataFinalF1.place(relx=0.580, rely=0.470, relwidth=0.130)
        
        self.tempProgramadoF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempProgramadoF1.place(relx=0.220, rely=0.620, relwidth=0.130)
        
        self.tempGastoF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempGastoF1.place(relx=0.510, rely=0.620, relwidth=0.130)
        
        self.tempOperandoF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempOperandoF1.place(relx=0.840, rely=0.620, relwidth=0.130)
        
        self.tempExtraF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempExtraF1.place(relx=0.170, rely=0.760, relwidth=0.130)

        self.vezTempoExtraF1 = Label(frameDetalhe1, font=('arial', 10, 'bold'), fg='#006dfa')
        self.vezTempoExtraF1.place(relx=0.580, rely=0.760, relwidth=0.030)
        
        def limpar_dados_visualizados():
            
            self.nomeF1['text'] = ''
            self.cpfF1['text'] = ''
            self.idF1['text'] = ''
            self.osF1['text'] = ''
            self.pecaF1['text'] = ''
            self.operacaoF1['text'] = ''
            self.tipoF1['text'] = ''
            self.horaLoginF1['text'] = ''
            self.horaInicialF1['text'] = ''
            self.horaFinalF1['text'] = ''
            self.dataInicialF1['text'] = ''
            self.dataFinalF1['text'] = ''
            self.tempProgramadoF1['text'] = ''
            self.tempGastoF1['text'] = ''
            self.tempOperandoF1['text'] = ''
            self.tempExtraF1['text'] = ''
            self.vezTempoExtraF1['text'] = ''
            
            self.lbInfo1['fg'] = corPadrao
            self.lbInfo2['fg'] = corPadrao
            self.lbInfo3['fg'] = corPadrao
            self.lbInfo4['fg'] = corPadrao
            self.lbInfo5['fg'] = corPadrao
            self.lbInfo6['fg'] = corPadrao
            self.lbInfo7['fg'] = corPadrao
            self.lbInfo7['fg'] = corPadrao
            self.lbInfo8['fg'] = corPadrao
            self.lbInfo9['fg'] = corPadrao
            self.lbInfo10['fg'] = corPadrao
            self.lbInfo11['fg'] = corPadrao
            self.lbInfo12['fg'] = corPadrao
            self.lbInfo13['fg'] = corPadrao
            self.lbInfo14['fg'] = corPadrao
            self.lbInfo15['fg'] = corPadrao
            self.lbInfo16['fg'] = corPadrao
            self.lbInfo17['fg'] = corPadrao
        
        botaoLimpar = Button(self.aba1, text='Limpar', font=('arial', 8), command=limpar_dados_visualizados)
        botaoLimpar.place(relx=0.420, rely=0.070)
        
        #Frame de Visualização de dados Os Pausadas

        frameDetalhe2 = Frame(self.aba1, highlightbackground='grey', highlightthickness=2)
        frameDetalhe2.place(relx=0.520, rely=0.120, relwidth=0.450, relheight=0.400)
        
        #Labels Informativos de dados do Frame de Visualização de Pausada

        self.lbInfo01 = Label(frameDetalhe2, text='Nome', font=('arial', 10, 'bold'))
        self.lbInfo01.place(relx=0.020, rely=0.025)
        
        self.lbInfo02 = Label(frameDetalhe2, text='CPF', font=('arial', 10, 'bold'))
        self.lbInfo02.place(relx=0.50, rely=0.025)
        
        self.lbInfo03 = Label(frameDetalhe2, text='ID', font=('arial', 10, 'bold'))
        self.lbInfo03.place(relx=0.850, rely=0.025)
        
        self.lbInfo04 = Label(frameDetalhe2, text='OS', font=('arial', 10, 'bold'))
        self.lbInfo04.place(relx=0.020, rely=0.170)
        
        self.lbInfo05 = Label(frameDetalhe2, text='Peça', font=('arial', 10, 'bold'))
        self.lbInfo05.place(relx=0.210, rely=0.170)
        
        self.lbInfo06 = Label(frameDetalhe2, text='Operação', font=('arial', 10, 'bold'))
        self.lbInfo06.place(relx=0.450, rely=0.170)
        
        self.lbInfo07 = Label(frameDetalhe2, text='Tipo', font=('arial', 10, 'bold'))
        self.lbInfo07.place(relx=0.730, rely=0.170)
        
        self.lbInfo08 = Label(frameDetalhe2, text='Hora de Login', font=('arial', 10, 'bold'))
        self.lbInfo08.place(relx=0.020, rely=0.320)
        
        self.lbInfo09 = Label(frameDetalhe2, text='Hora Pausada', font=('arial', 10, 'bold'))
        self.lbInfo09.place(relx=0.350, rely=0.320)
        
        self.lbInfo010 = Label(frameDetalhe2, text='Hora Retomada', font=('arial', 10, 'bold'))
        self.lbInfo010.place(relx=0.650, rely=0.320)
        
        self.lbInfo011 = Label(frameDetalhe2, text='Data Pausada', font=('arial', 10, 'bold'))
        self.lbInfo011.place(relx=0.020, rely=0.470)
        
        self.lbInfo012 = Label(frameDetalhe2, text='Data Retomada', font=('arial', 10, 'bold'))
        self.lbInfo012.place(relx=0.40, rely=0.470)
        
        self.lbInfo013 = Label(frameDetalhe2, text='T. Programado', font=('arial', 10, 'bold'))
        self.lbInfo013.place(relx=0.020, rely=0.620)
        
        self.lbInfo014 = Label(frameDetalhe2, text='T. Gasto', font=('arial', 10, 'bold'))
        self.lbInfo014.place(relx=0.380, rely=0.620)
        
        self.lbInfo015 = Label(frameDetalhe2, text='T. Operando', font=('arial', 10, 'bold'))
        self.lbInfo015.place(relx=0.670, rely=0.620)
        
        self.lbInfo016 = Label(frameDetalhe2, text='T. Extra', font=('arial', 10, 'bold'))
        self.lbInfo016.place(relx=0.020, rely=0.760)
        
        self.lbInfo017 = Label(frameDetalhe2, text='Número de Vezes', font=('arial', 10, 'bold'))
        self.lbInfo017.place(relx=0.350, rely=0.760)
        
        self.lbInfo018 = Label(frameDetalhe2, text='Motivo da Pausa', font=('arial', 10, 'bold'))
        self.lbInfo018.place(relx=0.020, rely=0.900)

        #Labels de captura de dados do frame visualização 2

        self.nomeF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.nomeF2.place(relx=0.10, rely=0.025, relwidth=0.390)
        
        self.cpfF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.cpfF2.place(relx=0.560, rely=0.025, relwidth=0.270)
        
        self.idF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.idF2.place(relx=0.900, rely=0.025, relwidth=0.050)
        
        self.osF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.osF2.place(relx=0.100, rely=0.170, relwidth=0.060)
        
        self.pecaF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.pecaF2.place(relx=0.320, rely=0.170, relwidth=0.080)
        
        self.operacaoF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.operacaoF2.place(relx=0.620, rely=0.170, relwidth=0.070)
        
        self.tipoF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tipoF2.place(relx=0.810, rely=0.170, relwidth=0.170)
        
        self.horaLoginF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.horaLoginF2.place(relx=0.200, rely=0.320, relwidth=0.130)
        
        self.horaInicialF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.horaInicialF2.place(relx=0.500, rely=0.320, relwidth=0.130)
        
        self.horaFinalF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.horaFinalF2.place(relx=0.800, rely=0.320, relwidth=0.130)
        
        self.dataInicialF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.dataInicialF2.place(relx=0.210, rely=.470, relwidth=0.130)
        
        self.dataFinalF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.dataFinalF2.place(relx=0.580, rely=0.470, relwidth=0.130)
        
        self.tempProgramadoF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempProgramadoF2.place(relx=0.220, rely=0.620, relwidth=0.130)
        
        self.tempGastoF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempGastoF2.place(relx=0.510, rely=0.620, relwidth=0.130)
        
        self.tempOperandoF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempOperandoF2.place(relx=0.840, rely=0.620, relwidth=0.130)
        
        self.tempExtraF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.tempExtraF2.place(relx=0.170, rely=0.760, relwidth=0.130)

        self.vezTempoExtraF2 = Label(frameDetalhe2, font=('arial', 10, 'bold'), fg='#006dfa')
        self.vezTempoExtraF2.place(relx=0.580, rely=0.760, relwidth=0.030)
        
        def limpar_dados_visualizados2():
            
            self.lbInfo01['fg'] = corPadrao
            self.lbInfo02['fg'] = corPadrao
            self.lbInfo03['fg'] = corPadrao
            self.lbInfo04['fg'] = corPadrao
            self.lbInfo05['fg'] = corPadrao
            self.lbInfo06['fg'] = corPadrao
            self.lbInfo07['fg'] = corPadrao
            self.lbInfo07['fg'] = corPadrao
            self.lbInfo08['fg'] = corPadrao
            self.lbInfo09['fg'] = corPadrao
            self.lbInfo010['fg'] = corPadrao
            self.lbInfo011['fg'] = corPadrao
            self.lbInfo012['fg'] = corPadrao
            self.lbInfo013['fg'] = corPadrao
            self.lbInfo014['fg'] = corPadrao
            self.lbInfo015['fg'] = corPadrao
            self.lbInfo016['fg'] = corPadrao
            self.lbInfo017['fg'] = corPadrao
            self.lbInfo018['fg'] = corPadrao
            
            self.nomeF2['text'] = ''
            self.cpfF2['text'] = ''
            self.idF2['text'] = ''
            self.osF2['text'] = ''
            self.pecaF2['text'] = ''
            self.operacaoF2['text'] = ''
            self.tipoF2['text'] = ''
            self.horaLoginF2['text'] = ''
            self.horaInicialF2['text'] = ''
            self.horaFinalF2['text'] = ''
            self.dataInicialF2['text'] = ''
            self.dataFinalF2['text'] = ''
            self.tempProgramadoF2['text'] = ''
            self.tempGastoF2['text'] = ''
            self.tempOperandoF2['text'] = ''
            self.tempExtraF2['text'] = ''
            self.vezTempoExtraF2['text'] = ''
        
        botaoLimpar2 = Button(self.aba1, text='Limpar', font=('arial', 8), command=limpar_dados_visualizados2)
        botaoLimpar2.place(relx=0.930, rely=0.070)
        
        #Criando Treeview para visualização dos dados de OS Finalizados
        
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('arial', 9, 'bold'))
        
        self.visualiza = ttk.Treeview(self.aba1, column=('1','2','3','4','5','6'), show='headings')
        self.visualiza.heading('1', text='ID')
        self.visualiza.heading('2', text='NOME')
        self.visualiza.heading('3', text='OS')
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
        self.visualiza.bind("<Double-1>", self.exibir_detalhes_frame1)
        
        scrollbar = Scrollbar(self.aba1, orient="vertical", command=self.visualiza.yview)
        self.visualiza.configure(yscrollcommand=scrollbar.set)
        scrollbar.place(relx=0.480, rely=0.600, relheight=0.400)
        
        valido = ''
        
        self.dataHoje = datetime.now().date().strftime('%d/%m/%Y')
        
        if self.bancoConnect:
            
            self.cursor.execute("select Id, Operador, OS, codigoPeca, CodigoOperacao, Tipo from monitoria_funcionarios WHERE DataFinal = '"+self.dataHoje+"'")
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

        
        #Criando Treeview para visualização dos dados de OS Pausados
        
        self.visualiza2 = ttk.Treeview(self.aba1, column=('1','2','3','4','5','6','7'), show='headings')
        self.visualiza2.heading('1', text='ID')
        self.visualiza2.heading('2', text='NOME')
        self.visualiza2.heading('3', text='OS')
        self.visualiza2.heading('4', text='PEÇA')
        self.visualiza2.heading('5', text='OPERAÇÃO')
        self.visualiza2.heading('6', text='TIPO')
        self.visualiza2.heading('7', text='PAUSA')
        
        self.visualiza2.column("1", width=-50, anchor='n')
        self.visualiza2.column("2", width=120, anchor='n')
        self.visualiza2.column("3", width=-45, anchor='n')
        self.visualiza2.column("4", width=-40, anchor='n')
        self.visualiza2.column("5", width=-10, anchor='n')
        self.visualiza2.column("6", width=10, anchor='n')
        self.visualiza2.column("7", width=40, anchor='n')
        
        self.visualiza2.place(relx=0.500, rely=0.600, relwidth=0.480, relheight=1)
        
        scrollbar2 = Scrollbar(self.aba1, orient="vertical", command=self.visualiza2.yview)
        self.visualiza2.configure(yscrollcommand=scrollbar2.set)
        scrollbar2.place(relx=0.980, rely=0.600, relheight=0.400)
        
        valido = ''

        if self.bancoConnect:
            
            self.cursor.execute("select ID, Operador, OS, CodigoPeca, CodigoOperacao, Tipo, MotivoPause from pausa_funcionarios where DataPause = '"+self.dataHoje+"'")
            valido = self.cursor.fetchall()

        self.pausado = []

        if len(valido) >= 1:
            
            for c in valido:
                
                self.pausado.append(c)
                
            #utilizando estrutura de repetição para inserir os dados obtidos já armazenado na lista "pausado"
            for i in range (len(self.pausado)):

                #extraindo do banco de dados as informações e armazenando nas variáveis
                idd = self.pausado[i][0]
                nome = self.pausado[i][1].title()
                os = self.pausado[i][2]
                peca = self.pausado[i][3]
                operacao = self.pausado[i][4]
                tipo = self.pausado[i][5]
                mPause = self.pausado[i][6]

                self.visualiza2.insert("", "end", values=(idd, nome, os, peca, operacao, tipo, mPause))
        
        threading.Thread(target=self.crud_os_finalizada).start()
        
    def aba_cadastro(self):
        
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

instancia = Front_End()
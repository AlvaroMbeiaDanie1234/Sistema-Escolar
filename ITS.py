from tkinter import*
from turtle import width
import mysql as errorcode
from mysql.connector import errorcode
import mysql.connector as mysql
from mysql import connector
import mysql.connector
import mysql
import mysql as mysql
from tkinter import ttk
from PIL import ImageTk,Image 
from tkinter import messagebox
from tkinter import messagebox, filedialog
from tkinter import simpledialog
import requests
from datetime import date
import datetime
import os, sys
import customtkinter


root = customtkinter.CTk()

image7=Image.open("D:\\Projectos\\Sistema Escolar\\Images\\first.png")
image6=ImageTk.PhotoImage(image7)
Label4=Label(root,image=image6, bd="0", justify="center", bg="white")
Label4.place(x=120, y=50)


TOP = Frame(root, width="12000", height="30", bg="skyblue")
TOP.place(x=0, y=0)

ITS = Label(TOP, text="Instituto Técnico de Saúde Nº 6080 Bela Vista", bg="skyblue", font="Arial 12")
ITS.place(x=480, y=2)

#===============================Local Para Fazer Login===========================#

def logar():
    Username = Nome.get()
    Password = Senha.get()
    if Username == "Username" or Password == "Password":
        messagebox.showerror("Erro de login", "Todos os dados são requiridos")
    elif Username =="Admin" and Password == "default":
        F2 = Frame(root, bg="white", width="1400", height="1000")
        F2.place(x=0, y=0)



        
       # img1 = ImageTk.PhotoImage(Image.open("Images\\primeiro.jpg"))
        #panel = Label(F2, image=img1)
        #panel.place(x=0, y=0)

        F2_TOP = Frame(F2, width="1400", height="30", bg="skyblue")
        F2_TOP.place(x=0, y=0)

        Logado = Label(F2_TOP, text="Logado como", bg="skyblue", fg="black", font="Arial 12")
        Logado.place(x=1, y=1)

        Logado = Label(F2_TOP, text="Administrador", bg="skyblue", fg="green", font="Arial 12")
        Logado.place(x=109, y=1)
    

        def sair():
            Msg = messagebox.askquestion("Sair", "Tens a certeza de que desejas sair")
            if Msg == 'yes':
                F2.destroy()
            else:
                pass


        LogOuT = Button(F2_TOP, text="Terminar Sessão", bg="skyblue", fg="red", font="Arial 12", bd="0", cursor="hand2", activebackground="green", command=sair)
        LogOuT.place(x=1090, y=1)

        def Novo_Aluno():
            F3 = Frame(F2, width="700", height="1000", bg="oldlace")
            F3.place(x=650, y=30)

            
            def sair():
                Msg = messagebox.askquestion("Perda de dados", "Se os dados não foram submetidos resultara em perda  de dados, tens a certeza de que desejas voltar?")
                if Msg == 'yes':
                    F3.destroy()
                else:
                    pass
                

            Voltar = Button(F3, text="Voltar", bg="oldlace", bd="0", cursor="hand2", activebackground="oldlace", command=sair)
            Voltar.place(x=590, y=40)

            Aluno_Frame = Label(F3, text="Cadastrar Aluno", font="Arial 15", bg="oldlace")
            Aluno_Frame.place(x=10, y=40)

            Aluno_Frame1 = Frame(F3, height="2", width="1000", bg="skyblue")
            Aluno_Frame1.place(x=10, y=63)


            Nome=Label(F3, text="Nome",font="Arial 10", bg="oldlace")
            Nome.place(x=10, y=120)
            
            Pai=Label(F3, text="Nome do Pai",font="Arial 10", bg="oldlace")
            Pai.place(x=10, y=160)
            
            Mae=Label(F3, text="Nome da Mãe", font="Arial 10", bg="oldlace")
            Mae.place(x=10, y=200)
            
            BI=Label(F3, text="Nº do BI", bg="oldlace")
            BI.place(x=10, y=240)
            
            Email=Label(F3, text="E-mail", bg="oldlace")
            Email.place(x=10, y=280)

            Nascimento=Label(F3, text="Data de Nascimento", bg="oldlace")
            Nascimento.place(x=10, y=320)
            
            Tel=Label(F3, text="Nº  de Telefone", bg="oldlace")
            Tel.place(x=10, y=360)

            Provincia=ttk.Combobox(F3, values=["Bengo","Benguela", "Bié","Cabinda","Kuando Kubango",
            "Kwanza Norte", "Kwanza Sul", "Cunene", "Huambo", "Huíla","Luanda","Lunda-Norte", "Lunda-Sul",
            "Malange", "Moxico", "Namibe", "Uige", "Zaire"], justify="center")
            Provincia.set("PROVÍNCIA")
            Provincia.place(x=10, y=410)

            Genero=ttk.Combobox(F3, values=["Masculino","Femenino"], justify="center", width="20")
            Genero.set("GENERO")
            Genero.place(x=220, y=410)

            Classe=ttk.Combobox(F3, values=["10ª Classe","11ª Classe", "12ª Classe", "13ª Classe"], justify="center")
            Classe.set("CLASSE")
            Classe.place(x=420, y=410)
            
            Ano_lectivo=ttk.Combobox(F3, values=["2022","2023", "2024", "2025", "2026", "2027", "2028", "2028", "2029", "2030"], justify="center")
            Ano_lectivo.set("ANO LECTIVO")
            Ano_lectivo.place(x=10, y=440)

            Curso=ttk.Combobox(F3, values=["Enfermagen","Análises Clinicas", "Farmácia", "Radiologia", "Fisioterapia"], justify="center")
            Curso.set("CURSO PRETENDIDO")
            Curso.place(x=220, y=440)

            Periodo=ttk.Combobox(F3, values=["Manhã","Tarde", "Noite"], justify="center")
            Periodo.set("PERÍODO")
            Periodo.place(x=420, y=440)

            #============================Entries================================#
            NomeEntry = ttk.Entry(F3, width="40", justify="center")
            NomeEntry.place(x=140, y=120)
            
            PaiEntry = ttk.Entry(F3, width="40", justify="center")
            PaiEntry.place(x=140, y=160)
            
            MaeEntry = ttk.Entry(F3, width="40", justify="center")
            MaeEntry.place(x=140, y=200)
            
            BiEntry = ttk.Entry(F3, width="40", justify="center")
            BiEntry.place(x=140, y=240)
            
            EmailEntry = ttk.Entry(F3, width="40", justify="center")
            EmailEntry.place(x=140, y=280)
            
            DataEntry = ttk.Entry(F3, width="40", justify="center")
            DataEntry.place(x=140, y=320)

            TelEntry = ttk.Entry(F3, width="40", justify="center")
            TelEntry.place(x=140, y=360)

            def enviar_dados():
                Nome = NomeEntry.get();
                Pai = PaiEntry.get();
                Mae = MaeEntry.get();
                BI = BiEntry.get();
                Email = EmailEntry.get();
                Nascimento = DataEntry.get();
                Tel = TelEntry.get();
                Natural_de = Provincia.get();
                Sexo = Genero.get();
                Nivel = Classe.get();
                Ano = Ano_lectivo.get();
                Cursos = Curso.get();
                Horario = Periodo.get()
                if(Nome =="" or Pai=="" or Mae =="" or BI==""  or Nascimento =="" or Tel =="" or Natural_de =="PROVÍNCIA" or Sexo=="GENERO" or Nivel=="CLASSE" or Ano=="ANO LECTIVO" or Cursos=="CURSO PRETENDIDO" or Horario=="PERÍODO"):
                    messagebox.showerror("Aviso", "Todos os dados são requeridos")
                else:
                    con = mysql.connector.connect(host="localhost", user="root", password="", database="ITS")
                    cursor = con.cursor()
                    try:
                        cursor.execute("insert into Alunos values (default,'"+ Nome +"','"+ Pai +"','"+ Mae +"','"+ BI +"','"+ Email +"','"+ Nascimento +"','"+ Tel +"','"+ Natural_de +"','"+ Sexo +"','"+ Nivel +"','"+ Ano +"','"+ Cursos +"','"+ Horario +"')")
                        cursor.execute("commit")
                        
                        for i, color in enumerate(["AMDM"]):
                            if i < ++10:
                                a = ttk.Progressbar(root, mode="determinate")
                                a.place(x=900, y=510)
                                a.start()

                                def progresso():
                                    a.destroy()
                                    messagebox.showinfo("Parabéns", "O cadastramento foi feito com sucesso")
                                    bom = Label(F2, text="Sucesso!", bg="oldlace", fg="green",font="Arial 12").place(x=900, y=510)
                                    NomeEntry.delete(0,'end')
                                    PaiEntry.delete(0, 'end')
                                    MaeEntry.delete(0, 'end')
                                    BiEntry.delete(0, 'end')
                                    EmailEntry.delete(0,'end')
                                    TelEntry.delete(0,'end')
                                    DataEntry.delete(0, 'end')
                                    Provincia.delete(0, 'end')
                                    Provincia.insert(0, "Provincia")
                                    Genero.delete(0, 'end')
                                    Genero.insert(0, "Genero")
                                    Classe.delete(0, 'end')
                                    Classe.insert(0, "Classe")
                                    Ano_lectivo.delete(0, 'end')
                                    Ano_lectivo.insert(0, "Ano Lectivo")
                                    Curso.delete(0, 'end')
                                    Curso.insert(0, "Curso Pretendido")
                                    Periodo.delete(0, 'end')
                                    Periodo.insert(0, "Turno")
                        

                                root.after(3000, progresso)
                

                        

                       


                    except mysql.connector.errors.DataError:
                        messagebox.showerror("Erro de data", "use de seguinte forma o parametro da data Ano-Mês-Dia")
                    except mysql.connector.errors.IntegrityError:
                        messagebox.showerror("Áviso", "Desculpe mais ja foi submetido notas com este número de identidade  " + BI)
                    except mysql.connector.errors.DatabaseError:
                        messagebox.showerror("Número ivalido", Tel + " não é um número de telefone valido")
                    except mysql.connector.errors.InterfaceError:
                        messagebox.showerror("Erro", "Notamos que o servidor esta offline tente mais tarde por favor")

            Submeter_novos_alunos = Button(F2, text="SUBMETER", bg="skyblue", cursor="hand2", bd="0", width="25", fg="white", font="Arial 10", command=enviar_dados)
            Submeter_novos_alunos.place(x=850, y=550)

        F2_TOP1 = Frame(F2, width="300", height="90", bg="oldlace", bd="2")
        F2_TOP1.place(x=10, y=70)
        Cadastrar = Button(F2_TOP1, text="CADASTRAR\nALUNO", bd="0", bg="oldlace", font="Arial 15", cursor="hand2", command=Novo_Aluno)
        Cadastrar.place(x=80, y=20)

       
        #=================================Local dos dados dos alunos============================#

        def buscar_alunos():
            F3 = Frame(root, width="1400", height="900", bg="white")
            F3.place(x=0, y=30)

            copyright = Label(F3, text="© Copyright 2022, all rights reserveds!", bg="white").place(x=130, y=610)

             #===================BUSCAR DADOS DOS ALUNOS============================#
              
            def Obter():
                ID = ID_Entry.get();
                if(ID == ""):
                    messagebox.showerror("Pesquisar Dados Do Estudante", "Digite o ID do estudante por favor!")
                else:
                    try:
                        con = mysql.connector.connect(host="localhost", user="root", password="", database="ITS")
                        cursor =con.cursor()
                        cursor.execute("select * from alunos  where Bi = ( '"+ ID_Entry.get() +"')")
                        rows = cursor.fetchall()
                       
                        for row in rows:
                            NomeEntry.insert(0, row[1])
                            PaiEntry.insert(0, row[2])
                            MaeEntry.insert(0, row[3])
                            BiEntry.insert(0, row[4])
                            EmailEntry.insert(0, row[5])
                            DataEntry.insert(0, row[6])
                            TelEntry.insert(0, row[7])
                            Provincia.delete(0, 'end')
                            Provincia.insert(0, row[8])
                            Genero.delete(0, 'end')
                            Genero.insert(0, row[9])
                            Classe.delete(0, 'end')
                            Classe.insert(0, row[10])
                            Ano_lectivo.delete(0, 'end')
                            Ano_lectivo.insert(0, row[11])
                            Curso.delete(0, 'end')
                            Curso.insert(0, row[12])
                            Periodo.delete(0, 'end')
                            Periodo.insert(0, row[13])

                            Msg = messagebox.askquestion("Imprimir dados", "Você deseja imprimir os dados de? " + ID)
                            if Msg == 'yes':
                                with open('Dados.txt', 'w') as Dados:
                                    Dados.write(' Instituto de Treinamento em Técnicas e Tecnologias\n\n')
                                    Dados.write('  Nome:       ' )
                                    Dados.write('  Filho de:   ' )
                                    Dados.write('  E de:       ' )
                                    Dados.write('_______________________________________________________________' + '\n')
                                    Dados.write('----------DADOS PROCESSADO NO SISTEMA ESCOLAR ITTT-------------' + '\n\n')
                                    with open('Dados.txt') as Dados:
                                        print(Dados.read())
                                    os.popen("Dados.txt")
                            else:
                                pass



                    except mysql.connector.errors.InterfaceError:
                        messagebox.showerror("Erro 402", "Sem conexão com os servidores")

#===================Assuntos dos erros principais no gerenciamento de alunos=======================================#
            rede = Label(F3, text="No Internet connection detected, try again later...", bg="white", fg="red", font="Arial 16")
            rede.place(x=650, y=300)
            rede402 = Label(F3, text="Error 402", bg="white", fg="red", font="Arial 40")
            rede402.place(x=750, y=230)

            rede402 = Message(F3,width="600", text="1º Verifique a sua conexção com a internet\n2º Certifique-se que o seu servidor local esta ligado\n3º Tente reiniciar o software\nÁviso: Caso continuares a obter o erro 402 contacte o desenvovedor por favor!", bg="white",  font="Arial 10")
            rede402.place(x=650, y=340)

            rede402_Sair = Button(F3, text="Contactar o desenvolvedor", bg="green", font="Arial 12", bd="0")
            rede402_Sair.place(x=790, y=430)
            
            Aluno_Frame = Label(F3, text="Gerenciador de Alunos", font="Arial 15", bg="white")
            Aluno_Frame.place(x=10, y=40)

            #=======================Local de atualizar o dados dos alunos===================#

            def Atualizar_dados():
                ID = ID_Entry.get();
                Nome = NomeEntry.get();
                Pai = PaiEntry.get();
                Mae = MaeEntry.get();
                BI = BiEntry.get();
                Email = EmailEntry.get();
                Nascimento = DataEntry.get();
                Tel = TelEntry.get();
                Natural_de = Provincia.get();
                Sexo = Genero.get();
                Nivel = Classe.get();
                Ano = Ano_lectivo.get();
                Cursos = Curso.get();
                Horario = Periodo.get()
                if(Nome =="" or Pai=="" or Mae =="" or BI==""  or Nascimento =="" or Tel =="" or Natural_de =="PROVÍNCIA" or Sexo=="GENERO" or Nivel=="CLASSE" or Ano=="ANO LECTIVO" or Cursos=="CURSO PRETENDIDO" or Horario=="PERÍODO"):
                    messagebox.showerror("Aviso", "Todos os dados são requeridos")
                else:
                    con = mysql.connector.connect(host="localhost", user="root", password="", database="ITS")
                    cursor =con.cursor()
                    cursor.execute("update  Alunos set Nome='" + Nome + "',Pai='" + Pai + "',Mae='" + Mae + "',BI='" + BI + "',Email='" + Email + "',Nascimento='" + Nascimento + "',Tel='" + Tel + "',Natural_de='" + Natural_de + "',Sexo='" + Sexo + "',Nivel='" + Nivel + "',Ano='" + Ano + "',Cursos='" + Cursos + "',Horario='" + Horario +"' where ID='" + BI + "'")
                    cursor.execute("commit")

                    NomeEntry.delete(0, 'end')
                    PaiEntry.delete(0, 'end')
                    MaeEntry.delete(0, 'end')
                    BiEntry.delete(0, 'end')
                    EmailEntry.delete(0,'end')
                    TelEntry.delete(0,'end')
                    DataEntry.delete(0, 'end')
                    Provincia.delete(0, 'end')
                    Provincia.insert(0, "Provincia")
                    Genero.delete(0, 'end')
                    Genero.insert(0, "Genero")
                    Classe.delete(0, 'end')
                    Classe.insert(0, "Classe")
                    Ano_lectivo.delete(0, 'end')
                    Ano_lectivo.insert(0, "Ano Lectivo")
                    Curso.delete(0, 'end')
                    Curso.insert(0, "Curso Pretendido")
                    Periodo.delete(0, 'end')
                    Periodo.insert(0, "Turno")
                    messagebox.showwarning("Aviso", "Atualizações de dados não disponivel no momento")
                    con.close();
                


            #==============Elimonar Estudantes ============#
            def Eliminar():
                ID = ID_Entry.get();
                if(ID ==""):
                    messagebox.showerror("Eliminar Estudante", "Digite o ID do estudante por favor!")
                else:
                    try:
                        Msg = messagebox.askquestion("Perda de dados", "Tens a certeza que desejas eliminar?\n Não sera possivel recuperar os dados apagados")
                        if Msg == 'yes':
                            con = mysql.connector.connect(host="localhost", user="root", password="", database="ITS")
                            cursor =con.cursor()
                            cursor.execute("delete from alunos  where Bi = ( '"+ ID_Entry.get() +"')")
                            cursor.execute("commit")
                            messagebox.showinfo("Atenção", "O Id foi eliminado com sucesso")

                            NomeEntry.delete(0, 'end')
                            PaiEntry.delete(0, 'end')
                            MaeEntry.delete(0, 'end')
                            BiEntry.delete(0, 'end')
                            EmailEntry.delete(0,'end')
                            TelEntry.delete(0,'end')
                            DataEntry.delete(0, 'end')
                            Provincia.delete(0, 'end')
                            Provincia.insert(0, "Provincia")
                            Genero.delete(0, 'end')
                            Genero.insert(0, "Genero")
                            Classe.delete(0, 'end')
                            Classe.insert(0, "Classe")
                            Ano_lectivo.delete(0, 'end')
                            Ano_lectivo.insert(0, "Ano Lectivo")
                            Curso.delete(0, 'end')
                            Curso.insert(0, "Curso Pretendido")
                            Periodo.delete(0, 'end')
                            Periodo.insert(0, "Turno")

                        else:
                            pass
                    except mysql.connector.errors.InterfaceError:
                        messagebox.showerror("Erro 402", "Impossivel deletar o id certifique-se que há conexção com a internet")
                        F3.update()
                        root.update()
                        ID_Entry.delete(0, 'end')
        


            def show():
                con = mysql.connector.connect(host="localhost", user="root", password="", database="ITS")
                cursor =con.cursor()
                cursor.execute("select * from alunos")
                rows = cursor.fetchall()


                # Adicional Estilo

                style = ttk.Style()
                style.configure("Treeview",
                background="silver",
                foreground="black",
                rowheight=50,
                rowwidth=170,
                fieldbackground="silver")
                
    #============Mudar cor quando for selecionado
                style.map('Treeview',
                background=[('selected', 'green')])


                Lista = ttk.Treeview(F3)
                Lista['columns'] = ("Nº", "Nome", "Pai", "Bilhete nº", "Curso", "Turno", "Contacto")
                Lista.place(x=490, y=70)


                #=========Formatar as Listas============#
                Lista.column("#0", width=0, stretch=NO)
                Lista.column("Nº", anchor=W, width=60)
                Lista.column("Nome", anchor=W, width=160)
                Lista.column("Pai", anchor=W, width=100)
                Lista.column("Bilhete nº", anchor=W, width=100)
                Lista.column("Curso", anchor=W, width=100)
                Lista.column("Turno", anchor=W, width=100)
                Lista.column("Contacto", anchor=W, width=100)


                Lista.heading("#0", text="", anchor=W)
                Lista.heading("Nº", text="Número", anchor=W)
                Lista.heading("Nome", text="Nome", anchor=W)
                Lista.heading("Pai", text="Filho de", anchor=W)
                Lista.heading("Bilhete nº", text="Bilhete nº", anchor=W)
                Lista.heading("Curso", text="Curso de", anchor=W)
                Lista.heading("Turno", text="Turno", anchor=W)
                Lista.heading("Contacto", text="Contacto", anchor=W)

                global count
                for row in rows:
                    Lista.insert(parent='', index='end', values=(row[0], row[1], row[2], row[4], row[12], row[13], row[7]))




            show()

            #==============================Local Para mostrar total de alunos no sistema====================================#

            def contar():
                con = mysql.connector.connect(host="localhost", user="root", password="", database="ITS")
                cursor =con.cursor()
                cursor.execute("select count(id) from alunos")
                rows = cursor.fetchall()
                for row in rows:
                    insrtDate = str(row  [0])
                    soma.insert(soma.size()+0, insrtDate)
                    con.close();


            soma = Listbox(F3,width="5", height="1", bd="0", bg="white", font="Arial 15", justify="center",  cursor="hand2")
            soma.place(x=630, y=600)

            contar()
            Total=Label(F3, text="Total De Alunos", font="Times 15", bg="white", fg="black")
            Total.place(x=490, y=600)

            data_atual = date.today()
            print(data_atual)

          

            def sair_do_F3():
                F3.destroy()

            Sair_F3 = Button(F3, text="Voltar", bd="0", bg="white", font="Arial 11", command=sair_do_F3).place(x=1165, y=40)


            Aluno_Frame1 = Frame(F3, height="2", width="1200", bg="skyblue")
            Aluno_Frame1.place(x=10, y=63)


            Nome=Label(F3, text="Nome",font="Arial 10", bg="white")
            Nome.place(x=10, y=120)
            
            Pai=Label(F3, text="Nome do Pai",font="Arial 10", bg="white")
            Pai.place(x=10, y=160)
            
            Mae=Label(F3, text="Nome da Mãe", font="Arial 10", bg="white")
            Mae.place(x=10, y=200)
            
            BI=Label(F3, text="Nº do BI", bg="white")
            BI.place(x=10, y=240)
            
            Email=Label(F3, text="E-mail", bg="white")
            Email.place(x=10, y=280)

            Nascimento=Label(F3, text="Data de Nascimento", bg="white")
            Nascimento.place(x=10, y=320)
            
            Tel=Label(F3, text="Nº  de Telefone", bg="white")
            Tel.place(x=10, y=360)

            Provincia=ttk.Combobox(F3, values=["Bengo","Benguela", "Bié","Cabinda","Kuando Kubango",
            "Kwanza Norte", "Kwanza Sul", "Cunene", "Huambo", "Huíla","Luanda","Lunda-Norte", "Lunda-Sul",
            "Malange", "Moxico", "Namibe", "Uige", "Zaire"], justify="center")
            Provincia.set("PROVÍNCIA")
            Provincia.place(x=10, y=410)

            Genero=ttk.Combobox(F3, values=["Masculino","Femenino"], justify="center", width="20")
            Genero.set("GENERO")
            Genero.place(x=260, y=410)

            Classe=ttk.Combobox(F3, values=["10ª Classe","11ª Classe", "12ª Classe", "13ª Classe"], justify="center")
            Classe.set("CLASSE")
            Classe.place(x=10, y=470)
            
            Ano_lectivo=ttk.Combobox(F3, values=["2022","2023", "2024", "2025", "2026", "2027", "2028", "2028", "2029", "2030"], justify="center")
            Ano_lectivo.set("ANO LECTIVO")
            Ano_lectivo.place(x=10, y=440)

            Curso=ttk.Combobox(F3, values=["Enfermagen","Analises Clinicas", "Farmácia"], justify="center")
            Curso.set("CURSO PRETENDIDO")
            Curso.place(x=260, y=440)

            Periodo=ttk.Combobox(F3, values=["Manhã","Tarde", "Noite"], justify="center")
            Periodo.set("PERÍODO")
            Periodo.place(x=260, y=470)

            #============================Entries================================#
            NomeEntry = ttk.Entry(F3, width="40", justify="center")
            NomeEntry.place(x=160, y=120)
            
            PaiEntry = ttk.Entry(F3, width="40", justify="center")
            PaiEntry.place(x=160, y=160)
            
            MaeEntry = ttk.Entry(F3, width="40", justify="center")
            MaeEntry.place(x=160, y=200)
            
            BiEntry = ttk.Entry(F3, width="40", justify="center")
            BiEntry.place(x=160, y=240)
            
            EmailEntry = ttk.Entry(F3, width="40", justify="center")
            EmailEntry.place(x=160, y=280)
            
            DataEntry = ttk.Entry(F3, width="40", justify="center")
            DataEntry.place(x=160, y=320)

            TelEntry = ttk.Entry(F3, width="40", justify="center")
            TelEntry.place(x=160, y=360)

#=====================Local para obter os dados=======================#

            ID = Label(F3, text="ID", bg="white")
            ID.place(x=10, y=570)

            ID_Entry = ttk.Entry(F3, width="20", justify="center")
            ID_Entry.place(x=35, y=570)




            eliminar=Button(F3, text="Eliminar", bg="#00513f",fg="white",  width="10", bd="1", activebackground="orange", cursor="hand2", command=Eliminar)
            eliminar.place(x=170, y=570)
            
            atualizar=Button(F3, text="Atualizar", bg="#00513f",fg="white",  width="10", bd="1", activebackground="orange", cursor="hand2", command=Atualizar_dados)
            atualizar.place(x=260, y=570)
            
            buscar=Button(F3, text="Pesquisar", bg="#00513f",fg="white",  width="10", bd="1", activebackground="orange", cursor="hand2", command=Obter)
            buscar.place(x=350, y=570)

            
           
        F2_TOP2 = Frame(F2, width="300", height="90", bg="oldlace", bd="2")
        F2_TOP2.place(x=330, y=70)
        Dados = Button(F2_TOP2, text="CONSULTAR\nALUNOS", bd="0", bg="oldlace", font="Arial 15", cursor="hand2", command=buscar_alunos)
        Dados.place(x=80, y=20)

#=======================================Local Para Lançar notas dos alunos=================#

        def mandar_notas():
           F3 = Frame(root, width="2000", height="1000").place(x=0, y=30)
           primeiro1=Label(F3, text="1º Trimestre", font="Arial 15")
           primeiro1.place(x=10, y=50)

           def enviar():
            Mac = MAC_entry.get();
            Npp = NPP_entry.get();
            Ntp = NPT_entry.get();
            media = (int(Mac) + int(Npp) + int(Ntp))/3
            print(media)
           
           Bi=Label(F3, text="Bi:", font="Times 10")
           Bi.place(x=10, y=90)
           
           Matematica=Label(F3, text="Matemática:", font="Times 10")
           Matematica.place(x=10, y=120)
           
           Fisica=Label(F3, text="Fisica:", font="Times 10")
           Fisica.place(x=10, y=150)
           
           Biologia=Label(F3, text="Biologia:", font="Times 10")
           Biologia.place(x=10, y=180)
           
           Etica=Label(F3, text="Ética:", font="Times 10")
           Etica.place(x=10, y=210)
           
           Inglês=Label(F3, text="Inglês:", font="Times 10")
           Inglês.place(x=10, y=240)
           
           Portugues=Label(F3, text="Portugues:", font="Times 10")
           Portugues.place(x=10, y=270)
           
           Anatomia=Label(F3, text="Anatomia:", font="Times 10")
           Anatomia.place(x=10, y=300)
           
           Fai=Label(F3, text="Fai:", font="Times 10")
           Fai.place(x=10, y=330)
           
           E_Fisica=Label(F3, text="E_Fisica:", font="Times 10")
           E_Fisica.place(x=10, y=360)
           
           Iec=Label(F3, text="Iec:", font="Times 10")
           Iec.place(x=10, y=389)
           
           Mac = Label(F3, text="MAC", font="Arial 12").place(x=10, y=460)

           Npp = Label(F3, text="NPP", font="Arial 12").place(x=110, y=460)

           Ntp = Label(F3, text="NPT", font="Arial 12").place(x=220, y=460)
           
           Informatica=Label(F3, text="Informática:", font="Times 10")
           Informatica.place(x=10, y=420)
           
           Bi_entry = ttk.Entry(F3, font="Times 10")
           Bi_entry.place(x=115, y=90)
           
           Matematica_entry=ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Matematica_entry.place(x=115, y=120)
           
           Fisica_entry = ttk.Entry(F3,font="Times 10", width="10", justify="center")
           Fisica_entry.place(x=115, y=150)
           
           Biologia_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Biologia_entry.place(x=115, y=180)
           
           Etica_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Etica_entry.place(x=115, y=210)
           
           Inglês_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Inglês_entry.place(x=115, y=240)
           
           Portugues_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Portugues_entry.place(x=115, y=270)
           
           Anatomia_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Anatomia_entry.place(x=115, y=300)
           
           Fai_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Fai_entry.place(x=115, y=330)
           
           E_Fisica_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           E_Fisica_entry.place(x=115, y=360)
           
           Iec_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Iec_entry.place(x=115, y=390)
           
           Informatica_entry = ttk.Entry(F3, font="Times 10", width="10", justify="center")
           Informatica_entry.place(x=115, y=420)

           MAC_entry = ttk.Entry(F3, font="Times 10", width="7", justify="center")
           MAC_entry.place(x=60, y=460)

           NPP_entry = ttk.Entry(F3, font="Times 10", width="7", justify="center")
           NPP_entry.place(x=150, y=460)

           NPT_entry = ttk.Entry(F3, font="Times 10", width="7", justify="center")
           NPT_entry.place(x=260, y=460)
           
           submeter_notas = Button(F3, text="Submeter", bd="0", bg="green", width="15", command=enviar).place(x=100, y=500)

          




        F2_TOP3 = Frame(F2, width="300", height="90", bg="oldlace", bd="2")
        F2_TOP3.place(x=10, y=220)
        Atribuir_Notas = Button(F2_TOP3, text="LANÇAMENTO DE NOTAS\nDOS ALUNOS", bd="0", bg="oldlace", font="Arial 15", cursor="hand2", command=mandar_notas)
        Atribuir_Notas.place(x=20, y=20)

        F2_TOP2 = Frame(F2, width="300", height="90", bg="oldlace", bd="2")
        F2_TOP2.place(x=330, y=220)
        Dados = Button(F2_TOP2, text="CONSULTAR NOTAS\nDOS ALUNOS", bd="0", bg="oldlace", font="Arial 15", cursor="hand2")
        Dados.place(x=60, y=20)
        

        #===============Texto na direita==================#
        Sobre_titulo = Label(F2, text="SCHOOL SYSTEM", bg="White", font="Arial 12")
        Sobre_titulo.place(x=650, y=70)
        linhao = Frame(F2, width="1000", height="2", bg="oldlace")
        linhao.place(x=650, y=100)

        texto1 = Message(F2, text="A SCHOOL SYSTEM é um software escolar desenvolvido para uso exclusivo do Instituto Técnico de Saúde\n nº 8060Com multiplas funcionalidades para um melhor um melhor ambiente de trabalho, este software\n não pode ser:", width="1000")
        texto1.place(x=650, y=120)

        texto2 = Message(F2, text="Cópiado, vendido ou mesmo redistribuido de acordo com a licensa do desenvolvedor, em caso de novas\n atualizações ou Má funcionamento do software entre em contacto com o desenvolvedor por favor!", width="1000")
        texto2.place(x=650, y=190)


        linha = Frame(F2, width="170", height="2", bg="#001721")
        linha.place(x=10, y=370)
        
        linha2 = Frame(F2, width="50", height="2", bg="orange")
        linha2.place(x=160, y=370)
            
        seguro = Label(F2,text="100% Seguro", bg="white")
        seguro.place(x=230, y=360)

    else:
        messagebox.showerror("Erro", "Palavra passe ou senha incorreta, tente novamente")



Login = Label(root, text="Fazer login", bg="white", fg="black", font="Arial 13")
Login.place(x=800, y=180)       

#Typing the entries
def on_enter(e):
    Nome.delete(0, 'end')

def on_leave(e):
    name = Nome.get()
    if name == '':
        Nome.insert(0, "Username")

Nome = ttk.Entry(root, width="40", justify="center")
Nome.place(x=800, y=220)
Nome.insert(0, 'Username')
Nome.bind('<FocusIn>', on_enter)
Nome.bind('<FocusOut>', on_leave)

def on_enter(e):
    Senha.delete(0, 'end')

def on_leave(e):
    name = Senha.get()
    if name == '':
        Senha.insert(0, "Password")


Senha= ttk.Entry(root, width="40", justify="center",show="*")
Senha.place(x=800, y=270)
Senha.insert(0, 'Password')
Senha.bind('<FocusIn>', on_enter)
Senha.bind('<FocusOut>', on_leave)

Entrar = Button(root, 
text="Entrar",
 bg="skyblue", 
 width="35", 
 bd="0", 
 cursor="hand2", command=logar)
Entrar.place(x=800, y=330)

Nova = Label(root, 
text="Não tem uma conta?", 
font="Times 10", 
bg="white")
Nova.place(x=850, y=360)

Conta_nova = Button(root, 
text="Criar", 
bg="white", 
fg="skyblue", 
bd="0", 
cursor="hand2", 
activebackground="white")
Conta_nova.place(x=965, y=360)

def nova_conta():
    Top = Toplevel()
    Top.title("Sign UP")
    Top.geometry("400x400+100+40")
    Top.resizable(False, False)
# Local para fazer cadastramento de professores






image71=Image.open("D:\\Projectos\\Sistema Escolar\\Images\\baixo.png")
image61=ImageTk.PhotoImage(image71)
Label41=Label(root,image=image61, bd="0", justify="center", bg="white")
Label41.place(x=900, y=500)


copyright = Label(root, text="© Copyright 2022, all rights reserveds!", bg="white").place(x=550, y=640)


root.title("Instituto Técnico de Saúde")
root["bg"]="white"
root.resizable(False, False)
root.geometry("1220x666+20+20")
root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# função para conectar a credencial de acesso ao Firebase, utilizando o arquivo json como chave de autenticação
def conexao_database():
    #cria a credencial necessária para acesso ao Firebase
    cred = credentials.Certificate(
        'C:\\Users\\Usuario\\Documents\\Rafael\\Projetos\\horta_rafa_said\\horta-rafa-said-firebase-adminsdk-986wi-98be8bb7af.json')
    #inicializa a conexão com o Firebase, utilizando a credencial e o endereço do Firebase
    firebase_admin.initialize_app(cred, {
    'databaseURL' : 'https://horta-rafa-said.firebaseio.com'})
#execução da função para conectar à database do Firebase
conexao_database()


# função para exibir a janela na qual serão inseridos os dados do calendário de jogos
def janela_cadastro():

    # fonte para usar nos ENTRY
    font = 'arial 20 bold'

    # janela de cadastro
    janela_cadastrar_especies = Toplevel(background='green')
    janela_cadastrar_especies.wm_iconbitmap('icon.ico')

    # janela para inserção de novas espécies na database
    janela_cadastrar_especies.title('Cadastro de nova espécie')

    # define os Labels na janela
    Label(janela_cadastrar_especies, text='Nome', font=font, bg='green', fg='white').grid(row=0)
    Label(janela_cadastrar_especies, text='Plantio', font=font, bg='green', fg='white').grid(row=1)
    Label(janela_cadastrar_especies, text='Colheita', font=font, bg='green', fg='white').grid(row=2)
    Label(janela_cadastrar_especies, text='Espaçamento', font=font, bg='green', fg='white').grid(row=3)
    Label(janela_cadastrar_especies, text='Água', font=font, bg='green', fg='white').grid(row=4)
    Label(janela_cadastrar_especies, text='Sol', font=font, bg='green', fg='white').grid(row=5)

    # ========== ENTRY ==========
    # formulário para inserção das informações sobre a espécie
    nome_especie_entry = Entry(janela_cadastrar_especies, font=font)
    plantio_entry = Entry(janela_cadastrar_especies, font=font)
    colheita_entry = Entry(janela_cadastrar_especies, font=font)
    espacamento_entry = Entry(janela_cadastrar_especies, font=font)
    agua_entry = Entry(janela_cadastrar_especies, font=font)
    sol_entry = Entry(janela_cadastrar_especies, font=font)

    # localiza as ENTRY, tem que ser separado para não retornar None
    '''The grid, pack and place functions of the Entry object and of all other widgets returns None. In python when you do a().b(), the result of the expression is whatever b() returns, therefore Entry(...).grid(...) will return None.'''
    nome_especie_entry.grid(row=0, column=1, padx=2, pady=4)
    plantio_entry.grid(row=1, column=1, padx=2, pady=4)
    colheita_entry.grid(row=2, column=1, padx=2, pady=4)
    espacamento_entry.grid(row=3, column=1, padx=2, pady=4)
    agua_entry.grid(row=4, column=1, padx=2, pady=4)
    sol_entry.grid(row=5, column=1, padx=2, pady=4)

    # função para adicionar novas espécies a database
    def adicionar_especie():
        messagebox.askquestion('Horta', 'Você tem certeza?')
        # Get a database reference to our Firebase database.
        ref = db.reference()
        # pega a child horta e armazena na variável posts_ref
        posts_ref = ref.child('horta')
        # push para colocar os dados no Firebase
        new_post = posts_ref.push()
        # cria um dicionário com os dados da espécie, usa o .get() para parsear a Entry para String
        dicionario_especie = {
            'nome': nome_especie_entry.get(),
            'plantio': plantio_entry.get(),
            'colheita': colheita_entry.get(),
            'espaçamento': espacamento_entry.get(),
            'agua': agua_entry.get(),
            'sol': sol_entry.get()
        }
        # posta os dados da partida no Firebase
        new_post.set(dicionario_especie)


    # botão para inserir os dados no Firebase
    btn_adicionar = Button(janela_cadastrar_especies, text='Adicionar', command=adicionar_especie, font=font, bg='white', fg='green').grid(row=6, column=1, sticky=N + W, padx=5, pady=4)


    # botão para fechar a janela
    btn_fechar = Button(janela_cadastrar_especies, text='Sair', command=janela_cadastrar_especies.destroy, font=font, bg='white', fg='green').grid(row=6, column=1, sticky=N + E, padx=5, pady=4)


# classe principal do programa
class Horta():
    def __init__(self):
        self.horta_window = Tk()
        self.horta_window.configure(background='green')
        self.horta_window.title('Horta | By Rafa Said')
        self.horta_window.resizable(False, False)
        self.horta_window.wm_iconbitmap('icon.ico')


        # ========== LABELS ==========
        Label(self.horta_window, text='HORTA RAFA, LEILA E SOFIA', width=25, bg='white', fg='green', font='arial 30 bold').grid(row=0, column=0, sticky=W, padx=10, pady=10)


        # ========== FUNÇÕES ==========
        # função para obter os registros das espécies cadastradas
        def obtendo_especies():
            dicionario_final = {}
            global lista_resultados
            lista_resultados = []
            # pega as keys (da child no Firebase) e separa o dicionário resultante em chave e valor
            for keys in db.reference('horta').get().items():
                # pega a posição 1 do dicionário anterior (que traz as informações sobre os resultados, e armazena na variável dados
                dados = keys[1]
                # desmembra o dicionário da variável dados em chave e valor
                for chave, valor in dados.items():
                    # obtém as informações dos resultados
                    if chave == 'agua':
                        agua = valor
                    if chave == 'colheita':
                        colheita = valor
                    if chave == 'espaçamento':
                        espacamento = valor
                    if chave == 'nome':
                        nome = valor
                    if chave == 'plantio':
                        plantio = valor
                    if chave == 'sol':
                        sol = valor
                        # adiciona os dados de resultados no dicionário dicionario_final
                        dicionario_final['Agua'] = agua
                        dicionario_final['Colheita'] = colheita
                        dicionario_final['Espaçamento'] = espacamento
                        dicionario_final['Nome'] = nome
                        dicionario_final['Plantio'] = plantio
                        dicionario_final['Sol'] = sol

                        # faz uma cópia do dicionário, para ter os dados de espécies cadastrada
                        copia = dicionario_final.copy()

                        # adiciona a cópia do dicionário na lista lista_resultados
                        lista_resultados.append(copia)

                        # limpa a cópia do dicionário para adicionar dados da próxima espécie
                        copia = {}


        # ========== TREE VIEW ==========
        # executa a função obtendo_especies() para obter os registros do Firebase
        obtendo_especies()

        #cria a TreeView
        self.tree = ttk.Treeview(self.horta_window, selectmode='browse',
                                 column=('column1', 'column2', 'column3', 'column4', 'column5', 'column6'), show='headings')

        fonte = 'arial 14 bold'
        #define as colunas da Treeview
        self.tree.column('column1', width=100, minwidth=100, stretch=YES, anchor=N)
        self.tree.heading('#1', text='Espécie')
        self.tree.column('column2', width=150, minwidth=150, stretch=YES, anchor=N)
        self.tree.heading('#2', text='Plantio')
        self.tree.column('column3', width=150, minwidth=150, stretch=YES, anchor=N)
        self.tree.heading('#3', text='Colheita')
        self.tree.column('column4', width=120, minwidth=120, stretch=YES, anchor=N)
        self.tree.heading('#4', text='Espaçamento (cm)')
        self.tree.column('column5', width=80, minwidth=80, stretch=YES, anchor=N)
        self.tree.heading('#5', text='Água')
        self.tree.column('column6', width=80, minwidth=80, stretch=YES, anchor=N)
        self.tree.heading('#6', text='Sol')

        # insere os dados do Firesabe na TreeView
        for cadastro in lista_resultados:
            self.tree.insert('',END, values=(cadastro['Nome'], cadastro['Plantio'], cadastro['Colheita'], cadastro['Espaçamento'], cadastro['Agua'], cadastro['Sol']))

        self.tree.grid(row=1, column=0, padx=9, pady=9, sticky=W + E, columnspan=4)
        self.tree.tag_configure('1', background='ivory')
        self.tree.tag_configure('2', background='ivory')
        self.tree.tag_configure('3', background='ivory')
        self.tree.tag_configure('4', background='ivory')
        self.tree.tag_configure('5', background='ivory')
        self.tree.tag_configure('6', background='ivory')


        #ToDo: função para deletar e para atualizar registros

        # ========= BUTTON ==========
        self.cadastrar_btn = Button(self.horta_window, text='CADASTRAR', width=12, bg='white', fg='green', font='arial 12 bold', command=janela_cadastro).grid(row=3, column=0, sticky=N, padx=5, pady=5)

        self.deletar_btn = Button(self.horta_window, text='DELETAR', width=12, bg='white', fg='green', font='arial 12 bold').grid(row=4, column=0, sticky=N, padx=5, pady=5)


        # ========== EXECUÇÃO DA JANELA ==========
        self.horta_window.mainloop()


try:
    Horta()
except:
    raise Exception('A janela não pode ser criada!')
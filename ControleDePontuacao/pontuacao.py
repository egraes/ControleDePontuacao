
import sqlite3
from PyQt5 import uic,QtWidgets		#carrega Biblioteca do Qtdesign			

connection = sqlite3.connect('jogos.db')
c = connection.cursor()

def create_table():
	
	c.execute('CREATE TABLE IF NOT EXISTS dados (jogo integer, placar integer)')
create_table()


def funcao_cadJogo():							#primeiros testes de cadastramento
	
	jogos     = tela_cadJogo.lineEdit.text()	# variavel recebe jogo da   Tela_cadJogo
	placar   = tela_cadJogo.lineEdit_2.text()	# variavel recebe pontos da Tela_cadJogo
	
	comando = "INSERT INTO dados (jogo,placar) VALUES($1,$2)"
	parametros = (jogos,placar)
	c.execute(comando,parametros)								# insere jogo e placar
	
	tela_cadJogo.lineEdit.setText('')							# limpa jogo Tela_cadJogo	
	tela_cadJogo.lineEdit_2.setText('')							# limpa pontos Tela_cadJogo
	
	connection.commit()											# atualiza dados no DB
	
	#----TESTE DE LEITURA DB-----
	
	comando = "SELECT * FROM dados"
	c.execute(comando)
	dadosdb = c.fetchall()
	
	dados = list()
	
	for i in dadosdb:
		dados.append(i)
	print(dados)
	
	
	
	
	
	
def funcao_delJogo():				#testa botao Deletar Jogos da tela_principal

	print ("Cheguei Deletar !!!")
	
def funcao_consJogo():				#testa botao Consultar Jogos da tela_principal

	print ("Cheguei Consulta !!!")
	



# Qt Designer app, load da tela Principal e teste funcoes dos Botoes

app=QtWidgets.QApplication([])								#app do QtDesigner				


tela_principal = uic.loadUi('tela1.ui')					 	#load tela Principal        
tela_cadJogo   = uic.loadUi('tela_cadJogo.ui')
# Botoes Tela Principal
tela_principal.btn_cadJogo.clicked.connect(tela_cadJogo.show)# Abre Tela cadastro
tela_principal.btn_consJogo.clicked.connect(funcao_consJogo)#(TESTE )prx ver. Abre Tela 
tela_principal.btn_delJogo.clicked.connect(funcao_delJogo)	#(TESTE )prx ver. Abre Tela 
tela_principal.btn_sair.clicked.connect(exit)			    # Encerra aplicaçao

# Botoes Tela de Cadastro
tela_cadJogo.btn_cadJogo.clicked.connect(funcao_cadJogo)	#botao Cadastrar->funcao_cadJogo
tela_cadJogo.btn_sair.clicked.connect(tela_cadJogo.close)	#botao fecha janeja cadastro 
tela_principal.show()										#Exibe tela Principal

app.exec()													#Exec. app gerado por QtDesigner
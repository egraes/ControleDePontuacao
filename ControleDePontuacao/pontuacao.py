
import sqlite3						# importa biblioteca do SQLite3
from PyQt5 import uic,QtWidgets		#carrega Biblioteca do Qtdesign			

#Cria banco se ainda não existir,tabela e conexao com o banco

connection = sqlite3.connect('jogos.db')
c = connection.cursor()

def create_table(): 							#cria tabela
	
	c.execute('CREATE TABLE IF NOT EXISTS dados (ID INTEGER PRIMARY KEY AUTOINCREMENT, jogo integer, placar integer, minTemp integer, maxTemp integer, recMin integer, recMax integer)')
create_table()

# funcao de cadastro de jogo

def funcao_cadJogo():		
	
	dados = list()								# armazena ultimo registro do banco	
	minTemp = 0									# Variavel placar minimo da temporada
	maxTemp = 0									# Variavel placar minimo da temporada
	
	somaRecMin = 0								#contador de quebra recorde min
	somaRecMax = 0								#contador de quebra recorde Max
	
	# Seleciona ultimo registro do banco para comparar com o novo cadastro
	
	comando = 'Select * from dados WHERE ID = (SELECT MAX(ID) FROM dados)'
	c.execute(comando)				
	dadosdb = c.fetchall()			
	for i in range(0,len(dadosdb)):
		dados.append(dadosdb[i])
	
	jogos     = tela_cadJogo.lineEdit.text()	# variavel recebe jogo da   Tela_cadJogo
	placar   = tela_cadJogo.lineEdit_2.text()	# variavel recebe pontos da Tela_cadJogo
	
	if not placar or int(placar) > 1000	or int(placar) <0:				#verifica se placar é nulo,menor que 1000 ou menor 0
		tela_cadJogo.label_4.setText('Digite um num entre 1-1000 !!!')
		return
	
		
		
		
	tela_cadJogo.lineEdit.setText('')			# limpa  campo jogo Tela_cadJogo	
	tela_cadJogo.lineEdit_2.setText('')			# limpa  campo pontos Tela_cadJogo
	tela_cadJogo.label_4.setText('')
						
	# Se banco estiver vazio, cria o primeiro registro com placar atual
	if not dadosdb:
		
		minTemp = int(placar) 					# minimo da temporada igual ultimo placar
		maxTemp = int(placar)					# maximo da temporada igual ultimo placar
		somaRecMin = 0							# quebra de recordes minimos zerado
		somaRecMax = 0							# quebra de recordes maximos zerado
		
	
    #Se banco não esta vazio, compara novo placar com Max e Minimo do ultimo registro 
	else:
		somaRecMin = int(dados[0][5])			# pega ultima posicao de cada variavel
		somaRecMax = int(dados[0][6])			# do ultimo registro do Db
		minTemp    = int(dados[0][3])
		maxTemp    = int(dados[0][4])
		
		if int(placar) < dados[0][2]:
			minTemp = int(placar)
			somaRecMin=somaRecMin+1			     # se placar for menor que Min da temporada/
												 # / soma 1 ao contador Min 
		if int(placar) > dados[0][4]:
			maxTemp = int(placar)
			somaRecMax = somaRecMax+1       	 # se placar for maior que Max da temporada/
												 #/ soma 1 ao contador Max 
			
		
		
	#Cria novo registro e atualiza o banco
	
	comando = "INSERT INTO dados (jogo,placar,minTemp,maxTemp,recMin,recMax) VALUES($1,$2,$3,$4,$5,$6)"
	parametros=(jogos,placar,minTemp,maxTemp,somaRecMin,somaRecMax)
	c.execute(comando,parametros)
	
	connection.commit()								# atualiza dados no DB
	
	
	# funcao de deletar jogo
	
def funcao_delJogo():								# Deletar Jogos, botao da tela_principal

	parametros=list()								#armazena parametro do SELECT		
	
	jogo = str(tela_delJogo.lineEdit.text())		#salva jogo da tela 
	parametros.append(jogo)
	comando = " DELETE FROM dados WHERE jogo = $1"	#SQL para remover o registro
	
	c.execute(comando,parametros)					#executa SQL
	
	tela_delJogo.lineEdit.setText('')				#limpa campo tela deletar
	
	connection.commit()								#atualiza o banco

def funcao_delTodos():								#deleta todos os registros

	comando = " DELETE FROM dados"					#SQL para remover o registro
	c.execute(comando)								#executa SQL
	connection.commit()								#atualiza o banco
	tela_delTodos.close()							#fecha janela deletar todos
	tela_delJogo.close()							#fecha janela deletar jogo
	
def funcao_consJogo():								# carrega todos os registros e dispoe na tabela

	comando = "SELECT * FROM dados"					#SQL seleciona todos os registros
	c.execute(comando)								#executa SQL
	dadosdb = c.fetchall()							#salva dados em dadosdb
	
	
	tela_consJogo.show()											#exibe tela de consulta
	tela_consJogo.label.setText('Consulta de Todos os Jogos')		#seta o titulo da janela
	tela_consJogo.tableWidget.setRowCount(len(dadosdb))				#define numero de linha pelo num de registros
	tela_consJogo.tableWidget.setColumnCount(6)						#define numero de colunas da tabela
	
	for i in range(0,len(dadosdb)):									#linhas do db
		for j in range(0,6):										#colunas do db
			tela_consJogo.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dadosdb[i][j+1]))) #dispoe Lin/col na Tabela
	



# Qt Designer app, load da tela Principal e teste funcoes dos Botoes

app=QtWidgets.QApplication([])									#app do QtDesigner				


tela_principal = uic.loadUi('tela1.ui')					 		#load tela Principal        
tela_cadJogo   = uic.loadUi('tela_cadJogo.ui')					#load tela de cadastro
tela_delJogo   = uic.loadUi('tela_delJogo.ui')					#load tela deletar
tela_consJogo  = uic.loadUi('telaConsulta.ui')					#load tela consulta
tela_delTodos  = uic.loadUi('tela_Deltudo.ui')					#load tela deletar tudo
# Botoes Tela Principal
tela_principal.btn_cadJogo.clicked.connect(tela_cadJogo.show)	# Abre Tela cadastro
tela_principal.btn_consJogo.clicked.connect(funcao_consJogo)	#(TESTE )prx ver. Abre Tela 
tela_principal.btn_delJogo.clicked.connect(tela_delJogo.show)	#Abre Tela deletar
tela_principal.btn_sair.clicked.connect(exit)			   		# Encerra aplicaçao

# Botoes Tela de Cadastro
tela_cadJogo.btn_cadJogo.clicked.connect(funcao_cadJogo)		#botao Cadastrar->funcao_cadJogo
tela_cadJogo.btn_sair.clicked.connect(tela_cadJogo.close)		#botao fecha janeja cadastro 
tela_principal.show()											#Exibe tela Principal

# Botoes Tela deletar
tela_delJogo.btn_delJogo.clicked.connect(funcao_delJogo)		#botao Deletar->funcao_delJogo  
tela_delJogo.btn_sair.clicked.connect(tela_delJogo.close)		#botao Sair
tela_delJogo.deltodos.clicked.connect(tela_delTodos.show)		#botao exibe janela deletar todos

# Botoes Tela delTodos
tela_delTodos.deletar.clicked.connect(funcao_delTodos)			#botao Deletar tuso -> funcao deletar tudo
tela_delTodos.btn_cancelar.clicked.connect(tela_delTodos.close)	#botao Cancelar janela deletar tudo

# Botao sair tela consulta
tela_consJogo.btn_sair.clicked.connect(tela_consJogo.close)		#botao sair da tela de consulta

app.exec()													#Exec. app gerado por QtDesigner
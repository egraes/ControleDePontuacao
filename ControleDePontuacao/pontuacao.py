
import sqlite3
from PyQt5 import uic,QtWidgets		#carrega Biblioteca do Qtdesign			

connection = sqlite3.connect('jogos.db')
c = connection.cursor()

def create_table():
	
	c.execute('CREATE TABLE IF NOT EXISTS dados (jogo integer, placar integer, minTemp integer, maxTemp integer, recMin integer, recMax integer)')
create_table()


def funcao_cadJogo():							#primeiros testes de cadastramento
	
	dados = list()								# armazena ultimo registro do banco	
	minTemp = 0									# Variavel placar minimo da temporada
	maxTemp = 0									# Variavel placar minimo da temporada
	
	somaRecMin = 0								#contador de quebra recorde min
	somaRecMax = 0								#contador de quebra recorde Max
	
	jogos     = tela_cadJogo.lineEdit.text()	# variavel recebe jogo da   Tela_cadJogo
	placar   = tela_cadJogo.lineEdit_2.text()	# variavel recebe pontos da Tela_cadJogo
	
							
	
	tela_cadJogo.lineEdit.setText('')			# limpa  campo jogo Tela_cadJogo	
	tela_cadJogo.lineEdit_2.setText('')			# limpa  campo pontos Tela_cadJogo
	
		
	# Seleciona ultimo registro do banco para comparar com o cadastro
	
	comando = 'Select * from dados WHERE ID = (SELECT MAX(ID) FROM dados)'
	c.execute(comando)				
	dadosdb = c.fetchall()			
	for i in range(0,len(dadosdb)):
		dados.append(dadosdb[i])
						
	# Se banco estiver vazio, cria o primeiro registro com placar atual
	if not dadosdb:
		
		minTemp = int(placar) 					# minimo da temporada igual ultimo placar
		maxTemp = int(placar)					# maximo da temporada igual ultimo placar
		somaRecMin = 0							# quebra de recordes minimos zerado
		somaRecMax = 0							# quebra de recordes maximos zerado
		
	
    #Se banco não esta vazio, compara novo placar com Max e Minimo do ultimo registro 
	else:
		
		if int(placar) <= dados[0][2]:
			minTemp = int(placar)
			maxTemp = dados[0][4]
			somaRecMin=somaRecMin+1				 # se placar for menor que Min da temporada/
			somaRecMax=dados[0][6]				 # / soma 1 ao contador Min e atualiza Min
		
		if int(placar) >= dados[0][4]:
			maxTemp = int(placar)
			minTemp = dados[0][3]				 # se placar for maior que Max da temporada/
			somaRecMin = dados[0][5]			 #/ soma 1 ao contador Max e atualiza Max
			somaRecMax = somaRecMax+1
	
	#Cria novo registro e atualiza o banco
	
	comando = "INSERT INTO dados (jogo,placar,minTemp,maxTemp,recMin,recMax) VALUES($1,$2,$3,$4,$5,$6)"
	parametros=(jogos,placar,minTemp,maxTemp,somaRecMin,somaRecMax)
	c.execute(comando,parametros)
	
	connection.commit()											# atualiza dados no DB
	
	
	
	
	
	
	
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
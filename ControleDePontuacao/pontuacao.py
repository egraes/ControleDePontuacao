from PyQt5 import uic,QtWidgets		#carrega Biblioteca do Qtdesign			


def funcao_cadJogo():				#testa botao Cadastrar Jogos da tela_principal
	
	print ("Cheguei Cadastro !!!")
	
def funcao_delJogo():				#testa botao Deletar Jogos da tela_principal

	print ("Cheguei Deletar !!!")
	
def funcao_consJogo():				#testa botao Consultar Jogos da tela_principal

	print ("Cheguei Consulta !!!")
	



# Qt Designer app, load da tela Principal e teste funcoes dos Botoes

app=QtWidgets.QApplication([])								#app do QtDesigner				


tela_principal = uic.loadUi('tela1.ui')					 	#load tela Principal        

# Botoes Tela Principal
tela_principal.btn_cadJogo.clicked.connect(funcao_cadJogo)	#(TESTE )prx ver. Abre Tela 
tela_principal.btn_consJogo.clicked.connect(funcao_consJogo)#(TESTE )prx ver. Abre Tela 
tela_principal.btn_delJogo.clicked.connect(funcao_delJogo)	#(TESTE )prx ver. Abre Tela 
tela_principal.btn_sair.clicked.connect(exit)			    # Encerra aplicaçao

										
tela_principal.show()										#Exibe tela Principal

app.exec()													#Exec. app gerado por QtDesigner
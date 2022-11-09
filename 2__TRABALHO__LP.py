listaregistros = []
regis = []
registros=0
u=1
print("----------SÓ PODERÁ SER CADASTRADO ATÉ CINCO REGISTROS!-----------")
i=0
x=1
while i!=5:
	print("\n1- Cadastro")
	print("2- Ler")
	print("3- Deletar")
	print("4- Atualizar")
	print("5- Sair")
	t= int( input("Digite a sua opção: "))
	if t==1:
		registros = int(input("Digite a quantidade de registros: "))
		regis.append(registros)
		cal = sum(regis)
		d = sum(regis)
		if cal <= 5 :
			for a in range(registros):
				print("\nCADASTRO N° %d"%x)
				x=x+1
				nome = (input("Nome: "))
				endereco = (input("Endereço: "))
				celular = (input("Celular: "))
				cpf = (input("CPF: "))
				email = (input("E-mail: "))
				confemail = (input("Confirme seu e-mail: "))
				if confemail != email:
					print("E-mail incorreto.")
					confemail = input("Digite novamente seu e-mail: ")
					if confemail == email:
						print("E-mail correto.")
			
						senha= (input ("Senha : "))
						confsenha= (input ("Confirma sua senha : "))
						if confsenha != senha:
							print("Senha incorreta : ")
							confsenha= (input ("Digite novamente sua senha: "))
						else :
							print("Senha correta.")
					else :
						print('E-mail incorreto\nVoltando ao MENU')
				else :
					print("E-mail correto.")
			
					senha= (input ("Senha : "))
					confsenha= (input ("Confirma sua senha : "))
					if confsenha != senha:
						print("Senha incorreta : ")
						confsenha= (input ("Digite novamente sua senha: "))
					else:
						print("\nDeseja confirmar seus dados? ")
						print("1- Sim")
						print("2- Não")
						s= int(input("Digite sua opção: "))
						if s==1:
							print("\nSeus dados estão confirmados no sistema. ")
				
				listaregistros.append(nome)
				u=u+1
				listaregistros.append(endereco)
				u=u+1
				listaregistros.append(celular)
				u=u+1
				listaregistros.append(cpf)
				u=u+1
				listaregistros.append(confemail)
				u=u+1
				listaregistros.append(confsenha)
				u=u+1
		else :
		    print("----------VALOR INVÁDIDO----------\nDIGITE UM NÚMERO ENTRE 1 Á 5\n")
		    if (regis[0]+regis[1]) > 5 : 
		    	del regis[1]
		    	calr= 5 - (sum(regis))
		    	print('Você só tem mais %d possibilidades de cadastro'%calr)
		    elif (regis[0]+regis[1]) > 5 and (regis[0]) == 5 :
		    	print('Já atingiu o máximo de cadastro')
		    elif (regis[0]+regis[1]+regis[2]) > 5 and (regis[0]+regis[1]) == 5 :
		    	print('Já atingiu o máximo de cadastro')
		    elif (regis[0]+regis[1]) < 5 and (regis[0]+regis[1]+regis[2]) > 5 :
		    	del regis[2]
		    	calr= 5 - (sum(regis))
		    	print('Você só tem mais %d possibilidades de cadastro'%calr)
		    elif (regis[0]+regis[1]+regis[2]+regis[3]) > 5 and (regis[0]+regis[1]+regis[2]) == 5 :
		    	print('Já atingiu o máximo de cadastro')
		    elif (regis[0]+regis[1]+regis[2]) < 5 and (regis[0]+regis[1]+regis[2]+regis[3]) > 5 :
		    	del regis[3]
		    	soma=(sum(regis))
		    	if soma == 3 :
		        	print('Você só tem mais 2 possibilidades de cadastro')
		    	if soma == 4 :
		        	print('Você só tem mais 1 possibilidades de cadastro')
		    elif (regis[0]+regis[1]+regis[2]+regis[3]) < 5 and (regis[0]+regis[1]+regis[2]+reg[3]+regis[4]) > 5:
		    	del regis[4]
		    	print('Você só tem mais 1 possibilidades de cadastro')
		    elif (regis[0]+regis[1]+regis[2]+regis[3]) > 5 and (regis[0]+regis[1]+regis[2]) == 5 :
		    	print('Já atingiu o máximo de cadastro')
		    else :
		    	print('Já atingiu o máximo de cadastro')
	elif t==2:
		d = sum(regis)
		if d > 0  :
		    print("\n*CADASTRO 1")
		    print("*CADASTRO 2")
		    print("*CADASTRO 3")
		    print("*CADASTRO 4")
		    print("*CADASTRO 5")
		    c = int(input("Qual opção você deseja ver? "))
		    if c==1:
			    print('\nNome: ', listaregistros[0])
			    print("Endereço: ", listaregistros[1])
			    print("Celular: ", listaregistros[2])
			    print("CPF: ", listaregistros[3])
			    print("E-mail: ", listaregistros[4])
			    print("Senha: ", listaregistros[5])
		    elif c==2:
			    if registros>=2 and registros<6:
				    print("\nNome: ", listaregistros[6])
				    print("Endereço: ", listaregistros[7])
				    print("Celular: ", listaregistros[8])
				    print("CPF: ", listaregistros[9])
				    print("E-mail: ", listaregistros[10])
				    print("Senha: ", listaregistros[11])
			    else:
				    print("NÃO FOI CADASTRADO NENHUM REGISTRO")
		    elif c==3:
			    if registros>=3 and registros<6:
				    print("\nNome: ", listaregistros[12])
				    print("Endereço: ", listaregistros[13])
				    print("Celular: ", listaregistros[14])
				    print("CPF: ", listaregistros[15])
				    print("E-mail: ", listaregistros[16])
				    print("Senha: ", listaregistros[17])
			    else:
				    print("NÃO FOI CADASTRADO NENHUM REGISTRO")
		    elif c==4:
			    if registros>=4 and registros<6:
				    print("\nNome: ", listaregistros[18])
				    print("Endereço: ", listaregistros[19])
				    print("Celular: ", listaregistros[20])
				    print("CPF: ", listaregistros[21])
				    print("E-mail: ", listaregistros[22])
				    print("Senha: ", listaregistros[23])
			    else:
				    print("NÃO FOI CADASTRADO NENHUM REGISTRO")
		    elif c==5:
			    if registros>=5 and registros<6:
				    print("\nNome: ", listaregistros[24])
				    print("Endereço: ", listaregistros[25])
				    print("Celular: ", listaregistros[26])
				    print("CPF: ", listaregistros[27])
				    print("E-mail: ", listaregistros[28])
				    print("Senha: ", listaregistros[29])
			    else:
				    print("NÃO FOI CADASTRADO NENHUM REGISTRO")

	elif t==3:
		d=sum(regis)
		if d == 1 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		elif d == 2 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		elif d == 3 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		    print("\nCADASTRO 3:")
		    print("Nome: ", listaregistros[12])
		    print("Endereço:",listaregistros[13])
		    print("Celular: ",listaregistros[14])
		    print("CPF: ",listaregistros[15])
		    print("E-mail: ",listaregistros[16])
		    print("Senha: ",listaregistros[17])
		elif d == 4 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		    print("\nCADASTRO 3:")
		    print("Nome: ", listaregistros[12])
		    print("Endereço:",listaregistros[13])
		    print("Celular: ",listaregistros[14])
		    print("CPF: ",listaregistros[15])
		    print("E-mail: ",listaregistros[16])
		    print("Senha: ",listaregistros[17])
		    print("\nCADASTRO 4:")
		    print("Nome: ", listaregistros[18])
		    print("Endereço:",listaregistros[19])
		    print("Celular: ",listaregistros[20])
		    print("CPF: ",listaregistros[21])
		    print("E-mail: ",listaregistros[22])
		    print("Senha: ",listaregistros[23])
		elif d == 5 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		    print("\nCADASTRO 3:")
		    print("Nome: ", listaregistros[12])
		    print("Endereço:",listaregistros[13])
		    print("Celular: ",listaregistros[14])
		    print("CPF: ",listaregistros[15])
		    print("E-mail: ",listaregistros[16])
		    print("Senha: ",listaregistros[17])
		    print("\nCADASTRO 4:")
		    print("Nome: ", listaregistros[18])
		    print("Endereço:",listaregistros[19])
		    print("Celular: ",listaregistros[20])
		    print("CPF: ",listaregistros[21])
		    print("E-mail: ",listaregistros[22])
		    print("Senha: ",listaregistros[23])
		    print("\nCADASTRO 5:")
		    print("Nome: ", listaregistros[24])
		    print("Endereço:",listaregistros[25])
		    print("Celular: ",listaregistros[26])
		    print("CPF: ",listaregistros[27])
		    print("E-mail: ",listaregistros[28])
		    print("Senha: ",listaregistros[29])
		else :
		    print('Sistema sem dados')
		d=sum(regis)
		if d > 0 and d < 6 :
		    print("Qual cadastro você quer deletar? ")
		    print("1- CADASTRO 1")
		    print("2- CADASTRO 2")
		    print("3- CADASTRO 3")
		    print("4- CADASTRO 4")
		    print("5- CADASTRO 5")
		    print("6- TODOS OS CADASTROS")
		
		    v = int(input("\nDigite a sua opção: "))
		
		    if v == 1 :
			    del listaregistros[5]
			    del listaregistros[4] 
			    del listaregistros[3]
			    del listaregistros[2]
			    del listaregistros[1]
			    del listaregistros[0]
			    if regis[0] > 0 :
				    del regis[0]
				    registros=registros-1
				    x=x-1
				    print("\n------CADASTRO 1 DELETADO:------ ")
				    print("Nova vaga de cadastro aberta")
		
		    elif v == 2 : 
			    del listaregistros[11] 
			    del listaregistros[10]
			    del listaregistros[9]
			    del listaregistros[8]
			    del listaregistros[7]
			    del listaregistros[6]
			    if regis[0] > 0 :
				    regis[0]=regis[0]-1
				    registros=registros-1
				    x=x-1
				    print("\n------CADASTRO 2 DELETADO:------ ")
				    print("Nova vaga de cadastro aberta")
		    elif v == 3 :
			    del listaregistros[17]
			    del listaregistros[16]
			    del listaregistros[15]
			    del listaregistros[14]
			    del listaregistros[13]
			    del listaregistros[12]
			    if regis[0] > 0 :
				    regis[0]=regis[0]-1
				    registros=registros-1
				    x=x-1
				    print("\n------CADASTRO 3 DELETADO:------ ")
				    print("Nova vaga de cadastro aberta")
		    elif v == 4 :
			    del listaregistros[23]
			    del listaregistros[22]
			    del listaregistros[21]
			    del listaregistros[20]
			    del listaregistros[19]
			    del listaregistros[18]
			    if regis[0] > 0 :
				    regis[0]=regis[0]-1
				    registros=registros-1
				    x=x-1
				    print("\n------CADASTRO 4 DELETADO:------ ")
				    print("Nova vaga de cadastro aberta")
		    elif v == 5 :
			    del listaregistros[29]
			    del listaregistros[28]
			    del listaregistros[27]
			    del listaregistros[26]
			    del listaregistros[25]
			    del listaregistros[24]
			    if regis[0] > 0 :
				    regis[0]=regis[0]-1
				    registros=registros-1
				    x=x-1
				    print("\n------CADASTRO 5 DELETADO:------ ")
				    print("Nova vaga de cadastro aberta")
		    elif v == 6 :
			    if cal == 1:
				    del listaregistros[5]
				    del listaregistros[4] 
				    del listaregistros[3]
				    del listaregistros[2]
				    del listaregistros[1]
				    del listaregistros[0]
				    del regis[0]
				    registros=registros-1
				    x=1
			    elif cal == 2:
				    del listaregistros[11] 
				    del listaregistros[10]
				    del listaregistros[9]
				    del listaregistros[8]
				    del listaregistros[7]
				    del listaregistros[6]
				    del listaregistros[5]
				    del listaregistros[4] 
				    del listaregistros[3]
				    del listaregistros[2]
				    del listaregistros[1]
				    del listaregistros[0]
				    obs= len(regis)  
				    if obs == 1 :
				        del regis[0]
				        registros=registros-2
				        x=1
				        print('\TODOS OS DADOS EXISTENTES DELETADOS')
				    else :
					    del regis[0:1]
					    registros=registros-2
					    x=1
					    print('\TODOS OS DADOS EXISTENTES DELETADOS')
			    elif cal == 3 :
			        del listaregistros[17]
			        del listaregistros[16]
			        del listaregistros[15]
			        del listaregistros[14]
			        del listaregistros[13]
			        del listaregistros[12]
			        del listaregistros[11] 
			        del listaregistros[10]
			        del listaregistros[9]
			        del listaregistros[8]
			        del listaregistros[7]
			        del listaregistros[6]
			        del listaregistros[5]
			        del listaregistros[4] 
			        del listaregistros[3]
			        del listaregistros[2]
			        del listaregistros[1]
			        del listaregistros[0]
			        obs= len(regis)
			        if obs == 1 :
			           del regis[0]
			           registros=registros-3
			           x=1
			           print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        elif obs == 2 :
			       	    del regis[0:1]
			       	    registros=registros-3
			       	    x=1
			       	    print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        else :
			            del regis[0:1:2]
			            registros=registros-3
			            x=1
			            print('\TODOS OS DADOS EXISTENTES DELETADOS')
			    elif cal == 4 :
			        del listaregistros[23]
			        del listaregistros[22]
			        del listaregistros[21]
			        del listaregistros[20]
			        del listaregistros[19]
			        del listaregistros[18]
			        del listaregistros[17]
			        del listaregistros[16]
			        del listaregistros[15]
			        del listaregistros[14]
			        del listaregistros[13]
			        del listaregistros[12]
			        del listaregistros[11]
			        del listaregistros[10]
			        del listaregistros[9]
			        del listaregistros[8]
			        del listaregistros[7]
			        del listaregistros[6]
			        del listaregistros[5]
			        del listaregistros[4] 
			        del listaregistros[3]
			        del listaregistros[2]
			        del listaregistros[1]
			        del listaregistros[0]
			        obs= len(regis)
			        if obs == 1 :
			            del regis[0]
			            registros=registros-4
			            x=1
			            print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        elif obs == 2 :
			    	    del regis[0:1]
			    	    registros=registros-4
			    	    x=1
			    	    print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        elif obs == 3 :
			            del regis[0:1:2]
			            registros=registros-4
			            x=1
			            print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        else :
			    	    del regis[0:1]
			    	    del regis[2:3]
			    	    registros=registros-4
			    	    x=1
			    	    print('\TODOS OS DADOS EXISTENTES DELETADOS')
			    elif cal == 5 :
			        del listaregistros[29]
			        del listaregistros[28]
			        del listaregistros[27]
			        del listaregistros[26]
			        del listaregistros[25]
			        del listaregistros[24]
			        del listaregistros[23]
			        del listaregistros[22]
			        del listaregistros[21]
			        del listaregistros[20]
			        del listaregistros[19]
			        del listaregistros[18]
			        del listaregistros[17]
			        del listaregistros[16]
			        del listaregistros[15]
			        del listaregistros[14]
			        del listaregistros[13]
			        del listaregistros[12]
			        del listaregistros[11]
			        del listaregistros[10]
			        del listaregistros[9]
			        del listaregistros[8]
			        del listaregistros[7]
			        del listaregistros[6]
			        del listaregistros[5]
			        del listaregistros[4] 
			        del listaregistros[3]
			        del listaregistros[2]
			        del listaregistros[1]
			        del listaregistros[0]
			        obs= len(regis)
			        if obs == 1 :
			    	    del regis[0]
			    	    registros=registros-5
			    	    x=1
			    	    print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        elif obs == 2 :
			            del regis[0:1]
			            registros=registros-5
			            x=1
			            print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        elif obs == 3 :
			    	    del regis[0:1:2]
			    	    registros=registros-5
			    	    x=1
			    	    print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        elif obs == 4 :
			            del regis[0:1]
			            del regis[2:3]
			            registros=regustros-5
			            x=1
			            print('\TODOS OS DADOS EXISTENTES DELETADOS')
			        else :
			            del regis[0]
			            del regis[1]
			            del regis[2]
			            del regis[3]
			            del regis[4]
			            registros=registros-5
			            x=1
			            print('\TODOS OS DADOS EXISTENTES DELETADOS')
			    else :
				    print(' ')
		    else:
			    print(' ')
		else:
		    print(' ')
	elif t == 4:
		cal= sum(regis)
		if cal == 1 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		elif cal == 2 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		elif cal == 3 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		    print("\nCADASTRO 3:")
		    print("Nome: ", listaregistros[12])
		    print("Endereço:",listaregistros[13])
		    print("Celular: ",listaregistros[14])
		    print("CPF: ",listaregistros[15])
		    print("E-mail: ",listaregistros[16])
		    print("Senha: ",listaregistros[17])
		elif cal == 4 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		    print("\nCADASTRO 3:")
		    print("Nome: ", listaregistros[12])
		    print("Endereço:",listaregistros[13])
		    print("Celular: ",listaregistros[14])
		    print("CPF: ",listaregistros[15])
		    print("E-mail: ",listaregistros[16])
		    print("Senha: ",listaregistros[17])
		    print("\nCADASTRO 4:")
		    print("Nome: ", listaregistros[18])
		    print("Endereço:",listaregistros[19])
		    print("Celular: ",listaregistros[20])
		    print("CPF: ",listaregistros[21])
		    print("E-mail: ",listaregistros[22])
		    print("Senha: ",listaregistros[23])
		elif cal == 5 :
		    print("----------DADOS DOS REGISTROS-----------")
		    print("\nCADASTRO 1:")
		    print("Nome: ", listaregistros[0])
		    print("Endereço:",listaregistros[1])
		    print("Celular: ",listaregistros[2])
		    print("CPF: ",listaregistros[3])
		    print("E-mail: ",listaregistros[4])
		    print("Senha: ",listaregistros[5])
		    print("\nCADASTRO 2:")
		    print("Nome: ", listaregistros[6])
		    print("Endereço:",listaregistros[7])
		    print("Celular: ",listaregistros[8])
		    print("CPF: ",listaregistros[9])
		    print("E-mail: ",listaregistros[10])
		    print("Senha: ",listaregistros[11])
		    print("\nCADASTRO 3:")
		    print("Nome: ", listaregistros[12])
		    print("Endereço:",listaregistros[13])
		    print("Celular: ",listaregistros[14])
		    print("CPF: ",listaregistros[15])
		    print("E-mail: ",listaregistros[16])
		    print("Senha: ",listaregistros[17])
		    print("\nCADASTRO 4:")
		    print("Nome: ", listaregistros[18])
		    print("Endereço:",listaregistros[19])
		    print("Celular: ",listaregistros[20])
		    print("CPF: ",listaregistros[21])
		    print("E-mail: ",listaregistros[22])
		    print("Senha: ",listaregistros[23])
		    print("\nCADASTRO 5:")
		    print("Nome: ", listaregistros[24])
		    print("Endereço:",listaregistros[25])
		    print("Celular: ",listaregistros[26])
		    print("CPF: ",listaregistros[27])
		    print("E-mail: ",listaregistros[28])
		    print("Senha: ",listaregistros[29])
		else :
			print('Sistema sem dados')
		if cal > 0 and cal < 3 :
			print("\nQual cadastro você quer atualizar? ")
			print("1- CADASTRO 1")
			print("2- CADASTRO 2")
			print("3- CADASTRO 3")
			print("4- CADASTRO 4")
			print("5- CADASTRO 5")
			print("6- TODOS OS CADASTROS")
		
			a = int(input("Digite a sua opção: "))
		
			if a==1:
				listaregistros[0]=input("NOME: ")
				listaregistros[1]=input("ENDEREÇO: ")
				listaregistros[2]=input("CELULAR: ")
				listaregistros[3]=input("CPF: ")
				listaregistros[4]=input("E-MAIL: ")
				listaregistros[5]=input("SENHA: ")
				print("\nDeseja confirmar seus dados? ")
				print("1- Sim")
				print("2- Não")
				l= int(input("Digite sua opção: "))
				if l==1:
					print("\nSeus dados estão confirmados no sistema. ")
				else:
					print("ATUALIZAÇÃO INVÁLIDA")
			elif a==2:
				listaregistros[0]=input("NOME: ")
				listaregistros[1]=input("ENDEREÇO: ")
				listaregistros[2]=input("CELULAR: ")
				listaregistros[3]=input("CPF: ")
				listaregistros[4]=input("E-MAIL: ")
				listaregistros[5]=input("SENHA: ")
				print("\nDeseja confirmar seus dados? ")
				print("1- Sim")
				print("2- Não")
				l= int(input("Digite sua opção: "))
				if l==1:
					print("\nSeus dados estão confirmados no sistema. ")
				else:
					print("ATUALIZAÇÃO INVÁLIDA")
			elif a==3:
				listaregistros[0]=input("NOME: ")
				listaregistros[1]=input("ENDEREÇO: ")
				listaregistros[2]=input("CELULAR: ")
				listaregistros[3]=input("CPF: ")
				listaregistros[4]=input("E-MAIL: ")
				listaregistros[5]=input("SENHA: ")
				print("\nDeseja confirmar seus dados? ")
				print("1- Sim")
				print("2- Não")
				l= int(input("Digite sua opção: "))
				if l==1:
					print("\nSeus dados estão confirmados no sistema. ")
				else:
					print("ATUALIZAÇÃO INVÁLIDA")
			elif a==4:
				listaregistros[0]=input("NOME: ")
				listaregistros[1]=input("ENDEREÇO: ")
				listaregistros[2]=input("CELULAR: ")
				listaregistros[3]=input("CPF: ")
				listaregistros[4]=input("E-MAIL: ")
				listaregistros[5]=input("SENHA: ")
				print("\nDeseja confirmar seus dados? ")
				print("1- Sim")
				print("2- Não")
				l= int(input("Digite sua opção: "))
				if l==1:
					print("\nSeus dados estão confirmados no sistema. ")
				else:
					print("ATUALIZAÇÃO INVÁLIDA")
			elif a==5:
				listaregistros[0]=input("NOME: ")
				listaregistros[1]=input("ENDEREÇO: ")
				listaregistros[2]=input("CELULAR: ")
				listaregistros[3]=input("CPF: ")
				listaregistros[4]=input("E-MAIL: ")
				listaregistros[5]=input("SENHA: ")
				print("\nDeseja confirmar seus dados? ")
				print("1- Sim")
				print("2- Não")
				l= int(input("Digite sua opção: "))
				if l==1:
					print("\nSeus dados estão confirmados no sistema. ")
				else:
					print("ATUALIZAÇÃO INVÁLIDA")
			elif a== 6:
				listaregistros[0]=input("NOME: ")
				listaregistros[1]=input("ENDEREÇO: ")
				listaregistros[2]=input("CELULAR: ")
				listaregistros[3]=input("CPF: ")
				listaregistros[4]=input("E-MAIL: ")
				listaregistros[5]=input("SENHA: ")
				listaregistros[6]=input("\nNOME: ")
				listaregistros[7]=input("ENDEREÇO: ")
				listaregistros[8]=input("CELULAR: ")
				listaregistros[9]=input("CPF: ")
				listaregistros[10]=input("E-MAIL: ")
				listaregistros[11]=input("SENHA: ")
				listaregistros[12]=input("\nNOME: ")
				listaregistros[13]=input("ENDEREÇO: ")
				listaregistros[14]=input("CELULAR: ")
				listaregistros[15]=input("CPF: ")
				listaregistros[16]=input("E-MAIL: ")
				listaregistros[17]=input("SENHA: ")
				listaregistros[18]=input("\nNOME: ")
				listaregistros[19]=input("ENDEREÇO: ")
				listaregistros[20]=input("CELULAR: ")
				listaregistros[21]=input("CPF: ")
				listaregistros[22]=input("E-MAIL: ")
				listaregistros[23]=input("SENHA: ")
				listaregistros[24]=input("\nNOME: ")
				listaregistros[25]=input("ENDEREÇO: ")
				listaregistros[26]=input("CELULAR: ")
				listaregistros[27]=input("CPF: ")
				listaregistros[28]=input("E-MAIL: ")
				listaregistros[29]=input("SENHA: ")
				print("\nDeseja confirmar seus dados? ")
				print("1- Sim")
				print("2- Não")
				l= int(input("Digite sua opção: "))
				if l==1:
					print("\nSeus dados estão confirmados no sistema. ")
				else:
					print("ATUALIZAÇÃO INVÁLIDA")
			else :
				print(' ')
		else:
			print(' ')
	elif t ==5:
		print("\nDESEJA SAIR DO SISTEMA? ")
		print("1- SIM")
		print("2- NÃO")
		
		s = int(input("Digite a sua opção: "))
		
		if s==1:
			print("\nVOCÊ SAIU DO SISTEMA.")
			i=5
		elif s>2:
				print("\nMENU CADASTRO")
		else:
			print("\nVOCÊ CONTINUA NO SISTEMA.")
	elif t>5:
		print("\nESSA OPÇÃO NÃO EXISTE. \nDIGITE UMA OPÇÃO DO MENU PRINCIPAL.")

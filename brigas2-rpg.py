#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class GloryTender:
	__doc__="""Classe dos heróis hernandinos"""

	nome=''
	golpe=''
	poder=0
	localizacao=''

	def __init__(self,nome,golpe,poder,localizacao):
		__doc__="""lets declarate"""
		self.nome = nome
		self.golpe = golpe
		self.poder = poder
		self.localizacao= localizacao

	def attack_enemy(self):
		__doc__="""Nosso herói atacará o inimigo"""
		print(self.nome+"atacou o inimigo com um"+self.golpe)
		
	def usa_arma(self):
		x = input("escolha uma instancia da arma que tu queres: ")
		print(self.nome + " usou " + x.nome +" e "+x.tiro_alvo())
                
class Gun:
	__doc__="""Ferramentas e instrumentos de guerra pros nossos heróis sairem no conflito e destruirem o inimigo"""
	nome=''
	poder=0
	
	def __init__(self,nome,poder):
		self.nome = nome
		self.poder = poder

	def tiro_alvo(self):

		sort = random.randint(1,10)

		if sort == 1:
			return ('atirou no chao!!!')
		elif sort ==2:
			return ('atirou dez metros acima do alvo')
		elif sort ==3:
			return ('acertou no alvo, mas na borda')
		elif sort ==4:
			return ('acertou quase no meio, eh um mestre!')
		elif sort ==5:
			return ('acertou no meio, voce estah pronto pra enfrentar a guerra!!!')
		else:
			return ('a arma nao funcionou!!!')


class Iterations:
	__doc__="""coloque dois objetos jogador aqui e 'bote as aranha pra brigá' """
	jogador1=''
	jogador2=''

	def __init__(self,jogador1,jogador2):
		self.jogador1=jogador1
		self.jogador2=jogador2
  
	def briga(self):
		print(self.jogador1.nome," deu um pontepé na bundo do ",self.jogador2.nome,", deixando ",self.jogador2.poder,"cm de cais aberto")

	def compara(self):
		if self.jogador1.poder > self.jogador2.poder:
			print(self.jogador1.nome+"é mais forte!")
		else:
			print(self.jogador2.nome+"é mais forte!")

#Fim do programa

mestre = GloryTender('Grande mestre ',' vai tomar caju!',6,'Virgínia')
rubens = GloryTender('Irmão Rubens','Seus cães gulosos!',3,'Fluminência')
pinto = GloryTender('Paulo Sérgio Pinto','Estamos encerrando Pampa Debates',4,'Alto Guaíba')

pistola = Gun("Pistola Calibre 38",4)
ak = Gun('AK-47',7)
espada = Gun('Espada',3)

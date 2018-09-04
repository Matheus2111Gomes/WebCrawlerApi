import bs4
import json
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq


#Função que serializa as ocorrencias
def serializar_ocorrencias(lista_urls, palavra):

	#Armazenara o array de todas as ocorrencias de cada link
	ocorrencias = []

	#Para cada link na lista sera feito o bloco de codigo
	for link in lista_urls:
		
		#formatando a pagina para html
		pag_url = str(uReq(link).read())
		pag_soup = soup(pag_url, "html.parser")

		#qtd de paragrafos <p> no html
		ct = paragrafos(pag_soup,palavra)
		
		#cria um dicionario com o link e a quantidade de ocorrencias
		ocorrencia = {"url":link, "qtd_de_ocorrencias": str(ct)}
		#adiciona o dicionario a lista de ocorrencias
		ocorrencias.append(ocorrencia)

		#printando no console a troca da url
		print("*************************************************************************")


	#retornando o array de dicionarios serializado no formato json
	#return json.dumps(ocorrencias, indent=4)
	return ocorrencias

#função que fara a busca dos paragrafos e de quais deles possuem a palavra buscada
def paragrafos(li,palavra_buscada):
	#encontrando todos os paragrafos
	paragrafos = li.findAll("p")
	contador = 0

	for p in paragrafos:
			
		# definindo p como substring de p para tudo q fique entre o inicio e o fim da tag de paragrafo
		p = str(p)[str(p).index(">")+1:str(p).index("</")]
		p = retirando_tag_link(p)
		

		
		#a função lower nesse caso impede que alguma ocorrencia passe despercebida por fator 
		#de caixa alta, caso a palavra esteja contida no paragrafo o contador sera acrescentado
		if palavra_buscada.lower() in p.lower():
			contador = contador+1		
			#Visualização no console de cada uma das ocorrencias
			print(p)
			print("---------------------------------------------------------------------------------")
		


	#a função retorna a quantidade de paragrafos que possuem a palavra
	return contador

#Função que retira trechos de tags de dentro do paragrafo
def retirando_tag_link(par):
	if "<a>" in par:
		par = par.replace("<a>","")
	if "<a" in par:
		par = par.replace(str(par[str(par).index("<a"):str(par).index('">') + 2]), "")
	if "</a>" in par:
		par = par.replace("</a>","")

	return par



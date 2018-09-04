import core
from bs4 import BeautifulSoup as soup

def test_retirando_tag_link():
	#usando o trecho seguinte de html, é possivel verificar a formatação do codigo no quesito de 
	#excluir dos paragrafos as tags <a>
	teste_texto = "<p> o <a>link</a> esta <a href=\"#\">formatado</a> </p>"
	paragraf = core.retirando_tag_link(teste_texto)
	assert paragraf == "<p> o link esta formatado </p>"


def test_paragrafos():
	#usando o trcho seguinte de html é possivel notar a forma como o codigo registra apenas 
	#as ocorrencias feitas dentro das tags de paragrafos
	teste_pag_html = soup("<html><head></head><body><h1>title</h1><p class=\"teste_class\">teste do paragrafo 1</p><h2> teste </h2> <p id=\"teste_id\">teste do paragrafo 2</p></body></html>", "html.parser")
	qtd_de_paragrafos = core.paragrafos(teste_pag_html,'teste')
	assert qtd_de_paragrafos == 2



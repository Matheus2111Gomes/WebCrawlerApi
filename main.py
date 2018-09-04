import core	#importando o core da aplicação
from flask import Flask #importando flask
from flask import request #importando modulo de requests
from flask import jsonify #importando modulo json
from werkzeug.contrib.cache import SimpleCache #importando caching

#definindo o tipo de cache que sera usado
#pelo fato da aplicação estar rodando no servidor local, sera utilizando o tipo
#SimpleCache para o armazenamento do processo
cache = SimpleCache()

#pelo fato da nossa api possuir apenas uma instancia de Flask, o nome dado sera o padrão __name__
app = Flask(__name__)


#rota principal que retornara o json
@app.route("/api", methods=['GET'])
def retornoJson():

	#strings que serão passadas pela url através do metodo GET
	word  = request.args['word']
	sites  = request.args['sites']


	#assim que entrar na view, daremos a variavel retorno o valor presente no cache com o titulo 'lista'
	retorno = cache.get('lista')
	
	#se o valor estiver vazio adicionaremos a função de serialização à variavel e setaremos o cache
	#dando o nome 'lista', valor do retorno, e o tempo limite de 1 minuto para permanecer na memoria
	if retorno is None:
		#as urls serão passadas com virgulas entre elas para delimita-las
		retorno = jsonify(core.serializar_ocorrencias(sites.split(","), word))
		cache.set('lista', retorno, timeout=60)
	
	return retorno 




if __name__ == '__main__':
	app.run(debug=False, port=8000)
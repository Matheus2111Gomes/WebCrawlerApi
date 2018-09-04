# WebCrawlerApi
Uma Api web desenvolvida em python utilizando os frameworks flask e beautifulsoup.   
Possui como proposito receber uma lista de URLs e encontrar nas paginas paragrafos contendo ocorrencias de uma determinada palavra (Web Crawler)

### Instalação

*Faça o download dos arquivos </n>   
*No seu terminal, navegue até o diretorio dos arquivos baixados e utilize o comando pip install -r requirements.txt para que seja instalado os frameworks necessario (recomendado criar um ambiente virtual para a instalação utilizando venv)

### Utilização

*Execute o arquivo "main.py" no terminal </n>   
*Assim que o servidor local estiver disponivel, entre em seu navegador e digite: </n>

http://127.0.0.1:8000/api?sites=siteUm,siteDois,siteTres&word=palavra

#####Obs: Passe os parametros de sites com uma virgula (,) separando-os

Após a execução, será exibido no navegador um json contendo a url do site e o numero de ocorrencias da palavra no mesmo
(é possivel ver cada uma das ocorrencias no terminal ao fim da execução do codigo.

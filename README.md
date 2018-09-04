# WebCrawlerApi
Uma Api web desenvolvida em python utilizando os frameworks flask e beautifulsoup.   
Possui como propósito receber uma lista de URLs e encontrar nas páginas, parágrafos contendo ocorrências de uma determinada palavra (Web Crawler).

### Instalação

*Faça o download dos arquivos.   
*Entre eles será encontrado o arquivo requirements.txt, certifiques-se de que seja instalado todos os frameworks listados no arquivo.

### Utilização

*Execute o arquivo "main.py" no terminal.    
*Assim que o servidor local estiver disponivel, entre em seu navegador e digite:   

http://127.0.0.1:8000/api?sites=siteUm,siteDois,siteTres&word=palavra

##### Obs: Passe os parametros de sites com apenas uma virgula (,) separando-os.

Após a execução, será exibido no navegador um json contendo a url do site e o numero de ocorrencias da palavra no mesmo
(é possivel ver cada uma das ocorrencias no terminal ao fim da execução do codigo.

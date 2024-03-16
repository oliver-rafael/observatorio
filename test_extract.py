from bs4.element import PreformattedString
import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.exceptions import HTTPError
import re

# Faz a verificacao do robots para, se a pagina permite craw
robots = None
URL = 'https://www.legislador.com.br/robots.txt'

#tratamento de excecoes
try:
  resposta = requests.get(URL)
  resposta.raise_for_status()
except HTTPError as exc:
  print(exc)
else:
  robots = resposta.text
# palavras chave para verificacao do robots
permite_crawling = True
if 'legislador' in robots.lower() or 'charts' in robots.lower():
  permite_crawling = False

#if permite_crawling == False:
  

conteudo = None # variavel recebe o conteudo da pagina
URL = 'https://www.legislador.com.br/LegisladorWEB.ASP?WCI=ProjetoTexto&ID=9&inEspecie=1&nrProjeto=45&aaProjeto=2024'

#tratamento de excecoes
try:
  resposta = requests.get(URL)
  resposta.raise_for_status()
except HTTPError as exc:
  print(exc)
else:
  conteudo=resposta.text

#Variavel recebe conteudo na página em html
pagina  = BeautifulSoup (conteudo, 'html.parser')

# iterando entre as linhas do arquivo para preencher os dados

conteudo_extraido = []
info_proj_lei = pagina.find_all('div',{'class':'card'})

for item in info_proj_lei:
  texto_coluna = []

  titulo_lei = item.find('h5',{'class':'card-title'})
  if titulo_lei:
    titulo_lei = titulo_lei.get_text().strip().replace('\xa0', ' ')
    texto_coluna.append(titulo_lei)

  data_lei = item.find('h6', {'class':'card-subtitle mb-2 text-muted'})
  if data_lei:
    data_lei = data_lei.get_text().strip().replace('\xa0', ' ')
    data= data_lei.replace('de', '')
    texto_coluna.append(data)

  autor_lei = item.find('dl',{'class':'row'})
  if autor_lei:
    autor_lei = autor_lei.get_text().strip().replace('\xa0', ' ')
    filtername = autor_lei.split(sep = '\n')
    realnome = (filtername[4]).replace('AutorExecutivo', '')
    texto_coluna.append(realnome)

  ementa_lei= item.find('p',{'class': 'card-text'})
  if ementa_lei :
    ementa_lei = ementa_lei.get_text().strip().replace('\xa0', ' ')
    texto_coluna.append(ementa_lei)

  conteudo_extraido.append(texto_coluna)

#salva informacoes em csv
dados_pro_lei = pd.DataFrame(conteudo_extraido, columns=['Título', 'Data', 'Autor', 'Ementa'])
dados_pro_lei.to_csv("projetos_de_lei.csv", index=False)
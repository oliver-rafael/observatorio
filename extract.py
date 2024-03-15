import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.exceptions import HTTPError
import re

# Métodos relacionados a recuperação das informações colocados dentro da classe.
class ProposicoesCrawler:

    def __init__(self, tipo="", data_inicio="", data_final=""):
        self.tipo_proposicao = tipo
        self.data_inicio = data_inicio
        self.data_final = data_final
        self.dados_proposicoes = {
            "tipo_proposicao": [],
            "numero_proposicao": [],
            "data_proposicao": [],
            "situacao_proposicao": [],
            "assunto_proposicao": [],
            "autor_proposicao": [],
            "texto_proposicao": []
        }

    # Esse método entra na página que permite escolher o tipo de proposição e o período de tempo de interesse.
    def __pagina_base(self):
        url_base = f'https://www.legislador.com.br/LegisladorWEB.ASP?WCI=ProposicaoConsulta&ID=9&dtInicial={self.data_inicio}&dtFinal={self.data_final}&tpProposicao={self.tipo_proposicao}&'
        return url_base

    # Esse método pega os dados da proposição do tipo escolhido mais recente dentro do intervalo de tempo inserido.
    def __gera_args(self):
        resposta = requests.get(self.__pagina_base())
        pagina = BeautifulSoup(resposta.content, 'html.parser')

        proposicao_info = pagina.find('a', {
            'class': 'btn btn-outline-secondary float-right d-flex justify-content-between align-items-center'})
        proposicao_info_link = re.split('[()]', proposicao_info['onclick'])[1].split(',')

        cam_proposicao = proposicao_info_link[0]
        num_proposicao = int(proposicao_info_link[2])
        tipo_proposicao = proposicao_info_link[1]
        ano_proposicao = proposicao_info_link[3]

        return cam_proposicao, tipo_proposicao, num_proposicao, ano_proposicao

    # Esse método gera os links do tipo de proposição de interesse no período especificado
    def gera_links(self):
        links_proposicoes = []
        args_proposicao = self.__gera_args()

        for proposicao in range(args_proposicao[2]):
            links_proposicoes.append(
                f'https://www.legislador.com.br/LegisladorWEB.ASP?WCI=ProposicaoTexto&ID={args_proposicao[0]}&TPProposicao={args_proposicao[1]}&nrProposicao={args_proposicao[2] - proposicao}&aaProposicao={args_proposicao[3]}')

        return links_proposicoes

    # Esse método armazena os dados das proposições em um dicionário
    def obter_dados(self, pagina):
        st_proposicao = len(pagina.find_all('dd', {'class': 'col-sm-9'}))

        self.dados_proposicoes["tipo_proposicao"].append(
            pagina.find('h5', {'class': 'card-title'}).get_text().split()[0])
        self.dados_proposicoes["numero_proposicao"].append(
            pagina.find('h5', {'class': 'card-title'}).get_text().split()[2])
        self.dados_proposicoes["data_proposicao"].append(
            pagina.find('h6', {'class': 'card-subtitle'}).get_text().split()[1])
        self.dados_proposicoes["situacao_proposicao"].append(
            pagina.find_all('dd', {'class': 'col-sm-9'})[2].get_text().split()[1] if st_proposicao == 5 else pagina.find_all('dd', {'class': 'col-sm-9'})[1].get_text())
        self.dados_proposicoes["assunto_proposicao"].append(
            pagina.find_all('dd', {'class': 'col-sm-9'})[3].get_text() if st_proposicao == 5 else pagina.find_all('dd', {'class': 'col-sm-9'})[2].get_text())
        self.dados_proposicoes["autor_proposicao"].append(
            pagina.find_all('dd', {'class': 'col-sm-9'})[4].get_text() if st_proposicao == 5 else pagina.find_all('dd', {'class': 'col-sm-9'})[3].get_text())
        self.dados_proposicoes["texto_proposicao"].append(re.sub(r"[\t\n\xa0\x93\x94\x95]"," ",pagina.find('p', {'class': 'card-text'}).get_text()))

        dados = self.dados_proposicoes
        return dados

# Dataframe
dados = pd.DataFrame(info)
dados


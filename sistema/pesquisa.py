import json
from sistema import destino_turistico
from config import db_dir
from sistema.algoritmos import LinkedList, ordenar_por_insercao, ordenar_bubblesort

class Pesquisa:
    """
    Class responsavel por realizar pesquisas de destinos turisticos

    Atributos:
    destinos (LinkedList): Lista ligada com todos os destinos turisticos
    historico_pesquisa (list): Lista com os destinos pesquisados 
    """
    def __init__(self, destinos):
        """
        Inicializa a classe Pesquisa

        Parametros:
        destinos (list): Lista de destinos turisticos
        """
        self.destinos = LinkedList()
        for destino in destinos:
            self.destinos.append(destino_turistico.DestinoTuristico(destino['designacao'], destino['pais'], destino['cidade'], destino['coordenadas'],
                                 destino['informacoes_url']))
        
        self.historico_pesquisa = []

    def pesquisar(self, pais=None, cidade=None, proximidade_aeroportos=False):
        """
        Pesquisa destinos turisticos com base nos parametros fornecidos

        Parametros:
        pais (str): Pais a pesquisar
        cidade (str): Cidade a pesquisar
        proximidade_aeroportos (bool): Se verdadeiro, pesquisa destinos proximos a aeroportos

        Retorna:
        LinkedList: Lista ligada aos destinos turisticos encontrados
        """
        resultados = LinkedList()
        for destino in self.destinos:
            if pais and destino.pais.lower() == pais:
                resultados.append(destino)
            elif cidade and destino.cidade.lower() == cidade:
                resultados.append(destino)
            elif proximidade_aeroportos:
                pass

        if  resultados.head is None:
            print("Nenhum resultado encontrado")
            return

        ordenar_por_insercao(resultados)

        self.historico_pesquisa.append({
            'cidade': cidade,
            'pais': pais,
            "proximidade_aeroportos": proximidade_aeroportos
        })

        for destino in resultados:
            print(destino)

    def consultar_destinos_mais_procurados(self):
        """
        Consulta os destinos mais procurados com base no historico de pesquisa

        Retorna:
        list: Lista de destinos turisticos mais procurados
        """
        with open(f"{db_dir}/historico.json", 'r') as f:
            historico = json.load(f)

        contagem_destinos = {}

        for item in historico:
            cidade_historico = item.get("cidade")
            pais_historico = item.get("pais")
            if cidade_historico:
                if cidade_historico in contagem_destinos:
                    contagem_destinos[cidade_historico] += 1
                else:
                    contagem_destinos[cidade_historico] = 1
            elif pais_historico:
                if pais_historico in contagem_destinos:
                    contagem_destinos[pais_historico] += 1
                else:
                    contagem_destinos[pais_historico] = 1

        most_searched_destino = max(contagem_destinos, key=contagem_destinos.get)

        matching_destinos = [destino for destino in self.destinos if
                             destino.pais.lower() == most_searched_destino.lower() or destino.cidade.lower() == most_searched_destino.lower()]

        ordenar_bubblesort(matching_destinos)
        return matching_destinos

    @staticmethod
    def consultar_novidades():
        """
        Consulta novidades nos ficheiros de companhias e destinos turisticos

        Retorna:
        None
        """
        ficheiros = ["sata.json", "tap.json", "destinos.json"]
        print("==== Novidades ====")
        for ficheiro in ficheiros:
            ficheiro_atual_diretorio = f"{db_dir}/{ficheiro}"
            ficheiro_antigo_diretorio = f"{db_dir}/prev_{ficheiro}"

            with open(ficheiro_atual_diretorio, 'r') as f:
                dados_ficheiro_atual = json.load(f)

            try:
                with open(ficheiro_antigo_diretorio, 'r') as f:
                    dados_ficheiro_antigo = json.load(f)
            except FileNotFoundError:
                dados_ficheiro_antigo = None

            if dados_ficheiro_atual != dados_ficheiro_antigo:
                print(f"#### Novidades encontradas em {ficheiro[:-5].title()} ####")
                if dados_ficheiro_antigo is not None:
                    novas_entradas = [entrada for entrada in dados_ficheiro_atual if entrada not in dados_ficheiro_antigo]
                    for entrada in novas_entradas:
                        if ficheiro != "destinos.json":
                            print(f"Nova rota encontrada: {entrada['origem']} -> {entrada['destino']}")
                        else:
                            destino = destino_turistico.DestinoTuristico(entrada['designacao'], entrada['pais'],
                                                                         entrada['cidade'], entrada['coordenadas'],
                                                                         entrada['informacoes_url'])

                            print(destino)

                with open(ficheiro_antigo_diretorio, 'w') as f:
                    json.dump(dados_ficheiro_atual, f)

            else:
                print(f"#### Nenhuma novidade encontrada em {ficheiro[:-5].title()}. ####")

    def salvar_historico(self):
        """
        Salva o historico de pesquisa num ficheiro json

        Retorna:
        None
        """
        if len(self.historico_pesquisa) > 0:
            try:
                with open(f"{db_dir}/historico.json", 'r') as f:
                    historico_existente = json.load(f)
            except FileNotFoundError:
                historico_existente = []

            historico_existente.extend(self.historico_pesquisa)

            with open(f"{db_dir}/historico.json", 'w') as f:
                json.dump(historico_existente, f)

            print("Historico atualizado")

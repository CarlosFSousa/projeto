import sys
from sistema import pesquisa

class Menu:

    def __init__(self, aeroportos, destinos, historico):
        self.aeroportos = aeroportos
        self.destinos = destinos
        self.historico = historico
        self.pesquisa = pesquisa.Pesquisa(self.destinos)
        self.opcoes = {
            "1": self.menu_pesquisa,
            "2": self.menu_novidades,
            "3": self.menu_destinos_procurados,
            "4": self.menu_avaliacao,
            "5": self.sair
        }

    def menu_inicial(self):

        while True:
            print("==== Menu ====")
            print("1. Pesquisar destinos turisticos")
            print("2. Consultar novidades")
            print("3. Consultar os destinos mais procurados")
            print("4. Avaliar Aplicacao")
            print("5. Sair")

            input_utilizador = input("Insira uma das opcoes: ")
            if input_utilizador in self.opcoes:
                self.opcoes[input_utilizador]()
            else:
                print("Por favor, insira uma das opcoes possiveis.")

    def menu_pesquisa(self):
        while True:
            print("==== Pesquisar Destinos ====")
            print("1. Pais")
            print("2. Cidade")
            print("3. Proximidade a aeroportos")
            print("4. Voltar")

            user_input = input("Insira uma das opcoes: ")

            if user_input == "1":
                pais = input("Insira o pais: ")
                self.pesquisa.pesquisar(pais=pais.lower())
            elif user_input == "2":
                cidade = input("Insira a cidade: ")
                self.pesquisa.pesquisar(cidade=cidade.lower())
            elif user_input == "3":
                self.pesquisa.pesquisar(proximidade_aeroportos=True)
            elif user_input == "4":
                self.menu_inicial()
            else:
                print("Por favor, insira uma das opcoes possiveis.")

    def menu_novidades(self):
        self.pesquisa.consultar_novidades()

    def menu_destinos_procurados(self):
        print("==== Destinos Mais Procurados ====")
        matching_destinos = self.pesquisa.consultar_destinos_mais_procurados()
        for i, destino in enumerate(matching_destinos, start=1):
            print(f"{i}. {destino}")

    @staticmethod
    def menu_avaliacao():
        while True:
            print("Como classifica a aplicacao?")
            print("#############################")
            print("1 - nada satisfeito.")
            print("2 - pouco satisfeito.")
            print("3 - satisfeito")
            print("4 - muito satisfeito")
            print("#############################")

            input_utilizador = input("Insira uma das opcoes:")

            if input_utilizador in ["1", "2", "3", "4"]:
                print("Obrigado pela sua avaliacao!")
                return input_utilizador
            else:
                print("Por favor, insira uma das opcoes possiveis.")

    def sair(self):
        self.pesquisa.salvar_historico()
        sys.exit()

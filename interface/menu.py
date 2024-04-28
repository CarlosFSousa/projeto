class Menu:

    def __init__(self):
        self.possibilidades = ["1", "2", "3", "4"]

    def menu_inicial(self):
        while True:
            print("#######################################")
            print("Menu")
            print("1 - Pesquisar destinos turisticos")
            print("2 - Consultar novidades")
            print("3 - Consultar os destinos mais procurados")
            print("4 - Avaliar Aplicacao")
            print("5 - Sair")
            print("#######################################")

            input_utilizador = input("Insira uma das opcoes: ")

            match input_utilizador:
                case "1":
                    # pesquisa_destinos()
                    pass
                case "2":
                    pass
                case "3":
                    pass
                case "4":
                    resultado = self.menu_avaliacao()
                    print(f"Avaliado em {resultado}")
                    # save(resultado,"avaliacao")
                    pass
                case "5":
                    break
                case _:
                    print("Por favor insira um numero valido")

    def menu_avaliacao(self):
        while True:
            print("Como classifica a aplicacao?")
            print("#############################")
            print("1 - nada satisfeito.")
            print("2 - pouco satisfeito.")
            print("3 - satisfeito")
            print("4 - muito satisfeito")
            print("#############################")

            input_utilizador = input("Insira uma das opcoes:")

            if input_utilizador in self.possibilidades:
                return input_utilizador
            else:
                print("Por favor, insira uma das opcoes possiveis.")


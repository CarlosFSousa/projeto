class Companhia:
    """
    Companhia Area

    Atributos:
    nome (str): Nome da companhia
    data (str): Data do voo
    origem (str): Aeroporto de origem
    destino (str): Aeroporto de destino
    duracao (str): Duracao do voo
    """
    def __init__(self, data, origem, destino, duracao):
        self.data = data
        self.origem = origem
        self.destino = destino
        self.duracao = duracao

    def __str__(self):
        return f"\n Data: {self.data}\nOrigem: {self.origem}\nDestino: {self.destino}\nDuracao: {self.duracao}\n"

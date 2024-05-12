class DestinoTuristico:
    """
    Destino turistico

    Atributos:
    designacao (str): Designacao do destino
    pais (str): Pais do destino
    cidade (str): Cidade do destino
    coordenadas (dict): Coordenadas do destino
    informacoes_url (str): URL com mais informacoes sobre o destino

    """
    def __init__(self, designacao, pais, cidade, coordenadas, informacoes_url):
        self.designacao = designacao
        self.pais = pais
        self.cidade = cidade
        self.coordenadas = coordenadas
        self.informacoes_url = informacoes_url

    def __str__(self):
        return f"\nDesignacao: {self.designacao}\nCountry: {self.pais}\nCity: {self.cidade}\nCoordinates: \nLatitude: {self.coordenadas['latitude']} \nLongitude: {self.coordenadas['longitude']} \nMore Info: {self.informacoes_url}\n"
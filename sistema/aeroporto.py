class Aeroporto:
    """
    Aeroporto

    Atributos:
    id (str): ID do aeroporto
    nome (str): Nome do aeroporto
    cidade (str): Cidade do aeroporto
    pais (str): Pais do aeroporto
    iata (str): Codigo IATA do aeroporto
    icao (str): Codigo ICAO do aeroporto
    longitude (str): Longitude do aeroporto
    latitude (str): Latitude do aeroporto
    altitude (str): Altitude do aeroporto
    dst (str): DST do aeroporto
    tz (str): TZ do aeroporto
    
    """

    def __init__(self, id, nome, cidade, pais, iata, icao, longitude, latitude, altitude, dst, tz):
        self.id = id
        self.nome = nome
        self.cidade = cidade
        self.pais = pais
        self.iata = iata
        self.icao = icao
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.dst = dst
        self.tz = tz

    def __str__(self):
        return f"Nome: {self.nome}\nCidade: {self.cidade}\nPais: {self.pais}\nIATA: {self.iata}\nICAO: {self.icao}\nLongitude: {self.longitude}\nLatitude: {self.latitude}\nAltitude: {self.altitude}\nDST: {self.dst}\nTZ: {self.tz}\n"
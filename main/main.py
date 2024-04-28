"""
Carlos Fontes e Sousa
Para que o match funcione, e necessario a versao de python 3.10, no minimo
"""
import json
import os
from projeto.interface.menu import Menu

current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)
database_directory = os.path.join(parent_directory, "db")


def main():
    aeroportos = json.load(open(f'{database_directory}/aeroportos.json', 'r', encoding='utf-8'))
    destinos = json.load(open(f'{database_directory}/destinos.json', 'r', encoding='utf-8'))
    sata = json.load(open(f'{database_directory}/sata.json', 'r', encoding='utf-8'))
    tap = json.load(open(f'{database_directory}/tap.json', 'r', encoding='utf-8'))
    historico = json.load(open(f'{database_directory}/historico.json', 'r', encoding='utf-8'))

    main_menu = Menu()
    main_menu.menu_inicial()


if __name__ == '__main__':
    main()

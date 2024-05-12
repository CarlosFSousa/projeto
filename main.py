"""
Carlos Fontes e Sousa - 11/05/2024
20142407
"""

import json
from interface.menu import Menu
from config import db_dir


def main():
    aeroportos = json.load(open(f'{db_dir}/aeroportos.json', 'r', encoding='utf-8'))
    destinos = json.load(open(f'{db_dir}/destinos.json', 'r', encoding='utf-8'))
    historico = json.load(open(f'{db_dir}/historico.json', 'r', encoding='utf-8'))
    sata = json.load(open(f'{db_dir}/sata.json', 'r', encoding='utf-8'))
    tap = json.load(open(f'{db_dir}/tap.json', 'r', encoding='utf-8'))

    main_menu = Menu(aeroportos, destinos, historico)
    main_menu.menu_inicial()


if __name__ == '__main__':
    main()

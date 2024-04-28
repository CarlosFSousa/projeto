import csv
import json


def convert_dat_to_json(input_file, output_file):
    airports = []
    with open(input_file, 'r', encoding='utf-8') as dat_file:
        reader = csv.reader(dat_file)
        for row in reader:
            airport = {
                'id': row[0],
                'nome': row[1],
                'cidade': row[2],
                'pais': row[3],
                'iata': row[4],
                'icao': row[5],
                'latitude': row[6],
                'longitude': row[7],
                'altitude': row[8],
                'timezone': row[9],
                'dst': row[10],
                'tz_database_time_zone': row[11],
                # hidden properties
                # 'type':row[12],
                # 'source':row[13]
            }
            airports.append(airport)

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(airports, json_file, ensure_ascii=False, indent=4)


convert_dat_to_json('./db/airports.dat', './db/aeroportos.json')



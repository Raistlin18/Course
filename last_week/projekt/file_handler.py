import csv
import sys

def get_dicts_from_csv(file_name):
    csv_list = []
    try:
        with open(file_name, 'r', encoding='utf-8') as forras:
            for i in csv.DictReader(forras):
                csv_list.append(i)
    except OSError:
        sys.exit('Hiba a fájl kezelése közben!')
    else:
        return tuple(csv_list)

def write_dicts_to_csv(file_name, list1):
    try:
        with open(file_name, 'w', encoding='utf-8') as cel:
            kulcsok = tuple(list1[0].keys())

            writer = csv.DictWriter(cel, kulcsok)
            writer.writeheader()

            for i in list1:
                writer.writerow(i)
    except OSError:
        sys.exit('A fájlt nem sikerült létrehozni')
    else:
        return 'Fájl létrehozva!'

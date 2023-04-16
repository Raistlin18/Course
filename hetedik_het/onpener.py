import csv
def read_csv(file_name):
    csv_list = []
    with open(file_name, 'r', encoding='utf-8') as forras:
        csv.reader(forras)
        csv_list = [x for x in csv.reader(forras)]
    return csv_list

print(read_csv('meetup.csv'))
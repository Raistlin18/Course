import csv
import sys
from pprint import pp


result = [{
    'by': 'count',
    'popularity': '1224.000000',
    'best_price': '1224.000000',
    'lowest_price': '964.000000',
    'highest_price': '964.000000',
    'sellers_amount': '1224.000000',
    'screen_size': '1222.000000',
    'memory_size': '1112.000000',
    'battery_size': '1214.000000'
}, {
    'by': 'mean',
    'popularity': '612.500000',
    'best_price': '7941.206699',
    'lowest_price': '7716.018672',
    'highest_price': '9883.410788',
    'sellers_amount': '16.743464',
    'screen_size': '5.394378',
    'memory_size': '95.700059',
    'battery_size': '3608.201812'
}, {
    'by': 'std',
    'popularity': '353.482673',
    'best_price': '8891.836260',
    'lowest_price': '8560.959059',
    'highest_price': '11514.936818',
    'sellers_amount': '20.597006',
    'screen_size': '1.476991',
    'memory_size': '111.922576',
    'battery_size': '1668.268774'
}, {
    'by': 'min',
    'popularity': '1.000000',
    'best_price': '214.000000',
    'lowest_price': '198.000000',
    'highest_price': '229.000000',
    'sellers_amount': '1.000000',
    'screen_size': '1.400000',
    'memory_size': '0.003200',
    'battery_size': '460.000000'
}, {
    'by': '25%',
    'popularity': '306.750000',
    'best_price': '2599.750000',
    'lowest_price': '2399.000000',
    'highest_price': '2887.000000',
    'sellers_amount': '2.000000',
    'screen_size': '5.162500',
    'memory_size': '32.000000',
    'battery_size': '2900.000000'
}, {
    'by': '50%',
    'popularity': '612.500000',
    'best_price': '4728.000000',
    'lowest_price': '4574.000000',
    'highest_price': '5325.500000',
    'sellers_amount': '8.000000',
    'screen_size': '6.000000',
    'memory_size': '64.000000',
    'battery_size': '3687.000000'
}, {
    'by': '75%',
    'popularity': '918.250000',
    'best_price': '9323.000000',
    'lowest_price': '9262.250000',
    'highest_price': '12673.750000',
    'sellers_amount': '26.000000',
    'screen_size': '6.400000',
    'memory_size': '128.000000',
    'battery_size': '4400.000000'
}, {
    'by': 'max',
    'popularity': '1224.000000',
    'best_price': '56082.000000',
    'lowest_price': '49999.000000',
    'highest_price': '69999.000000',
    'sellers_amount': '125.000000',
    'screen_size': '8.100000',
    'memory_size': '1000.000000',
    'battery_size': '18800.000000'
}]


# def get_dict_from_csv(file_name):
#     csv_list = []
#
#     try:
#         with open(file_name, 'r', encoding='utf-8') as forras:
#             for i in csv.DictReader(forras):
#                 csv_list.append(i)
#
#     except OSError:
#         exit('Hiba, a fájl kezelése közben!')
#
#     else:
#         return tuple(csv_list)
#
#
# pp(get_dict_from_csv('phones.csv'))


def write_dicts_to_csv(file_name, lista_tupli):
    try:
        with open(file_name, 'w', encoding='utf-8') as cel:
            kulcsok = tuple(lista_tupli[0].keys())

            writer = csv.DictWriter(cel, kulcsok)
            writer.writeheader()

            for i in lista_tupli:
                writer.writerow(i)
    except OSError:
        sys.exit('A fájlt nem sikerült létrehozni')
    else:
        print('Fájl létrehozva!')


write_dicts_to_csv('result.csv', result)
